---
layout: default
title: "Horizon Summary: 2026-07-27 (ZH)"
date: 2026-07-27
lang: zh
---

> 从 29 条内容中筛选出 9 条重要资讯。

---

1. [vLLM v0.26.0：新增 Inkling 模型系列、DeepSeek-V4 性能优化等](#item-1) ⭐️ 8.0/10
2. [LLM 大幅降低形式化验证成本](#item-2) ⭐️ 8.0/10
3. [美国公民因 GrapheneOS 手机在机场搜查中被擦除而遭指控](#item-3) ⭐️ 8.0/10
4. [中继市场助长 AI 云服务代币转售与欺诈](#item-4) ⭐️ 8.0/10
5. [欧盟提议浏览器级隐私设置以消灭 Cookie 横幅](#item-5) ⭐️ 8.0/10
6. [OpenAI Agents Python SDK v0.19.0 新增程序化工具调用](#item-6) ⭐️ 7.0/10
7. [PGSimCity 交互式可视化 PostgreSQL 内部机制](#item-7) ⭐️ 7.0/10
8. [英伟达物理 AI 收入达 100 亿美元，目标 1000 亿](#item-8) ⭐️ 7.0/10
9. [OpenAI 敦促白宫加快前沿 AI 模型审查](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0：新增 Inkling 模型系列、DeepSeek-V4 性能优化等](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 新增对 Inkling 模型系列的支持，对 DeepSeek-V4 进行了显著的性能优化，通过 head_dtype 支持 fp32 lm_head，并引入了可针对每个 KV-cache 组选择的灵活注意力后端。 此次发布增强了 vLLM 的通用性和性能，通过支持更多模型架构并提升推理效率，使在生产环境中部署大语言模型的用户受益。 该版本包含来自 212 位贡献者的 411 次提交，值得注意的新增功能包括 Inkling 的分段 CUDA 图支持、DeepSeek-V4 的专用路由内核，以及用于分层存储的 KV 卸载指标。

github · khluu · 7月27日 01:06

**背景**: vLLM 是一个开源的高吞吐量 LLM 推理引擎，用于优化大语言模型服务中的内存和计算。Inkling 模型系列是 Thinking Machines Lab 推出的通用多模态模型，支持文本、图像和音频输入。DeepSeek-V4 是一个大语言模型，通过自定义内核获得了性能提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/thinkingmachines/Inkling">thinkingmachines/ Inkling · Hugging Face</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling : Our Open-Weights Model - Thinking Machines Lab</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#model optimization`, `#GPU kernels`, `#open source`

---

<a id="item-2"></a>
## [LLM 大幅降低形式化验证成本](https://www.imperialviolet.org/2026/07/26/zstd-lean.html) ⭐️ 8.0/10

一篇博客文章指出，大型语言模型（LLM）已使形式化验证的成本大幅降低，从大约软件开发成本的 20 倍降至接近零，可能彻底改变软件可靠性。 这一转变可能使形式化验证对主流软件开发变得实用，大幅减少错误和安全漏洞。它还可能改变漏洞利用的经济性，因为验证比寻找漏洞更便宜。 文章特别提到使用 LLM 与 Lean 定理证明器以及针对 Rust 的 Verus 等工具。社区评论指出，编写形式化规范可能成为程序员的关键技能，且 LLM 生成的证明现在可以以以前成本的一小部分完成。

hackernews · zdw · 7月26日 20:53 · [社区讨论](https://news.ycombinator.com/item?id=49062291)

**背景**: 形式化验证使用数学证明来保证软件正确性，但历史上极其昂贵（通常是开发成本的 20 倍）。LLM 现在可以自动生成证明，大幅减少所需的人力。Lean 和 Verus 等工具将定理证明集成到编程语言中，使验证更加易于使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2505.15740">[2505.15740] HybridProver: Augmenting Theorem Proving with ...</a></li>

</ul>
</details>

**社区讨论**: 评论者大多同意这一论点，有些人分享了个人项目，如用于基准测试 ATP 系统的 OpenATP。一位评论者指出加密领域对基于 LLM 的验证实际成本存在困惑，引用了一条推文称对以太坊虚拟机进行 Lean 形式化需要 15 万美元的 API 代币。

**标签**: `#formal verification`, `#LLM`, `#software reliability`, `#theorem proving`, `#Lean`

---

<a id="item-3"></a>
## [美国公民因 GrapheneOS 手机在机场搜查中被擦除而遭指控](https://www.techspot.com/news/113236-us-prosecutors-charge-atlanta-man-after-grapheneos-phone.html) ⭐️ 8.0/10

一名美国公民在亚特兰大机场边境搜查中，因输入胁迫 PIN 码导致其 GrapheneOS 手机自动擦除数据而被起诉。这一事件引发了关于使用旨在胁迫下保护数据的安全功能的法律后果的讨论。 此案凸显了数字隐私权与政府边境搜查权之间的紧张关系，可能为法院如何处理胁迫 PIN 码和加密功能的使用开创先例。它影响到所有使用强隐私工具的旅行者，并引发了关于在合法搜查期间擦除设备合法性的问题。 GrapheneOS 中的胁迫 PIN 码功能在输入时会触发静默恢复出厂设置，而标准 PIN 码则解锁手机。据报道，当执法人员要求解锁设备时，用户输入了胁迫 PIN 码而非解锁，导致数据擦除并随后被起诉。

hackernews · eecc · 7月26日 22:21 · [社区讨论](https://news.ycombinator.com/item?id=49063022)

**背景**: GrapheneOS 是一个注重安全的基于 Android 的操作系统，提供高级隐私功能，包括胁迫 PIN 码——在胁迫下输入时会擦除设备。美国边境执法人员拥有广泛的权力搜查电子设备，在搜查期间故意销毁证据可能导致妨碍司法指控。此案仍在审理中，引发了关于安全工具与刑法交叉的复杂法律问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.androidauthority.com/grapheneos-duress-pin-us-prosecution-3691271/">GrapheneOS duress PIN could land a man in prison - Android Authority</a></li>
<li><a href="https://www.androidauthority.com/grapheneos-duress-pin-3584795/">I use a duress PIN to protect my data — here’s how it works</a></li>
<li><a href="https://privacygear.nl/en/guides/grapheneos-duress-pin-guide/">GrapheneOS duress PIN : wipe your phone under... — PrivacyGear.nl</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了使用胁迫 PIN 码是合法的安全实践还是非法的妨碍行为。一些人认为用户在选择此类功能时必须承担法律后果，而另一些人则建议像 VeraCrypt 的隐藏卷这样的诱饵操作系统可能是更好的替代方案。还有技术澄清指出，GrapheneOS 的胁迫 PIN 码不会覆盖数据，而是执行恢复出厂设置，这可能无法完全阻止法医恢复。

**标签**: `#GrapheneOS`, `#digital rights`, `#border security`, `#encryption`, `#legal`

---

<a id="item-4"></a>
## [中继市场助长 AI 云服务代币转售与欺诈](https://vectoral.com/blog/token-relay-market) ⭐️ 8.0/10

一项调查揭露了一个地下中继市场，代币转售商通过汇集 API 密钥并使用代理服务，以折扣价出售 AI 和云服务，利用计费系统和免费信用额度。 该市场助长了欺诈行为，并为转售商提供了不公平的竞争优势，破坏了合法提供商的定价模式，并可能损害依赖免费信用额度的初创企业。 转售商使用开源工具构建代理服务，通过汇集 API 密钥（通常通过盗用账户或滥用免费信用额度获得）路由请求，以官方价格的一小部分出售代币。

hackernews · mlenhard · 7月26日 15:17 · [社区讨论](https://news.ycombinator.com/item?id=49058993)

**背景**: AWS 和 Azure 等 AI 和云提供商提供免费信用额度以吸引新客户。然而，欺诈者通过创建多个账户、使用被盗支付方式或滥用计费系统来积累信用额度，然后在中继市场以折扣价转售。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://devblogs.co/posts/an-inside-look-at-the-relay-market-powering-token-resellers-and-fraud">An Inside Look at the Relay Market Powering Token Resellers and...</a></li>
<li><a href="https://cctest.ai/en/articles/inside-the-ai-token-relay-market-cheap-inference-account-pools-and-fraud">AI Token Relay Market : Cheap APIs and Fraud Risks - CCTest</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，类似的转售市场在上一代互联网巨头的产品中就已存在，免费信用额度滥用是关键推动因素。一些人强调了在订阅模式中防止代币欺诈的挑战，而另一些人则指出正在开发像 WorkOS Radar 这样的解决方案来应对这一问题。

**标签**: `#AI`, `#cloud computing`, `#fraud`, `#market abuse`, `#security`

---

<a id="item-5"></a>
## [欧盟提议浏览器级隐私设置以消灭 Cookie 横幅](https://killthecookiebanner.eu/) ⭐️ 8.0/10

欧盟委员会提出一项法规，允许用户在浏览器中一次性设置隐私偏好，从而消除每个网站上的 Cookie 横幅。 这可能终结广受诟病的 Cookie 横幅体验，改善用户体验和可访问性，并在执行得当的情况下减少追踪。 该提案将 Cookie 规则纳入 GDPR 框架，为网站提供更多法律依据，但遭到德国、法国等欧盟成员国以及谷歌的反对。

hackernews · rapnie · 7月26日 11:53 · [社区讨论](https://news.ycombinator.com/item?id=49057175)

**背景**: Cookie 横幅是根据欧盟电子隐私指令要求弹出的窗口，用于获取用户对追踪 Cookie 的同意。它们因烦人、误导且往往无法提供真正的知情同意而受到批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://noyb.eu/en/eu-member-states-and-google-suddenly-want-keep-cookie-banners">EU Member States (and Google) suddenly want to keep cookie banners!</a></li>
<li><a href="https://thecapitolforum.com/eu-cookie-banner-cleanup-plan-faces-conflicting-pushback-echoing-tensions-that-tanked-past-efforts/">EU Cookie Banner Cleanup Plan Faces Conflicting Pushback, Echoing Tensions That Tanked Past Efforts - The Capitol Forum</a></li>

</ul>
</details>

**社区讨论**: 评论者大多支持该提案，指出其烦人、缺乏知情同意以及可访问性问题。一些人认为应完全禁止横幅，而另一些人则强调需要严格执行并对违规行为处以罚款。

**标签**: `#privacy`, `#regulation`, `#web standards`, `#user experience`, `#accessibility`

---

<a id="item-6"></a>
## [OpenAI Agents Python SDK v0.19.0 新增程序化工具调用](https://github.com/openai/openai-agents-python/releases/tag/v0.19.0) ⭐️ 7.0/10

OpenAI 发布了 openai-agents-python SDK 的 v0.19.0 版本，引入了通过新的 `ProgrammaticToolCallingTool` 类实现的程序化工具调用功能，允许支持的模型生成 JavaScript 来协调工具。该版本还新增了公共的 `agents.decorators` 模块及 `@tool` 别名，并通过同时接受类型化对象和字典来提升配置灵活性。 该功能使 AI 智能体能够编写并执行 JavaScript 以实现复杂的工具编排，包括并行调用、循环和条件判断，显著扩展了智能体工作流的能力。SDK 的改进也让开发者更容易构建和配置多智能体系统，可能加速 AI 智能体在生产环境中的采用。 程序化工具调用仅受某些 OpenAI Responses 模型支持，并需要托管的 JavaScript 运行时；它支持每个工具的 `allowed_callers`、结构化函数工具输出，并与流式传输、护栏和审批集成。该版本还强化了日志记录以避免暴露敏感负载，并提升了与 AnyLLM 和 LiteLLM 提供商的兼容性。

github · seratch · 7月27日 04:10

**背景**: OpenAI Agents SDK 是一个轻量级框架，用于构建多智能体工作流，支持 OpenAI 的 Responses 和 Chat Completions API 以及超过 100 种其他大语言模型。工具调用（函数调用）允许模型与外部系统交互，而程序化工具调用则通过让模型编写 JavaScript 程序来协调单个请求中的多个工具调用，从而实现更动态、更高效的智能体行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling">Programmatic Tool Calling | OpenAI API</a></li>
<li><a href="https://openai.github.io/openai-agents-python/">OpenAI Agents SDK</a></li>
<li><a href="https://github.com/openai/openai-agents-python">GitHub - openai / openai - agents - python : A lightweight, powerful...</a></li>

</ul>
</details>

**标签**: `#openai`, `#agents-sdk`, `#tool-calling`, `#python`, `#ai-agents`

---

<a id="item-7"></a>
## [PGSimCity 交互式可视化 PostgreSQL 内部机制](https://nikolays.github.io/PGSimCity/) ⭐️ 7.0/10

PGSimCity 是一个交互式可视化工具，通过动画展示 PostgreSQL 的内部架构，包括进程管理、内存分配和查询执行流程。它实时、动态地演示数据库在底层是如何运作的。 该工具让开发者和学生能够轻松理解复杂的数据库内部机制，降低了学习 PostgreSQL 基于进程的架构的门槛。社区反馈表明，如果它能支持查询驱动和交互式操作，将变得更有价值，有望成为数据库课程的教学辅助工具。 该工具是开源的，可在 nikolays.github.io/PGSimCity/ 访问。用户反映自动导览中同时出现的动画过多，容易让人眼花缭乱；部分用户在 4K 显示器上放大时会出现空白屏幕。

hackernews · jonbaer · 7月27日 00:19 · [社区讨论](https://news.ycombinator.com/item?id=49063754)

**背景**: PostgreSQL 采用多进程架构，一个“postmaster”进程为每个客户端连接 fork 出一个新的后端进程。它还使用共享内存和各种后台进程（如 writer、checkpointer）来实现并发和可靠性。理解这一架构对于调优和排查 PostgreSQL 性能问题至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.algomaster.io/p/postgresql-internal-architecture">How PostgreSQL Works: Internal Architecture Explained</a></li>
<li><a href="https://severalnines.com/blog/understanding-postgresql-architecture/">Understanding the PostgreSQL Architecture | Severalnines</a></li>
<li><a href="https://www.postgresql.org/docs/current/spi-memory.html">PostgreSQL: Documentation: 18: 45.3. Memory Management</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该工具的教育价值，但希望增加交互性，例如输入自定义查询并观察其在系统中的流转。部分人认为自动导览信息过载，而使用大屏幕的用户则欣赏其细节丰富度。还有人建议将类似的可视化概念应用于 Kubernetes 等其他领域。

**标签**: `#PostgreSQL`, `#database internals`, `#visualization`, `#educational tool`

---

<a id="item-8"></a>
## [英伟达物理 AI 收入达 100 亿美元，目标 1000 亿](https://news.google.com/rss/articles/CBMiW0FVX3lxTE55VllHTUVsLUR6a3lUSFJ4cGdDZUVFWnNOVUN0bG91N1J0c3E0RUxKdFhzTjFkSDFkbW5BLVZjSkdwbEdJNXBwaFVGVU42bGQ2ZXlQU2luSGNmbGc?oc=5) ⭐️ 7.0/10

英伟达 CEO 黄仁勋宣布，公司的物理 AI 业务收入已达到 100 亿美元，并规划了通往 1000 亿美元的路径。 这一里程碑标志着物理 AI（为机器人和自动驾驶汽车等自主系统提供动力的技术）获得了强大的市场验证，并使英伟达成为下一波 AI 驱动的实体产业中的主导者。 根据 MarketsandMarkets 的数据，物理 AI 市场预计将从 2026 年的 15 亿美元增长到 2032 年的 152.4 亿美元，这使得英伟达的 100 亿美元数字明显大于当前的市场预估。

google_news · finance.biggo.com · 7月26日 22:09

**背景**: 物理 AI 是指能够感知、推理并在物理世界中行动的 AI 系统，使机器人和自动驾驶汽车等自主机器成为可能。英伟达提供硬件（GPU）、仿真平台（如 Omniverse）和 AI 模型来支持这一生态系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/generative-physical-ai/">What is Physical AI? | NVIDIA Glossary</a></li>
<li><a href="https://www.marketsandmarkets.com/ResearchInsight/physical-ai-nvidia.asp">NVIDIA is Driving the Next Era of Physical AI Innovation</a></li>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world">NVIDIA and Global Robotics Leaders Take Physical AI to the Real World | NVIDIA Newsroom</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Physical AI`, `#AI Hardware`, `#Market Growth`, `#Robotics`

---

<a id="item-9"></a>
## [OpenAI 敦促白宫加快前沿 AI 模型审查](https://news.google.com/rss/articles/CBMihwFBVV95cUxQZGZJS3IxSXd1ME9Ib0s5LVpmQmxjdjJicG5FelJBeWhpRG9RNUVtZUhKSllNVDVkM2JCcmYxRTdmNkRoYTRTNWg5WFlqaUpFRS1RUk1DVExWRVBtSk9YMUZYMXVnNTlzZUdWV3N5ZVJ3TmpncXkyNlNIeVloeTkzdHM0SDNKd3M?oc=5) ⭐️ 7.0/10

OpenAI 正在游说白宫加快对前沿 AI 模型的审查流程，推动在模型发布前更快获得监管批准。 此举可能影响美国 AI 监管格局，在缩短先进模型上市时间的同时影响全球标准，凸显了创新速度与安全监管之间的张力。 当前针对前沿模型的自愿性 30 天预发布审查由白宫行政令确立。OpenAI 的推动表明该公司希望审查更快，可能是为了保持竞争优势。

google_news · Unite.AI · 7月26日 12:57

**背景**: 前沿 AI 模型是当前最先进、能力最强的模型，基于海量数据训练，可执行多种任务。美国政府目前依赖自愿审查而非强制监管，这与欧盟的 AI 法案不同。OpenAI 的游说反映了关于如何平衡创新与安全的持续辩论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work - NVIDIA</a></li>
<li><a href="https://carussignal.com/white-house-30-day-frontier-ai-review-explained/">The 30-Day Rule: What the White House's New Frontier - AI Review ...</a></li>

</ul>
</details>

**标签**: `#AI Policy`, `#OpenAI`, `#Regulation`, `#Frontier Models`

---