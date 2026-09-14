---
layout: default
title: "Horizon Summary: 2026-09-14 (ZH)"
date: 2026-09-14
lang: zh
---

> 从 22 条内容中筛选出 7 条重要资讯。

---

1. [Signal 将利用零知识证明实现无需手机号注册](#item-1) ⭐️ 8.0/10
2. [汽车正在收集并向第三方出售驾驶员数据](#item-2) ⭐️ 8.0/10
3. [Mullenweg 在董事会试图罢免后回归 Automattic CEO 职位](#item-3) ⭐️ 8.0/10
4. [谷歌持续投放诈骗广告引发众怒](#item-4) ⭐️ 8.0/10
5. [Perplexity 采用 GPT-6 Astra 实现自主化生产运维](#item-5) ⭐️ 8.0/10
6. [Fable 5.1 破解 370 年前的 Cyphral Distich 密码](#item-6) ⭐️ 7.0/10
7. [OpenAI 通过 Agents API 公开测试版开放 Codex Harness](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Signal 将利用零知识证明实现无需手机号注册](https://community.signalusers.org/t/registration-without-a-phone-number/2222?page=10) ⭐️ 8.0/10

根据社区讨论和代码提交，Signal 计划允许用户使用零知识证明在无需手机号的情况下完成注册。该实现可能要求通过 Google Play Billing 进行购买以缓解垃圾信息问题，同时保留短信验证选项。 此举标志着广泛使用的安全通讯应用在隐私保护方面取得重大进步，因为它可以将身份与手机号解耦并减少元数据暴露。这可能会影响其他消息平台采用类似的隐私保护注册方式。 零知识证明将允许用户在不透露凭证的情况下证明其拥有有效凭证，但具体机制以及是否能完全防止垃圾信息仍不明确。社区成员还指出，当前发布周期已支持无 SIM 卡的 Android 平板作为一等附属设备。

hackernews · Cider9986 · 9月13日 21:47 · [社区讨论](https://news.ycombinator.com/item?id=49689048)

**背景**: Signal 是一款以强端到端加密著称的消息应用，但历来要求使用手机号注册，这将账户与现实身份绑定。零知识证明是一种密码学协议，允许一方在不透露任何底层信息的情况下证明某个陈述为真，并越来越多地用于隐私保护系统中以匿名验证凭证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-knowledge_proof">Zero-knowledge proof - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Signal_(software)">Signal (software) - Wikipedia</a></li>
<li><a href="https://signal.org/">Signal Messenger: Speak Freely</a></li>

</ul>
</details>

**社区讨论**: 社区情绪褒贬不一：一些人欢迎隐私潜力和新的平板支持，而另一些人则批评基础设施自动化缺乏透明度，并质疑仅靠零知识证明是否足以保护隐私。还有人担心使用 Google Play Billing 来缓解垃圾信息，以及无需手机号注册是否真的已经可用。

**标签**: `#Signal`, `#zero-knowledge proofs`, `#privacy`, `#secure messaging`, `#authentication`

---

<a id="item-2"></a>
## [汽车正在收集并向第三方出售驾驶员数据](https://www.theverge.com/column/994172/your-car-is-selling-your-data) ⭐️ 8.0/10

The Verge 的一篇专栏文章详细描述了现代联网汽车如何收集驾驶员数据（包括位置、速度和生物特征信息）并将其出售给第三方，在 Hacker News 上引发了关于隐私和监管的热烈讨论。评论者分享了个人数据收集经历，并指出加州 AB-1542 法案将禁止出售敏感地理位置数据。 这一问题影响数百万可能不知道自己的车辆数据正被变现的驾驶员，引发了重大的隐私和消费者保护担忧。这也表明监管机构对汽车数据的关注日益增加，像 AB-1542 这样的法律可能重塑汽车制造商和数据经纪商的运营方式。 收集的数据包括敏感类别，如精确到 1850 英尺以内的地理位置，AB-1542 将其归类为敏感个人信息。即使驾驶员在配套应用中禁用了数据收集，某些数据仍可能被共享，而且选择退出通常不会删除已收集的数据。

hackernews · bookofjoe · 9月13日 13:45 · [社区讨论](https://news.ycombinator.com/item?id=49683953)

**背景**: 联网汽车配备了传感器和互联网连接，可实现导航和远程解锁等功能，但它们也会持续收集驾驶行为、位置甚至生物特征数据。这些数据可被出售给第三方，用于保险风险评估、营销和城市规划等目的，通常未经消费者明确同意。美国联邦贸易委员会警告称，此类收集和使用可能违反现行法律，而加州 AB-1542 等法规旨在限制敏感数据的出售。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2024/05/cars-consumer-data-unlawful-collection-use">Cars & Consumer Data: On Unlawful Collection & Use | Federal Trade Commission</a></li>
<li><a href="https://www.consumerreports.org/electronics/personal-information/how-to-stop-your-car-from-collecting-sharing-driving-data-a1233378612/">Stop Your Car From Collecting and Sharing Your Driving Data - Consumer Reports</a></li>
<li><a href="https://www.monda.ai/blog/automotive-data-monetization">Automotive Data Monetization : Trends & Examples 2025 | Monda</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了强烈的隐私担忧，分享了个人经历：即使禁用了数据收集，仍发现自己的里程数被报告给 Carfax 等服务。一些人强调了行业历史行为，例如一家德国汽车制造商寻求收集和出售车辆数据却无明确目的，而另一些人指出加州 AB-1542 可能很快使此类数据销售非法。少数人批评 The Verge 投放侵犯隐私的广告，指责其虚伪。

**标签**: `#privacy`, `#automotive`, `#data-collection`, `#regulation`, `#consumer-protection`

---

<a id="item-3"></a>
## [Mullenweg 在董事会试图罢免后回归 Automattic CEO 职位](https://techcrunch.com/2026/09/12/automattic-confirms-mullenweg-has-returned-as-ceo-after-attempted-ouster-by-board/) ⭐️ 8.0/10

Matt Mullenweg 在董事会将其停职带薪休假、并任命 CFO Mark Davies 为临时 CEO 仅两天后，便回归 Automattic（WordPress.com 母公司）CEO 职位。据 TechCrunch 报道，Mullenweg 将其他管理员移出公司 Slack，并告知员工他已重新掌控公司，而董事会的罢免计划并未顺利推进，相关沟通也混乱且反复无常。 这对 Automattic 以及支撑全球超过 43% 网站的 WordPress 生态而言，是一起重大的公司治理事件。领导层动荡引发了对 WordPress 未来方向、开源治理以及该公司旗下 WooCommerce、Tumblr、Beeper 等广泛使用产品稳定性的质疑。 董事会仅提前 50 分钟通知便将 Mullenweg 停职带薪休假，并拒绝其咨询法律顾问的请求，同时任命 CFO Mark Davies 为临时 CEO。当 TechCrunch 询问 Mullenweg 其回归 CEO 的说法是否属实时，他承诺发布一篇博客文章，但该文章实际内容是关于购买一艘船屋；对于后续追问，他回应称：“我显然不是喷子，我是海盗。”

hackernews · ilamont · 9月13日 20:19 · [社区讨论](https://news.ycombinator.com/item?id=49688259)

**背景**: Matt Mullenweg 是开源发布软件 WordPress 的联合创始人，该软件被全球超过 43% 的网站使用；他于 2005 年创立 Automattic，旗下运营 WordPress.com、WooCommerce、Tumblr、Beeper 等产品。董事会此次行动之前，公司已历经两年多的内部动荡以及与 WordPress 托管公司 WP Engine 的法律纠纷。Automattic 是一家完全分布式公司，在 90 多个国家拥有 1,900 多名员工，没有实体总部。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automattic">Automattic - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Matt_Mullenweg">Matt Mullenweg</a></li>
<li><a href="https://ma.tt/about/">About Matt Mullenweg Matt Mullenweg Returns As Automattic CEO Two Days After Being ... Matt Mullenweg Ousted From Automattic: What Devs Must Know Automattic Board Forces CEO Matt Mullenweg Into Leave of ... Automattic CEO Matt Mullenweg is out: Does this mean long ... Matt Mullenweg | Unlucky in Cards</a></li>

</ul>
</details>

**社区讨论**: 评论者对此事深表担忧，多人表示 Mullenweg 似乎正经历心理健康危机或已脱离现实，并援引其在 Slack 上的异常行为以及对 TechCrunch 的回避性回答。也有人指出，文章并未显示董事会真正撤销了决定，且 Automattic 内部无人就谁在掌权给出明确答复。

**标签**: `#Automattic`, `#WordPress`, `#corporate governance`, `#open source`, `#leadership`

---

<a id="item-4"></a>
## [谷歌持续投放诈骗广告引发众怒](https://www.atomic14.com/2026/09/13/why-is-google-still-serving-dodgy-ads) ⭐️ 8.0/10

atomic14.com 上的一篇文章，连同获得 763 个赞和 344 条评论的 Hacker News 讨论，探讨了为何谷歌在发布商和用户广泛投诉的情况下仍继续投放诈骗和低质量广告。社区成员分享了第一手经历，称其 AdSense 变现网站上出现诈骗弹窗，YouTube 上充斥着 AI 生成的诈骗广告。 这场讨论凸显了数字广告领域日益严重的信任危机，谷歌主导的广告网络被指责将收入置于广告质量和用户安全之上。如果像谷歌这样的平台不能或不愿遏制诈骗广告，发布商、广告主和用户可能会推动更严格的责任追究和监管。 评论者指出，诈骗者不断轮换使用 azurestaticapps.net、herokuapp.com、netlify.app 和 digitaloceanspaces.com 等免费托管域名，而谷歌拒绝屏蔽这些域名，因为将其视为顶级域名。一位在谷歌广告上花费超过 1 亿美元的评论者声称，谷歌正在激进地榨取收入，可能是为了掩盖 AI 领域的失利，并在 AI 颠覆其广告业务之前尽可能获利。

hackernews · iamflimflam1 · 9月13日 17:37 · [社区讨论](https://news.ycombinator.com/item?id=49686445)

**背景**: 谷歌的广告网络在数百万网站和 YouTube 上投放广告，贡献了公司绝大部分收入。广告质量执法通常依赖自动审核和政策检查，但诈骗者通过注册新域名和制作欺骗性创意不断适应。恶意广告（通过广告传播恶意软件）长期以来一直是广告行业的难题，其防范需要行为分析而非静态检查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.google.com/google-ads/answer/18179211?hl=en">Prevent invalid leads - Google Ads Help</a></li>
<li><a href="https://www.humansecurity.com/learn/topics/what-is-malvertising/">What is malvertising ? | Impact & protection against it - HUMAN Security</a></li>
<li><a href="https://www.adexchanger.com/the-sell-sider/virtuous-cycle-ad-quality-enforcement/">adexchanger.com/the-sell-sider/virtuous-cycle- ad - quality - enforcement</a></li>

</ul>
</details>

**社区讨论**: 整体情绪对谷歌高度批评，评论者称该公司是共犯，并要求对诈骗广告追究严格责任。多位用户分享了其网站和 YouTube 上出现诈骗广告的个人经历，其他人则推测谷歌的收入压力和 AI 竞争解释了执法松懈的原因。

**标签**: `#advertising`, `#google`, `#fraud`, `#platform-moderation`, `#tech-ethics`

---

<a id="item-5"></a>
## [Perplexity 采用 GPT-6 Astra 实现自主化生产运维](https://openai.com/index/perplexity-improving-accuracy-with-astra) ⭐️ 8.0/10

Perplexity 正在使用 OpenAI 的 GPT-6 Astra 自主撰写沟通内容、修改软件并监控生产系统，与早期模型相比，其向人类确认的频率大幅降低。这标志着 Astra 首次被大规模应用于端到端生产工程工作流中。 这标志着 AI 融入关键工程工作流的方式发生了范式转变——一家重要 AI 公司信任下一代模型在极少人工监督下修改代码并监控线上系统。这可能加速自主智能体在整个软件行业的采用，同时也引发关于可靠性与责任归属的新问题。 GPT-6 Astra 于 2026 年 9 月 3 日以有限预览形式发布，是 OpenAI 目前能力最强的模型，专为复杂推理、编程、计算机操作、研究和文档创作而设计。Perplexity 对 Astra 的使用建立在其此前的 Perplexity Computer 平台之上，该平台可编排 19 个 AI 模型以自主执行端到端项目。

rss · OpenAI News · 9月14日 00:00

**背景**: GPT-6 Astra 是 OpenAI 的下一代大语言模型，因 2026 年 7 月的 Hugging Face 事件而推迟发布，该事件促使公司增加了更多安全防护措施。Perplexity 是一家 AI 搜索与智能体公司，于 2026 年 2 月推出 Perplexity Computer——一个基于云的平台，可编排多个 AI 模型自主进行研究、编程和部署项目。将 Astra 用于生产监控意味着该模型持续观察线上系统，并在发现异常时采取行动，所需的人工确认比早期模型更少。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra - Wikipedia</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>
<li><a href="https://www.sci-tech-today.com/news/perplexity-computer-19-model-ai-agent/">Perplexity Launches 'Computer': A 19-Model AI System That Researches, Codes, Deploys, and Never Clocks Out</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#OpenAI`, `#software-engineering`, `#production-systems`

---

<a id="item-6"></a>
## [Fable 5.1 破解 370 年前的 Cyphral Distich 密码](https://www.vals.ai/blogs/fable-solves-cyphral-distich) ⭐️ 7.0/10

Vals AI 宣布，Anthropic 的 Claude Fable 5.1 在零人工干预的情况下，仅用 44 分钟、约 17.6 万个 token 就自主破解了 Cyphral Distich——一段印在托马斯·厄克特爵士 1653 年著作《Logopandecteision》末尾的 64 位数字密码。该模型在文本自身中找到了密钥，解开了这个沉寂 370 年的密码。 这一结果凸显了 LLM 能够自动化那些历来制约密码学和学术研究的繁琐搜索、测试与文献追溯工作，从而有望解开大量被忽视的历史谜题。同时，它也加剧了一场更广泛的争论：这类成果究竟体现了真正的通用推理能力，还是仅仅因为大量“低垂的果实”从未有人认真尝试过。 Cyphral Distich 是一段由两行各 32 个数字组成的密码文本，解码所需的密钥并非外部提供，而是隐藏在文本自身之中。整个破解过程耗时约 44 分钟、消耗约 17.6 万个 token，Vals AI 将任务设定为一个开放式目标：寻找一个未解的历史密码并将其破解。

hackernews · u1hcw9nx · 9月13日 21:06 · [社区讨论](https://news.ycombinator.com/item?id=49688695)

**背景**: Cyphral Distich 出现在苏格兰博学家托马斯·厄克特爵士 1653 年出版的《Logopandecteision》一书末尾，他还曾提出过一种通用语言。密码文本（cryptogram）是指经过刻意编码的短消息，不知道生成规则就无法解读，而这段密码数百年来一直未能被破译。Claude Fable 5.1 是 Anthropic 推出的大语言模型，相较 Fable 5 全面升级，在智能体编程、长时间运行的智能体工作流和知识工作方面提升尤为明显。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vals.ai/blogs/fable-solves-cyphral-distich">Claude Fable 5.1 Solves the Cyphral Distich</a></li>
<li><a href="https://en.wikipedia.org/wiki/Logopandecteision">Logopandecteision - Wikipedia</a></li>
<li><a href="https://www.schneier.com/blog/archives/2026/09/claude-fable-solves-a-historical-cipher.html">Claude Fable Solves a Historical Cipher - Schneier on Security</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为这段密码极为冷门、很可能从未被认真研究过，因此这一成果或许更多反映了未被探索的“低垂果实”，而非通用能力的飞跃。有人分享了 LLM 破解个人密码的类似经历，也有人对这类成果究竟预示着 AI 即将带来颠覆，还是仅仅解决了被忽视的简单问题，表达了矛盾心态。

**标签**: `#AI`, `#cryptography`, `#LLM`, `#historical cipher`, `#problem-solving`

---

<a id="item-7"></a>
## [OpenAI 通过 Agents API 公开测试版开放 Codex Harness](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNZE5ZTEp5ZzIzYkpXVjZnLVRnandLRnNHV0t6SnpnUU5Bd2lja0w5bVRwRkNwWnhna0I0TVk4MXhOcTZyV0Fqcmtqb1hoYVJQaExsbzdPeEJJN2RmTE43cnBsUkZBOGM2M0FVSEFCSmJxaEFpeERLVndfU0FYVVZFalRrdGh2WDZDdW9N?oc=5) ⭐️ 7.0/10

OpenAI 于 2026 年 9 月 10 日推出 Agents API 公开测试版，向所有开发者开放托管的 Codex harness。该 API 让应用能够通过单一接口构建并运行长时间运行的云端智能体，支持会话编排、上下文压缩、工具调用和多智能体委派。 这降低了那些已超越单次模型调用、但不愿自行构建和维护智能体运行时的团队的门槛。通过开放与 Codex 和 ChatGPT for Work 相同的底层基础设施，OpenAI 正将自己定位为自主编程与工作流智能体的托管后端，从而加剧与其他智能体框架的竞争。 该托管 harness 提供持久会话、沙箱执行环境、MCP 工具访问、委派子智能体、上下文压缩、故障恢复和流式事件。它由开源 Codex harness 驱动，因此开发者可以查看协调模型调用、工具和上下文的核心逻辑，而由 OpenAI 负责运营和维护。

google_news · The Eastern Herald · 9月13日 09:03

**背景**: 智能体 harness 是负责管理 AI 模型如何调用工具、跨步骤保持上下文以及在长任务中从故障恢复的编排层。此前，构建此类智能体的开发者必须使用 Agents SDK 等框架自行组装这些组件。Agents API 将该运行时打包为托管云服务，类似于云平台对服务器管理的抽象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-the-agents-api/">Introducing the Agents API - OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/agents-api/overview">Agents API | OpenAI API - developers.openai.com</a></li>
<li><a href="https://theroboticsmedia.com/article/openai-agents-api-public-beta-codex-harness-september-10-2026">OpenAI Agents API Ships In Public Beta With Codex Harness</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Codex`, `#Agents API`, `#AI coding agents`, `#developer tools`

---