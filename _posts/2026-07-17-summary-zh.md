---
layout: default
title: "Horizon Summary: 2026-07-17 (ZH)"
date: 2026-07-17
lang: zh
---

> 从 42 条内容中筛选出 14 条重要资讯。

---

1. [Firefox 被编译为 WebAssembly 在另一浏览器中运行](#item-1) ⭐️ 9.0/10
2. [Kimi K3 2.8T-A50B：最大开源模型，Opus 4.8 级别性能，Sonnet 5 价格](#item-2) ⭐️ 9.0/10
3. [Roc 编译器从 Rust 重写为 Zig](#item-3) ⭐️ 8.0/10
4. [交互式线性代数书籍获好评](#item-4) ⭐️ 8.0/10
5. [Thinking Machines Lab 发布 975B 开放权重模型 Inkling](#item-5) ⭐️ 8.0/10
6. [Linus Torvalds 宣布 Linux 不反 AI](#item-6) ⭐️ 8.0/10
7. [Lila Sciences：将实验室视为 AI 训练的数据中心](#item-7) ⭐️ 8.0/10
8. [NVIDIA Nemotron-3 Embed 登顶 RTEB 排行榜](#item-8) ⭐️ 8.0/10
9. [新型数据注入攻击瞄准 AI 代理](#item-9) ⭐️ 8.0/10
10. [微软 Comic Chat 开源，时隔 30 年](#item-10) ⭐️ 7.0/10
11. [Decoy 字体：双层文字欺骗 AI](#item-11) ⭐️ 7.0/10
12. [LM Studio 推出 Bionic，面向开放模型的 AI 智能体](#item-12) ⭐️ 7.0/10
13. [GPT-5.6 Codex 漏洞可在完全访问模式下删除文件](#item-13) ⭐️ 7.0/10
14. [新 AI 模型保持性能优势](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Firefox 被编译为 WebAssembly 在另一浏览器中运行](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter Labs 将 Gecko 引擎（Firefox）编译为 WebAssembly，使得完整的 Firefox 浏览器可以在另一个浏览器中运行。该项目使用了估计价值 25,000 美元的 AI 代币（Claude Opus 和 Fable），但由于订阅计划实际花费远低于此。 这是一项突破性的技术成就，拓展了 WebAssembly 的能力边界，可能为浏览器内虚拟化和遗留软件访问带来新的应用场景。同时也展示了 AI 辅助开发在复杂移植项目中的强大能力。 该演示通过 WebSocket 使用 Wisp 协议将所有网络流量代理到 Puter 的服务器，因为浏览器中的 WebAssembly 无法打开任意网络连接。该项目支持端到端加密，观察到 HTTPS 流量已加密，而 HTTP 流量为明文。

rss · Simon Willison · 7月16日 23:34

**背景**: WebAssembly (WASM) 是一种低级二进制指令格式，可在现代浏览器中以接近原生的速度运行。将像 Gecko 这样的完整浏览器引擎编译为 WASM 因其规模和复杂性而极具挑战性。Wisp 协议是一种低开销协议，用于通过单个 WebSocket 连接代理多个 TCP/UDP 套接字。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/HeyPuter/firefox-wasm">GitHub - HeyPuter/firefox-wasm: 🦊 Firefox in WebAssembly</a></li>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low-overhead, easy to implement protocol for proxying multiple TCP/UDP sockets over a single websocket. · GitHub</a></li>
<li><a href="https://www.drweb.de/firefox-webassembly-gecko-engine-browser/">Firefox als WebAssembly: Browser im Browser-Tab?</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论非常积极，许多人对这一技术壮举印象深刻。一些人提出了代理流量的成本问题，团队通过扩展服务器解决了这一问题。AI 辅助开发的方面也引起了关注。

**标签**: `#WebAssembly`, `#Firefox`, `#Browser Engineering`, `#AI-assisted Development`, `#WebSocket`

---

<a id="item-2"></a>
## [Kimi K3 2.8T-A50B：最大开源模型，Opus 4.8 级别性能，Sonnet 5 价格](https://www.latent.space/p/ainews-kimi-k3-28t-a50b-the-largest) ⭐️ 9.0/10

Moonshot AI 发布了 Kimi K3，一个拥有 2.8 万亿参数、500 亿激活参数的混合专家模型，声称性能与 Claude Opus 4.8 相当，而定价与 Claude Sonnet 5 类似。 作为有史以来最大的开源模型，Kimi K3 使前沿级 AI 能力民主化，可能加速开源 AI 发展，并以有竞争力的定价挑战专有模型。 Kimi K3 拥有 100 万 token 的上下文窗口、原生多模态输入，并采用了包括 Kimi Delta Attention (KDA) 和 Attention Residuals 在内的新型注意力机制。定价为每百万输入 token 3 美元，每百万输出 token 15 美元，缓存输入为 0.3 美元。

rss · Latent Space · 7月17日 01:46

**背景**: 大型语言模型通常以参数数量和 MoE 架构中的激活参数来衡量。开源模型公开发布权重，使社区能够使用和微调。Opus 4.8 和 Sonnet 5 是 Anthropic 的前沿模型；以 Sonnet 5 的价格达到 Opus 4.8 的性能代表了重大的性价比突破。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.latent.space/p/ainews-kimi-k3-28t-a50b-the-largest">[AINews] Kimi K3 2.8T-A50B: the largest open model ever released; Opus 4.8-class at Sonnet 5 pricing</a></li>
<li><a href="https://tosea.ai/blog/kimi-k3-complete-guide">How to Use Kimi K3: Complete Guide to Moonshot AI's 2.8T-Parameter Flagship Model | Tosea.ai</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，该模型作为中国开源模型定价较高，但如果确实能与前沿模型竞争，则定价合理。一些人认为中国实验室正在将智能商品化，而另一些人则质疑如此大规模训练投资的回报。

**标签**: `#AI`, `#open-source`, `#large language model`, `#Kimi K3`, `#breakthrough`

---

<a id="item-3"></a>
## [Roc 编译器从 Rust 重写为 Zig](https://rtfeldman.com/rust-to-zig) ⭐️ 8.0/10

Roc 编译器团队正在将其编译器从 Rust 重写为 Zig，理由是 Zig 的增量编译速度、交叉编译支持以及更适合二进制修补和代码重载等底层编译器任务。 这次重写凸显了系统编程中内存安全与底层控制之间的权衡，并可能影响更广泛语言生态中的编译器设计选择。 Zig 的 ReleaseSafe 模式通过运行时检查捕获 use-after-free 错误，但社区成员质疑它是否真正防止所有 use-after-free 漏洞。Roc 编译器之前使用 OCaml 进行原型设计，然后转向 Rust，现在又转向 Zig。

hackernews · jorangreef · 7月16日 11:39 · [社区讨论](https://news.ycombinator.com/item?id=48933149)

**背景**: Roc 是一种快速、友好的函数式编程语言。其编译器正从 Rust 重写为 Zig，以利用 Zig 的增量编译和交叉编译特性，这些特性对开发者生产力至关重要。Zig 是一种系统编程语言，优先考虑手动内存管理和编译时执行，提供类似 C 的底层控制但具有现代特性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.roc-lang.org/">The Roc Programming Language</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language) - Wikipedia</a></li>
<li><a href="https://ziglang.org/learn/overview/">Overview ⚡ Zig Programming Language</a></li>

</ul>
</details>

**社区讨论**: 社区评论讨论编译器是否真的需要不安全代码来生成机器码，Steve Klabnik 认为只有热修补需要不安全，常规编译不需要。其他人质疑 Zig 的 use-after-free 检测声明，并指出 Rust 的安全特性对编译器正确性很有价值。

**标签**: `#Rust`, `#Zig`, `#compilers`, `#memory safety`, `#programming languages`

---

<a id="item-4"></a>
## [交互式线性代数书籍获好评](https://immersivemath.com/ila/) ⭐️ 8.0/10

一本 2015 年出版的沉浸式线性代数书，包含交互式图形，因其通过可视化进行教学的创新方法而重新被在线社区发现并高度赞扬。 这本书展示了交互式可视化如何显著增强对抽象数学概念的理解，有可能彻底改变数学教育，并激发其他学科的类似资源。 该书具有交互式图形，允许读者实时操作和探索概念，并包含工具提示以提供额外上下文。它可在 immersivemath.com 上免费在线获取。

hackernews · srean · 7月16日 15:32 · [社区讨论](https://news.ycombinator.com/item?id=48935951)

**背景**: 线性代数是数学的基础分支，用于计算机科学、物理学和工程学等领域。传统教科书依赖静态图表，这使得向量空间和变换等抽象概念难以理解。交互式图形通过让学习者直接查看和操作概念来弥合这一差距。

**社区讨论**: 评论者表达了强烈的热情，许多人希望统计学和机器人学等其他学科也有类似的交互式资源。一些人指出，像 LLM 这样的现代 AI 工具可以使创建此类交互式内容更容易、更快，从而可能带来新一代教育材料。

**标签**: `#linear algebra`, `#interactive learning`, `#education`, `#visualization`, `#mathematics`

---

<a id="item-5"></a>
## [Thinking Machines Lab 发布 975B 开放权重模型 Inkling](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 8.0/10

由前 OpenAI CTO Mira Murati 创立的 Thinking Machines Lab 发布了 Inkling，这是一个采用 Apache-2.0 许可的开放权重 975B 参数混合专家多模态模型，具有 41B 活跃参数和 1M token 上下文窗口。 Inkling 是目前美国最大的开放权重模型，为微调和定制提供了强大基础，并增强了美国开放权重生态系统以对抗来自中国的竞争模型。 模型卡片明显简略，训练数据文档极少，实验室承认 Inkling 不是前沿模型，而是通过其 Tinker 平台进行微调的强大基础模型。一个更小的 276B（12B 活跃参数）变体 Inkling-Small 已承诺但尚未发布。

rss · Simon Willison · 7月16日 15:35

**背景**: 混合专家（MoE）模型每个 token 仅激活部分参数，从而在高效推理的同时实现较大的总参数量。开放权重模型允许开发者自由微调和部署，促进 AI 生态系统的创新和竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our open-weights model - Thinking Machines Lab</a></li>
<li><a href="https://www.marktechpost.com/2026/07/15/thinking-machines-lab-releases-inkling-a-975b-parameter-open-weights-multimodal-moe-with-41b-active-parameters-and-controllable-thinking-effort/">Thinking Machines Lab Releases Inkling: A 975B-Parameter Open-Weights Multimodal MoE With 41B Active Parameters And Controllable Thinking Effort - MarkTechPost</a></li>
<li><a href="https://sebastianraschka.com/blog/2026/inkling-architecture-benchmark-notes.html">Inkling: A New Open-Weight 975B MoE with a Few Surprises</a></li>

</ul>
</details>

**社区讨论**: 社区讨论指出模型卡片和训练数据文档过于简略令人担忧，但总体情绪积极，因为模型规模大、许可开放且实验室声誉良好。一些人指出 Inkling 不是前沿模型，而是实用的定制基础模型。

**标签**: `#AI`, `#open-weights`, `#multimodal`, `#mixture-of-experts`, `#Mira Murati`

---

<a id="item-6"></a>
## [Linus Torvalds 宣布 Linux 不反 AI](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linux 创始人 Linus Torvalds 在 Linux Media 邮件列表中声明，Linux 不是一个反 AI 的项目，AI 是一个明确有用的工具，并告诉反对者他们可以分叉项目或离开。 来自顶级维护者的强烈支持标志着 Linux 内核的明确政策方向，可能影响更广泛的开源社区对 AI 集成的立场。 Torvalds 强调 AI 的有用性已不再存疑，尽管其经济影响等其他问题仍然存在。他是在回应社区对内核开发中使用 AI 工具的反对时发表此声明的。

rss · Simon Willison · 7月16日 13:26

**背景**: Linux 内核是最大的开源项目之一，Linus Torvalds 是其创始人和顶级维护者。近期，一些开源项目采取了反 AI 政策，限制 AI 生成的代码或工具。Torvalds 的声明明确了 Linux 的立场，将 AI 视为合法的开发工具。

**标签**: `#Linux`, `#AI`, `#Open Source`, `#Kernel Development`

---

<a id="item-7"></a>
## [Lila Sciences：将实验室视为 AI 训练的数据中心](https://www.latent.space/p/the-lab-of-the-future-should-feel) ⭐️ 8.0/10

Lila Sciences 提议将科学实验室转变为数据中心，为 AI 生成训练数据，其特色是充满机器人的实验室可自主进行实验。 这一范式转变可能为 AI 训练解锁大量未开发的科学数据，加速生命科学、化学和材料科学领域的发现。 该方法涉及使用自主实验室，以超人速度生成假设、设计实验并迭代，将实验室本身视为数据生成基础设施。

rss · Latent Space · 7月16日 13:30

**背景**: 当前 AI 训练严重依赖互联网数据，而互联网数据是有限的。科学实验能产生丰富、结构化的数据，可用于训练模型进行推理和发现。Lila Sciences 由 Flagship Pioneering 支持，旨在构建首个科学超级智能平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lila.ai/">LILA | Scientific Superintelligence</a></li>
<li><a href="https://www.flagshippioneering.com/companies/lila-sciences">Lila Sciences | Flagship Pioneering</a></li>

</ul>
</details>

**标签**: `#AI`, `#scientific research`, `#automation`, `#data infrastructure`, `#lab of the future`

---

<a id="item-8"></a>
## [NVIDIA Nemotron-3 Embed 登顶 RTEB 排行榜](https://huggingface.co/blog/nvidia/nemotron-3-embed-wins-rteb) ⭐️ 8.0/10

NVIDIA 的 Nemotron-3 Embed 模型在 RTEB（检索文本嵌入基准）排行榜上获得总体第一名，标志着 AI 系统在智能体检索方面的突破。 这一成就推动了智能体检索领域的发展，AI 系统可动态检索和推理信息，影响 RAG 和企业 AI 等应用。它为多语言和多模态场景下的嵌入模型树立了新标准。 基于 Ministral-3-8B 的 Nemotron-3 Embed-8B 模型将文本映射为 4096 维稠密向量，在多语言检索基准上达到最先进性能。RTEB 排行榜于 2025 年 10 月推出，是 MTEB 排行榜新检索部分的一部分。

rss · Hugging Face Blog · 7月16日 16:01

**背景**: 嵌入模型将文本转换为数值向量用于相似性搜索，对检索增强生成（RAG）和语义搜索至关重要。智能体检索扩展了这一点，使 AI 智能体能够自主决定何时以及如何检索信息，提高准确性和适应性。RTEB 基准在多种检索任务上评估模型，提供标准化比较。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepinfra.com/nvidia/Nemotron-3-Embed-8B">nvidia/ Nemotron - 3 - Embed -8B - Demo - DeepInfra</a></li>
<li><a href="https://huggingface.co/blog/rteb">Introducing RTEB: A New Standard for Retrieval Evaluation</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#embeddings`, `#retrieval`, `#AI`, `#benchmark`

---

<a id="item-9"></a>
## [新型数据注入攻击瞄准 AI 代理](https://news.google.com/rss/articles/CBMif0FVX3lxTE1vRm5uMi1lajhJWmhfN3NtaEM1M01mNG1BNjZYeERRQ1dwclZNUUk2RnlrY050QXpzOXhzUkYxdjZqenBOOG9naS1qSnJlbWpMbFVKWWZKSnZONFZlWERzUUg0S1NaNVJMS0prb1U1MnUxQVlGbDNWRlpFM1pta2M?oc=5) ⭐️ 8.0/10

研究人员发现了一种名为“代理数据注入”（ADI）的新型攻击，能够操纵 AI 代理误点击或执行攻击者命令，并绕过现有的提示注入防御。 这种攻击对用于网页浏览、编码等自主任务的 AI 代理构成重大安全威胁，因为它利用了 LLM 解释结构化数据的方式，而非依赖提示操纵。 该攻击通过向 AI 代理处理的数据字段注入恶意内容，导致 LLM 误解边界并执行伪造指令。已在六个真实 AI 模型上得到验证。

google_news · The Hacker News · 7月16日 11:32

**背景**: AI 代理是使用大型语言模型（LLM）自主执行任务（如点击按钮或运行命令）的软件程序。传统的提示注入攻击操纵文本输入，而 ADI 攻击则利用代理处理的结构化数据（如电子邮件、JSON），使其更难防御。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/07/new-agent-data-injection-attack-can.html">New Agent Data Injection Attack Can Make AI Agents Misclick or Run Attacker Commands</a></li>
<li><a href="https://arxiv.org/abs/2607.05120">[2607.05120] Agent Data Injection Attacks are Realistic Threats to AI Agents</a></li>

</ul>
</details>

**标签**: `#AI security`, `#adversarial attack`, `#data injection`, `#cybersecurity`

---

<a id="item-10"></a>
## [微软 Comic Chat 开源，时隔 30 年](https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/) ⭐️ 7.0/10

2026 年 7 月 16 日，微软将 1990 年代的图形化 IRC 客户端 Comic Chat（后更名为 Microsoft Chat）开源，该软件能将文本对话转化为漫画形式。源代码现已在 GitHub 上以 MIT 许可证发布。 此次发布保留了一段独特的互联网历史，允许开发者研究、修改并在现代系统上运行该软件。这也凸显了微软对开源日益增长的承诺，尤其是对于具有文化意义的怀旧项目。 Comic Chat 最初由微软研究员 David Kurlander 开发，于 1996 年随 Internet Explorer 3.0 首次发布。它被捆绑在 Windows 98 中，本地化为 24 种语言，并且还向世界介绍了 Comic Sans 字体。

hackernews · jervant · 7月16日 16:06 · [社区讨论](https://news.ycombinator.com/item?id=48936426)

**背景**: IRC（互联网中继聊天）是 1990 年代和 2000 年代初流行的基于文本的聊天协议，用于群组通信。Comic Chat 是一个图形化 IRC 客户端，能自动将对话渲染为漫画面板，并带有可自定义的头像，使聊天更加有趣和易用。此次开源由 Robert Standefer 推动，并得到 Scott Hanselman 的支持，经过六年的努力才实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Microsoft_Comic_Chat">Microsoft Comic Chat</a></li>
<li><a href="https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/">Microsoft Comic Chat is now open source</a></li>
<li><a href="https://en.wikipedia.org/wiki/IRC_client">IRC client</a></li>

</ul>
</details>

**社区讨论**: 社区反应极为积极，许多人表达了对微软此举的怀旧和赞赏。一些评论者指出，Comic Chat 在当时因其非标准的 IRC 协议扩展而备受争议，但总体情绪是兴奋和对代码库的好奇。

**标签**: `#open source`, `#microsoft`, `#irc`, `#nostalgia`, `#comic chat`

---

<a id="item-11"></a>
## [Decoy 字体：双层文字欺骗 AI](https://www.mixfont.com/experiments/decoy-font) ⭐️ 7.0/10

一种名为 Decoy 字体的新字体利用双层排版技术，在可见文字中嵌入隐藏信息，使 AI 模型更难读取真实内容，同时人类仍可阅读。 这项技术展示了一种对抗性方法，用于保护文本不被 AI 读取，可能影响隐私、内容审核和 AI 训练数据收集等领域。 该字体利用空间频率：精细轮廓显示诱饵字母，而模糊或低分辨率渲染则显示真实信息。社区测试结果不一，部分 AI 模型仅在提示下才能检测到隐藏文本。

hackernews · ray__ · 7月16日 16:18 · [社区讨论](https://news.ycombinator.com/item?id=48936584)

**背景**: 对抗性排版是一种通过操纵文本来混淆机器学习模型的技术。Decoy 字体在此基础上，利用 AI 视觉系统与人类视觉处理空间频率的差异，在同一空间中嵌入两条信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mixfont.com/experiments/decoy-font">Decoy Font: A TTF font that hides what you type</a></li>
<li><a href="https://typedrawers.com/discussion/5640/i-made-an-anti-ai-typeface-where-every-letter-contains-a-decoy-letter">I made an anti-AI typeface where every letter contains a decoy letter — TypeDrawers</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有人认为很酷但质疑其实用性，也有人报告称 GPT-4o 等 AI 模型在提示下能解码隐藏信息。一位用户指出，将图像缩小到较低分辨率会导致 AI 转而读取隐藏文本。

**标签**: `#AI`, `#typography`, `#security`, `#adversarial`, `#HackerNews`

---

<a id="item-12"></a>
## [LM Studio 推出 Bionic，面向开放模型的 AI 智能体](https://lmstudio.ai/blog/introducing-lm-studio-bionic) ⭐️ 7.0/10

Bionic 以隐私优先的方式为开放模型带来智能体能力，允许用户在本地运行 AI 智能体而无需数据离开其控制，这可能加速本地 AI 智能体在敏感任务中的采用。 Bionic 支持两种项目类型：用于编码的“Code”项目和用于文档创建/处理并带有自动检查点的“Work”项目。它可以使用本地模型或切换到云端开放模型，LM Studio 承诺零数据保留政策。

hackernews · minimaxir · 7月16日 20:18 · [社区讨论](https://news.ycombinator.com/item?id=48939662)

**背景**: 智能体框架是使大型语言模型能够作为 AI 智能体运行的软件基础设施，它管理工具使用、记忆和状态持久化。没有框架，LLM 是无状态的，只能生成文本；框架允许多步骤、面向工具的任务。LM Studio 是一款流行的桌面应用，用于在本地运行开放模型，而 Bionic 将其扩展到智能体领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lmstudio.ai/blog/introducing-lm-studio-bionic">Introducing LM Studio Bionic: the AI agent for open models | LM Studio Blog | LM Studio</a></li>
<li><a href="https://9to5mac.com/2026/07/16/lm-studio-expands-beyond-chat-with-bionic-a-new-ai-agent-app-for-open-models/">LM Studio launches Bionic, a new AI agent app for open models - 9to5Mac</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示出积极的兴趣和建设性反馈。用户称赞 Bionic 易于使用且与 Codex 相似，但提出了系统级访问、本地网络搜索、SSH 支持和模型加载进度条等功能请求。创始人提供了针对特定模型的免费测试积分。

**标签**: `#AI agents`, `#open models`, `#local LLM`, `#LM Studio`, `#agentic harness`

---

<a id="item-13"></a>
## [GPT-5.6 Codex 漏洞可在完全访问模式下删除文件](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 7.0/10

Thibault Sottiaux 报告称，当启用完全访问模式且未使用沙箱保护时，GPT-5.6 Codex 可能因错误覆盖 $HOME 环境变量而意外删除文件。 此漏洞凸显了具有完全系统访问权限的 AI 编码代理的关键安全风险，可能导致依赖 Codex 进行自动化任务的开发者和企业遭受不可逆的数据丢失。 该漏洞发生在 Codex 尝试通过覆盖 $HOME 来设置临时目录时，却错误地删除了 $HOME。触发条件包括启用完全访问模式、无沙箱保护以及关闭自动审查。

rss · Simon Willison · 7月16日 17:45

**背景**: Codex 是一种 AI 编码代理，可以在用户系统上执行命令。完全访问模式赋予其无限制权限，而沙箱则将其与主机隔离。$HOME 环境变量指向用户的主目录，覆盖它是临时工作区的常见做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explainx.ai/blog/openai-codex-gpt-5-6-home-deletion-full-access-july-2026">Codex GPT - 5 . 6 $HOME Deletion — Full Access | explainx.ai</a></li>
<li><a href="https://www.firecrawl.dev/blog/ai-agent-sandbox">AI Agent Sandbox: How to Safely Run Autonomous Agents in 2026</a></li>

</ul>
</details>

**标签**: `#codex`, `#coding-agents`, `#generative-ai`, `#ai-safety`, `#bug`

---

<a id="item-14"></a>
## [新 AI 模型保持性能优势](https://huggingface.co/blog/Dharma-AI/newer-models-same-advantages) ⭐️ 7.0/10

Hugging Face 上的一篇博客文章指出，新 AI 模型持续超越旧模型，在性能和能力上保持代际优势。 这一见解帮助从业者决定何时升级模型，并验证了 AI 的快速进步，影响生产系统中的模型选择。 该文章可能比较了不同模型版本的准确性、推理速度和任务泛化等指标，但摘要中未提供具体数字。

rss · Hugging Face Blog · 7月16日 11:49

**背景**: AI 模型经常通过新架构和训练技术进行更新，带来渐进式改进。理解持续优势的趋势有助于开发者有效分配资源。

**标签**: `#AI/ML`, `#model comparison`, `#Hugging Face`, `#deep learning`

---