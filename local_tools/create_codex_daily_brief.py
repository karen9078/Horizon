#!/usr/bin/env python3
"""Create the daily Codex AI media brief with fallbacks."""

from __future__ import annotations

import json
import re
import sqlite3
import subprocess
import sys
from datetime import date
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen
from xml.etree import ElementTree


CODEX = Path('/Applications/ChatGPT.app/Contents/Resources/codex')
RUNTIME_WORKDIR = Path('/Users/karen/.codex/automation-workdir')
SIDEBAR_PROJECT = Path('/Users/karen/Documents/Obsidian ')
CODEX_DB = Path('/Users/karen/.codex/state_5.sqlite')
OUT_DIR = Path('/Users/karen/.codex/logs/horizon-daily-brief')
RAW_BASE = 'https://raw.githubusercontent.com/karen9078/Horizon/gh-pages/_posts'
USER_AGENT = 'Mozilla/5.0 KarenDailyBrief/1.0'


RSS_FEEDS = [
    ('OpenAI News', 'https://openai.com/news/rss.xml'),
    ('Simon Willison', 'https://simonwillison.net/atom/everything/'),
    ('GitHub AI and ML', 'https://github.blog/ai-and-ml/feed/'),
    ('Vercel Blog', 'https://vercel.com/atom'),
    ('LangChain Blog', 'https://blog.langchain.com/rss/'),
]

HN_QUERIES = [
    'AI coding agent',
    'Claude Code',
    'Cursor AI',
    'MCP agent',
    'OpenAI Codex',
]


def fetch_text(url: str, timeout: int = 10) -> str | None:
    try:
        request = Request(url, headers={'User-Agent': USER_AGENT})
        with urlopen(request, timeout=timeout) as response:
            return response.read().decode('utf-8', errors='replace')
    except (HTTPError, URLError, TimeoutError, OSError):
        return None


def today_title(day: date) -> str:
    return f'AI每日简报 / {day.month} 月 {day.day} 号简报'


def horizon_report(day: date) -> str | None:
    return fetch_text(f'{RAW_BASE}/{day.isoformat()}-summary-zh.md', timeout=12)


def clean_text(text: str) -> str:
    return re.sub(r'\s+', ' ', text or '').strip()


def xml_text(element: ElementTree.Element, names: list[str]) -> str:
    for name in names:
        found = element.find(name)
        if found is not None and found.text:
            return clean_text(found.text)
    return ''


def collect_rss_items(limit_per_feed: int = 5) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for feed_name, url in RSS_FEEDS:
        xml = fetch_text(url, timeout=8)
        if not xml:
            continue
        try:
            root = ElementTree.fromstring(xml)
        except ElementTree.ParseError:
            continue

        channel_items = root.findall('.//item')
        if channel_items:
            for item in channel_items[:limit_per_feed]:
                title = xml_text(item, ['title'])
                link = xml_text(item, ['link'])
                desc = xml_text(item, ['description'])
                if title:
                    items.append({
                        'source': feed_name,
                        'title': title,
                        'url': link,
                        'summary': desc[:500],
                    })
            continue

        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        for entry in root.findall('.//atom:entry', ns)[:limit_per_feed]:
            title = xml_text(entry, ['{http://www.w3.org/2005/Atom}title'])
            summary = xml_text(entry, ['{http://www.w3.org/2005/Atom}summary', '{http://www.w3.org/2005/Atom}content'])
            link = ''
            link_el = entry.find('{http://www.w3.org/2005/Atom}link')
            if link_el is not None:
                link = str(link_el.attrib.get('href') or '')
            if title:
                items.append({
                    'source': feed_name,
                    'title': title,
                    'url': link,
                    'summary': summary[:500],
                })
    return items


def collect_hn_items(limit_per_query: int = 4) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    seen: set[str] = set()
    for query in HN_QUERIES:
        url = f'https://hn.algolia.com/api/v1/search_by_date?query={quote(query)}&tags=story&hitsPerPage={limit_per_query}'
        text = fetch_text(url, timeout=8)
        if not text:
            continue
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            continue
        for hit in data.get('hits', []):
            title = clean_text(hit.get('title') or hit.get('story_title') or '')
            link = clean_text(hit.get('url') or hit.get('story_url') or '')
            if not title or title in seen:
                continue
            seen.add(title)
            created = hit.get('created_at') or ''
            try:
                parsedate_to_datetime(created.replace('Z', '+0000'))
            except Exception:
                pass
            items.append({
                'source': f'Hacker News: {query}',
                'title': title,
                'url': link,
                'summary': f'points: {hit.get("points")}, comments: {hit.get("num_comments")}',
            })
    return items


def fallback_report(day: date) -> str:
    items = collect_rss_items() + collect_hn_items()
    if not items:
        items = [
            {
                'source': 'Fallback',
                'title': '今日自动资讯源暂时不可用',
                'url': '',
                'summary': '请基于 AI 编程、Agent、MCP、Codex、Claude Code、Cursor 等方向生成今日选题框架，并提示稍后可补充最新链接。',
            }
        ]

    lines = [
        f'# {day.isoformat()} AI 自媒体简报素材',
        '',
        '说明：Horizon 今日 raw 日报未发布，以下为自动兜底抓取的可靠资讯源素材。',
        '',
    ]
    for index, item in enumerate(items[:24], 1):
        lines.extend([
            f'## {index}. {item["title"]}',
            f'- 来源：{item["source"]}',
            f'- 链接：{item["url"] or "无"}',
            f'- 摘要：{item["summary"] or "无"}',
            '',
        ])
    return '\n'.join(lines)


def compact_report(markdown: str, limit: int = 18000) -> str:
    cleaned = re.sub(r'\n{3,}', '\n\n', markdown).strip()
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[:limit] + '\n\n[内容过长，后文已截断，请基于以上重点整理。]'


def thread_exists(title: str) -> bool:
    if not CODEX_DB.exists():
        return False
    with sqlite3.connect(CODEX_DB) as conn:
        row = conn.execute(
            'SELECT 1 FROM threads WHERE title = ? AND archived = 0 LIMIT 1',
            (title,),
        ).fetchone()
    return row is not None


def latest_thread_id() -> str | None:
    if not CODEX_DB.exists():
        return None
    with sqlite3.connect(CODEX_DB) as conn:
        row = conn.execute(
            'SELECT id FROM threads ORDER BY created_at DESC LIMIT 1',
        ).fetchone()
    return row[0] if row else None


def update_thread(thread_id: str, title: str) -> None:
    with sqlite3.connect(CODEX_DB) as conn:
        conn.execute(
            'UPDATE threads SET title = ?, cwd = ? WHERE id = ?',
            (title, str(SIDEBAR_PROJECT), thread_id),
        )
        conn.commit()


def run_codex(title: str, report_day: date, report_text: str, source_kind: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    RUNTIME_WORKDIR.mkdir(parents=True, exist_ok=True)
    output_file = OUT_DIR / f'codex-daily-brief-{report_day.isoformat()}.md'
    prompt = f"""请生成今天的中文 AI 自媒体选题工作台。

任务标题：{title}
素材来源：{source_kind}

要求：
1. 内容清爽，不要杂乱，不要输出配置过程。
2. 重点服务 AI 自媒体博主选题。
3. 优先关注 AI 编程、AI 智能体、Codex、Claude Code、Cursor、MCP、Agent 框架、开发者工具和大模型产品动态。
4. 输出今日最值得关注的 5 条资讯，按自媒体流量潜力排序。
5. 每条包含：爆点、目标受众、为什么值得讲。
6. 每条给出小红书 / B站 / 视频号标题建议。
7. 每条给出封面文案建议。
8. 最推荐的一条，写一版 60 秒短视频脚本。
9. 给出不同平台发布版本建议。
10. 如果素材来自兜底源，可以正常产出，不要让用户再来询问。

素材：

{compact_report(report_text)}
"""
    cmd = [
        str(CODEX),
        'exec',
        '-C',
        str(RUNTIME_WORKDIR),
        '--skip-git-repo-check',
        '--sandbox',
        'danger-full-access',
        '-o',
        str(output_file),
        prompt,
    ]
    before = latest_thread_id()
    result = subprocess.run(
        cmd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=1200,
        check=False,
    )
    log_path = OUT_DIR / f'codex-daily-brief-{report_day.isoformat()}.log'
    log_path.write_text(result.stdout, encoding='utf-8')
    if result.returncode != 0:
        raise RuntimeError(f'Codex failed with exit code {result.returncode}. See {log_path}')

    after = latest_thread_id()
    if after and after != before:
        update_thread(after, title)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    report_day = date.today()
    title = today_title(report_day)
    if thread_exists(title):
        print(json.dumps({'status': 'exists', 'title': title}, ensure_ascii=False))
        return 0

    report = horizon_report(report_day)
    source_kind = 'Horizon raw daily report'
    if not report:
        report = fallback_report(report_day)
        source_kind = 'fallback RSS + Hacker News sources'

    run_codex(title, report_day, report, source_kind)
    print(json.dumps({'status': 'created', 'title': title, 'source': source_kind}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        raise SystemExit(1)
