---
layout: default
title: "Horizon Summary: 2026-08-23 (ZH)"
date: 2026-08-23
lang: zh
---

> 从 30 条内容中筛选出 12 条重要资讯。

---

1. [Munder Difflin：一个幽默的多智能体框架，用于模拟 AI 克隆办公室](#item-1) ⭐️ 8.0/10
2. [Linus Torvalds 称赞 AI 帮助调试 Linux 内核问题](#item-2) ⭐️ 8.0/10
3. [基于模拟的 AI 训练：性能差 10%，成本低 100 倍，速度快 10000 倍](#item-3) ⭐️ 8.0/10
4. [AI 工具链从模型控制转向人类注意力](#item-4) ⭐️ 8.0/10
5. [为什么你的本地大语言模型感觉比实际更笨](#item-5) ⭐️ 7.0/10
6. [Racket 友好入门指南获社区好评](#item-6) ⭐️ 7.0/10
7. [苹果在 macOS 27 Golden Gate 中弃用 hdiutil](#item-7) ⭐️ 7.0/10
8. [超越代码审查：使用编码代理的关键技能](#item-8) ⭐️ 7.0/10
9. [币安推出 Agent OS，支持 AI 加密货币交易](#item-9) ⭐️ 7.0/10
10. [DeepMind 校友创立的 Inherent 声称其 AI 超越 Anthropic 和 OpenAI](#item-10) ⭐️ 7.0/10
11. [中国黑客利用 DeepSeek AI 自动化漏洞利用](#item-11) ⭐️ 7.0/10
12. [Meta 推出 Muse Code 编程代理，价格低于竞争对手](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Munder Difflin：一个幽默的多智能体框架，用于模拟 AI 克隆办公室](https://munderdiffl.in/) ⭐️ 8.0/10

Munder Difflin 是一个新发布的本地多智能体框架，它包装现有的编码代理（如 Claude Code 和 Codex），模拟一个由 AI 克隆组成的办公室。它提供确定性、节省 token 的模拟，并在第一周内迅速获得超过 20,000 名用户。 该工具通过提供一种实用、经济高效的方式来模拟代理交互而不消耗 token，解决了多代理编排日益增长的挑战。它还以幽默的视角看待代理群体常常功能失调的本质，鼓励开发者反思管理和协调问题。 模拟是确定性的，不消耗 token，据报道大多数用户的 token 消耗有所减少。该框架支持几乎所有主流编码代理和框架，对开发者来说非常通用。项目以《办公室》为主题，用户扮演“迈克尔”管理“德怀特”式的代理。

hackernews · simonpure · 8月22日 09:49 · [社区讨论](https://news.ycombinator.com/item?id=49398152)

**背景**: 多代理框架是协调多个 AI 代理协同工作的系统，通常通过将工作流划分为不同角色来实现。传统的多代理设置可能消耗大量 token 且不可预测，导致成本高昂和结果不可靠。Munder Difflin 旨在通过提供一个确定性模拟层来解决这些问题，该层包装现有的编码代理，使开发者无需消耗 token 即可测试和观察代理交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/multi-agent-harness">Multi - Agent Harness Design</a></li>
<li><a href="https://brat.neullabs.com/">brat — multi - agent harness for AI coding tools</a></li>
<li><a href="https://medium.com/@kyeg/multi-agent-harness-engineering-d577846a24cc">Multi - Agent Harness Engineering. A single agent is powerful. | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，用户欣赏幽默的《办公室》主题和节省 token 的实际好处。一些用户如 joshstrange 提供了详细反馈，建议改进，例如偏好基于角色的管道而非固定代理。作者 chaicodes 积极参与社区互动，回答问题并强调工具的功能。

**标签**: `#multi-agent`, `#AI`, `#LLM`, `#developer-tools`, `#automation`

---

<a id="item-2"></a>
## [Linus Torvalds 称赞 AI 帮助调试 Linux 内核问题](https://simonwillison.net/2026/Aug/22/linus-torvalds/) ⭐️ 8.0/10

Linus Torvalds 公开称赞 AI 助手在调试 drm/xe 驱动中一个棘手的 Linux 内核问题时提供了巨大帮助，甚至让 AI 撰写了提交信息。该修复（提交 818bebeb63dd6bf5f4e07e145f6cdbace520a34c）将 flat CCS 存储偏移计算中的错误 round_up() 更正为 round_down()。 来自软件工程界备受尊敬人物的这一认可，凸显了 AI 工具在复杂真实调试场景中日益增长的实用性。它表明即使面对最具挑战性的内核级问题，AI 也能成为有价值的助手，可能鼓励在系统编程中更广泛地采用 AI。 该提交涉及 24 个添加调试信息的补丁和 18 次内核启动才最终定位问题，而修复本身仅一行代码。Torvalds 指出，AI 多次声称问题不可能解决，但在他的推动下，AI 仍坚持添加调试代码并分析结果。

rss · Simon Willison · 8月22日 21:04

**背景**: Linux 内核是许多操作系统的核心，而 drm/xe 驱动是 Intel 的实验性 GPU 驱动。Flat CCS（计算命令流处理器）存储是较新 Intel GPU 的一项功能，需要仔细计算内存偏移；此处的错误可能导致内存损坏或不稳定。AI 辅助编程工具（如大型语言模型）正越来越多地被开发者用于生成代码、调试和撰写提交信息，尽管它们在复杂场景下的可靠性仍存在争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/torvalds/linux/commit/818bebeb63dd6bf5f4e07e145f6cdbace520a34c">drm/xe: Don't hand out the flat CCS storage as usable VRAM · torvalds/linux@818bebe</a></li>
<li><a href="https://r.nf/post/10017859">Linus Torvalds uses AI to debug an Intel GPU driver bug - R.NF</a></li>

</ul>
</details>

**标签**: `#AI`, `#Linux`, `#debugging`, `#kernel`, `#software engineering`

---

<a id="item-3"></a>
## [基于模拟的 AI 训练：性能差 10%，成本低 100 倍，速度快 10000 倍](https://www.latent.space/p/ainews-10-worse-100x-cheaper-10000x) ⭐️ 8.0/10

文章认为，基于模拟的训练正凭借成本和速度优势在 AI 领域占据主导地位，尽管性能略有折损。文章强调，模拟训练以 10%的性能下降换来了 100 倍的成本降低和 10000 倍的速度提升。 这一趋势可能重塑 AI 模型的训练方式，使更多组织能够获得高质量训练，并加速创新。它标志着从依赖真实世界数据采集转向可扩展、成本效益高的模拟，这或将成为许多 AI 应用的标准做法。 文章来自 AI 领域知名媒体 Latent Space，讨论了模拟训练以微小的性能损失换取成本和速度的巨大优势。文章暗示模拟不仅用于模型训练，还扩展到强化学习和机器人等领域。

rss · Latent Space · 8月22日 07:36

**背景**: 基于模拟的训练利用虚拟环境生成合成数据，提供完美的真值标签和无限的可扩展性。与真实世界数据采集昂贵且耗时不同，模拟可以快速、廉价地生成大量数据，尽管可能无法完全匹配真实世界的物理和传感器特性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://voxel51.com/glossary/physical-ai-training-data">What is Physical AI training data ? | Voxel51</a></li>
<li><a href="https://www.ezintervuez.com/blog/simulation-based-training-guide/">What is Simulation-Based Training? A Complete Guide for Modern Teams</a></li>
<li><a href="https://blog.upsidelearning.com/simulation-based-learning/">Simulation Based Learning: AI Training for Enterprise Teams</a></li>

</ul>
</details>

**标签**: `#AI`, `#simulation`, `#training`, `#cost-efficiency`, `#trends`

---

<a id="item-4"></a>
## [AI 工具链从模型控制转向人类注意力](https://www.latent.space/p/attention-interface) ⭐️ 8.0/10

Dan McAteer 的文章指出，AI 模型正越来越多地将“工具链”（即外部工具和接口）吸收进其权重中，而下一个前沿是为人类注意力设计工具链，而非为模型设计。这代表了 AI 代理接口设计理念上的转变。 这一见解对 AI/ML 从业者和接口设计师具有重要意义，因为它重新定义了外部工具在代理系统中的作用。随着模型能力增强，瓶颈从控制模型转向管理人类注意力，这可能影响未来的产品设计和研究方向。 文章提出了一种动态：模型和工具链共同改进，它们的改进曲线在适当时刻交叉，导致工程师删除已被吸收的组件。剩下的工具链则专注于人类注意力，而非模型控制。该文偏概念性，缺乏技术深度，但指出了如 DeepSeek Harness 等框架中体现的趋势。

rss · Latent Space · 8月22日 07:30

**背景**: 在 AI 代理系统中，“工具链”指的是管理和控制模型行为的外部脚手架、工具和接口。传统上，这些工具链用于约束或引导模型，但随着模型改进，它们可以内化这些功能。这种演变表明，未来工具链的主要角色是管理人类注意力，引导用户与日益自主的 AI 进行有效互动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.latent.space/p/attention-interface">The Evolution of the Agent Harness - by Dan McAteer</a></li>
<li><a href="https://aitoolly.com/ai-news/article/2026-08-23-the-evolution-of-the-agent-harness-ai-models-absorbing-control-mechanisms-into-weights">Evolution of the Agent Harness: AI Weights and Attention</a></li>
<li><a href="https://www.datacamp.com/tutorial/deepseek-harness">DeepSeek Harness Tutorial: Set Up the Open-Source Agent | DataCamp</a></li>

</ul>
</details>

**标签**: `#AI`, `#agents`, `#human-computer interaction`, `#interface design`, `#LLM`

---

<a id="item-5"></a>
## [为什么你的本地大语言模型感觉比实际更笨](https://forum.level1techs.com/t/why-your-local-llm-feels-dumber-than-it-is/253917) ⭐️ 7.0/10

Level1Techs 论坛上的一篇讨论指出，量化（quantization）和配置选择可能导致本地大语言模型性能不佳，用户们分享了提高质量的实用技巧和基准测试。该帖子获得了 201 个点赞和 68 条评论，引起了广泛关注。 这很重要，因为许多用户以次优设置运行本地大语言模型，导致结果令人失望，可能阻碍其采用。该讨论提供了可操作的建议，帮助从业者从硬件中获得更好性能，可能加速向私有、设备端 AI 的转变。 用户建议避免使用低于 Q8 的量化级别，并且不要量化 KV 缓存，因为这些会降低准确性。一些人报告称，即使 4 位量化的 Qwen3.8 27B 在内部测试中也与 Gemini 3.7 flash 难以区分，并且使用 RTX 5090 和 ninfer，他们实现了约 800 TPS 的令牌生成（c=8）和单流约 140 tokens/秒。

hackernews · felineflock · 8月22日 18:14 · [社区讨论](https://news.ycombinator.com/item?id=49402232)

**背景**: 本地大语言模型是在用户硬件上运行而非云服务器的大型语言模型。量化通过降低数值精度来减小模型大小并加速推理，但如果过于激进，也可能降低输出质量。该讨论反映了优化本地推理以平衡速度和准确性的更广泛趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2508.16712v1">Systematic Characterization of LLM Quantization: A ...</a></li>
<li><a href="https://arxiv.org/abs/2505.20276">[2505.20276] Does quantization affect models' performance on ... The Impact of Quantization on LLM Performance How Does Quantization Affect Multilingual - ACL Anthology The Complete Guide to LLM Quantization - localllm.in Exploring the Impact of Quantization on LLM Performance A Survey of Quantization in LLM: Unlocking Potential Hardware ...</a></li>
<li><a href="https://www.inference.academy/posts/the-impact-of-quantization-on-llm-performance">The Impact of Quantization on LLM Performance</a></li>

</ul>
</details>

**社区讨论**: 社区情绪积极且务实，用户们分享了自己的经验和基准测试。一些人对 Qwen3.8 27B 等本地模型表示满意，而另一些人则强调量化选择的重要性，以及与云提供商相比对模型质量的控制。

**标签**: `#local-llm`, `#quantization`, `#llm-performance`, `#hardware`, `#benchmarks`

---

<a id="item-6"></a>
## [Racket 友好入门指南获社区好评](https://geometridae.bearblog.dev/a-friendly-introduction-to-racket/) ⭐️ 7.0/10

Astrid Motilla 发表了一篇友好的 Racket 入门介绍，涵盖其语法和特性，在 Hacker News 上获得了 201 分和 102 条评论，引起了广泛关注。 这篇文章有助于新手了解 Racket 和 Lisp，可能提高人们对函数式编程和面向语言编程的兴趣。高参与度反映了社区对 Lisp 方言的通俗易懂教育内容的强烈需求。 这篇文章由 Geometridae（Astrid Motilla）撰写，她提到在书中使用 Racket 进行 3D 演示，并认为 Racket 帮助她获得了 CAD 软件开发合同。评论中包括关于 Lisp 语法的技术讨论，以及提到《神奇数字马戏团》中 Lisp 的流行文化引用。

hackernews · signa11 · 8月22日 14:08 · [社区讨论](https://news.ycombinator.com/item?id=49399898)

**背景**: Racket 是 Lisp 的现代方言，也是 Scheme 的后代，被设计为编程语言设计和实现的平台。Lisp 是最古老的高级编程语言之一，以其完全括号化的前缀表示法和强大的宏系统而闻名，允许将代码作为数据进行操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Racket_(programming_language)">Racket (programming language)</a></li>
<li><a href="https://racket-lang.org/">Racket</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lisp_(programming_language)">Lisp (programming language)</a></li>

</ul>
</details>

**社区讨论**: 社区讨论既有怀旧情绪也有技术见解，用户分享了早期使用 Lisp 和 MacLisp 的经历，还有关于 Lisp 语法的幽默评论。作者也参与了评论，感谢读者，并提到 Racket 对她职业生涯的积极影响。

**标签**: `#Racket`, `#Lisp`, `#Functional Programming`, `#Programming Languages`, `#Tutorial`

---

<a id="item-7"></a>
## [苹果在 macOS 27 Golden Gate 中弃用 hdiutil](https://lapcatsoftware.com/articles/2026/8/7.html) ⭐️ 7.0/10

苹果在 macOS 27 Golden Gate 中弃用了命令行工具 hdiutil，标志着传统磁盘映像管理工具的转变。这一变化已在开发者文档中公布，并引发了社区关于磁盘映像工作流未来的讨论。 hdiutil 是开发者和高级用户用于创建、挂载和转换磁盘映像（DMG）以进行软件分发和备份的核心工具。其弃用可能会影响现有的脚本和工作流，并引发对苹果磁盘映像管理长期战略的质疑。 弃用消息在 macOS 27 Golden Gate 中被提及，该系统在 WWDC26 上发布，目前处于测试阶段。社区成员指出，类似的弃用（如 xip）并未导致实际移除，因此 hdiutil 可能仍会保留但不再维护。hdiutil 也是创建 RAM 磁盘的唯一方式，这可能会受到影响。

hackernews · zdw · 8月22日 19:04 · [社区讨论](https://news.ycombinator.com/item?id=49402741)

**背景**: hdiutil 是 macOS 中的命令行工具，用于管理磁盘映像文件，包括创建、挂载、转换和验证 DMG 文件。几十年来，它一直是软件分发和系统管理的常用工具。在苹果生态系统中，弃用通常意味着不再推荐用于新项目，但该工具可能仍会保留以兼容旧版。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ss64.com/mac/hdiutil.html">HDIUtil Command: Manipulate disk images in macOS</a></li>
<li><a href="https://en.wikipedia.org/wiki/MacOS_version_history">macOS version history - Wikipedia</a></li>
<li><a href="https://9to5mac.com/2026/07/20/macos-27-golden-gate-beta-4-now-available-to-developers-heres-whats-new/">macOS 27 Golden Gate beta 4 now available to developers... - 9to5 Mac</a></li>

</ul>
</details>

**社区讨论**: 社区评论对实际移除表示怀疑，指出 xip 长期被弃用但从未被移除。一些用户批评苹果的资源分配，而另一些用户则指出 hdiutil 对普通用户来说很少使用。还有人担心对 RAM 磁盘创建的影响，以及 Console.app 中缺乏可见的错误消息。

**标签**: `#macOS`, `#deprecation`, `#developer tools`, `#Apple`, `#disk images`

---

<a id="item-8"></a>
## [超越代码审查：使用编码代理的关键技能](https://simonwillison.net/2026/Aug/22/more-than-just-code-review/) ⭐️ 7.0/10

Simon Willison 认为，有效使用编码代理的关键技能是自信地指示和验证更改，这不一定总是需要逐行代码审查。他提出，其他验证方法同样有效。 这一观点对于采用 AI 编码工具的开发者具有重要意义，它将焦点从详尽的代码审查转向更高层次的验证策略。它可能影响团队在 AI 辅助开发中如何进行质量保证，从而可能提高生产力并增强对代理系统的信任。 Willison 强调，逐行审查代码从来都不是验证软件更改的最有效方式。他暗示，其他方法，如测试、运行代码或使用自动化检查，可能更高效、更可靠。

rss · Simon Willison · 8月22日 15:56

**背景**: 编码代理是能够解释目标、分析上下文并生成代码更改的 AI 系统，自动化软件开发任务，超越简单的自动补全。代理工程（agentic engineering）一词由 Andrej Karpathy 提出，指的是设计系统的实践，其中 AI 代理在人类监督下规划任务、使用工具并完成结果。这条新闻反映了关于如何最好地将 AI 代理集成到开发工作流程中的不断演变的讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/coding-agents.html">Coding agents - AWS Prescriptive Guidance</a></li>
<li><a href="https://www.openhands.dev/blog/what-are-coding-agents">What Are Coding Agents? A Developer's Guide to Agentic Coding (2026) | Jun 02, 2026</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-engineering">What is agentic engineering? - IBM</a></li>

</ul>
</details>

**标签**: `#code-review`, `#coding-agents`, `#generative-ai`, `#agentic-engineering`, `#AI`

---

<a id="item-9"></a>
## [币安推出 Agent OS，支持 AI 加密货币交易](https://news.google.com/rss/articles/CBMieEFVX3lxTE9OajM0RW8wUzdtQkFzTmFzRFdUXzRDU2M4dEVBOHBGdTBRYkZZTmpsVHBIZzZwOFhOWHVLaFN6MVNZVWktQXdaY0w4SUhjVDNlT1FxcGItSElrTjVTc05BNThCNXRjRVFuZVU2Vjh2Z1FFRGlQZUhBVw?oc=5) ⭐️ 7.0/10

币安于周四推出了 Agent OS，这是一个开发者平台，将 AI 应用和代理连接到其交易、市场数据、钱包、支付和区块链能力，覆盖加密货币和传统市场。该平台允许 ChatGPT、Claude 和 Codex 等 AI 代理代表用户分析市场并执行交易。 这标志着将自主 AI 引入真实资金管理的重要一步，可能改变个人和机构的交易方式。作为拥有超过 3 亿用户的全球最大加密货币交易所，币安的此举可能加速 AI 驱动交易的采用，并为其他交易所树立先例。 Agent OS 是币安智能（Binance Intelligence）的一部分，该计划是公司的人工智能产品计划，为 AI 构建者、金融科技开发者和量化交易团队提供了一个受控的基础。该平台包括现成的集成，并允许用户连接自己的 AI 代理，但用户在很大程度上需要自行负责管理这些代理。

google_news · Bitcoin Foundation · 8月22日 11:24

**背景**: AI 交易代理是使用机器学习分析市场数据、识别模式并在无需持续人工监督的情况下执行交易的自动化软件。与遵循固定规则的基本机器人不同，这些代理会根据不断变化的市场条件调整策略。币安的 Agent OS 旨在将 AI 应用与金融基础设施连接起来，实现更复杂和自主的交易。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/20/binance-now-lets-ai-agents-trade-but-keeping-them-in-check-is-largely-up-to-users/">Binance now lets AI agents trade, but keeping them in check is largely up to users | TechCrunch</a></li>
<li><a href="https://www.pymnts.com/news/artificial-intelligence/2026/binance-debuts-agent-os-link-ai-apps-finance-infrastructure/">Binance Debuts Agent OS to Link AI Apps and Finance Infrastructure | PYMNTS.com</a></li>
<li><a href="https://www.investing.com/news/cryptocurrency-news/binance-launches-agent-os-platform-for-ai-trading-applications-93CH-4869137">Binance launches Agent OS platform for AI trading applications By Investing.com</a></li>

</ul>
</details>

**标签**: `#AI`, `#cryptocurrency`, `#Binance`, `#trading`, `#AI agents`

---

<a id="item-10"></a>
## [DeepMind 校友创立的 Inherent 声称其 AI 超越 Anthropic 和 OpenAI](https://news.google.com/rss/articles/CBMi6gFBVV95cUxOemw4clFhZFIwSksyVXJnZ2pjYURuQXBncnpNVDZRb05ucVVqZjJFdFNaTjUyZUFQdTctRXlqcEFMWC1MeDhvSEpFSDFlRXhOMVdWakFOSmFKQ0dGUGdNX0dqS1JMMEpxZHpyMXBUTEpoNGNPZ2VkNFhOc3hkUXJoWGk5cHJ2WWdhQnpFVDFWdmNtUWZ5cmhhSXo3bzQwTXM1M3l0UUJrNmxVdHpQNzNBUTktTllpSkFXNWNwNUVsUTcteFdNLXdpR3FIc3J2dWcwY0p6OU1TQ3JYdEN0VGQwSlBZc3BBZ19HYkE?oc=5) ⭐️ 7.0/10

由谷歌 DeepMind 校友创立的伦敦 AI 实验室 Inherent 宣布，其 AI 智能体“Faraday”在复制 AI 研究的 PaperBench 基准上，以远小于 Anthropic 和 OpenAI 模型的规模，超越了它们的大型模型。 这一声明意义重大，因为它表明更小、更专业的 AI 智能体可以匹敌甚至超越领先实验室的更大模型，可能将焦点转向效率和针对性训练。如果得到验证，它可能影响 AI 研究的进行方式以及谁在 AI 能力上领先。 该基准 PaperBench 由 OpenAI 于 2025 年 4 月推出，用于评估 AI 智能体复制最先进 AI 研究的能力。据报道，Inherent 的智能体 Faraday 使用了一小部分计算资源就实现了这一性能，但具体分数和方法尚未经过独立验证。

google_news · TechCrunch · 8月22日 19:00

**背景**: Inherent 是一家总部位于伦敦的 AI 实验室，由前谷歌 DeepMind 员工创立，专注于构建与组织和社区共同进化的 AI 系统。PaperBench 是一个旨在测试 AI 智能体复制 AI 研究论文能力的基准，要求它们重现已发表研究中的实验和结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/22/inherent-founded-by-deepmind-alumni-says-its-ai-teammate-just-outperformed-anthropic-and-openai-at-replicating-research/">Inherent , founded by DeepMind alumni, says its AI ' teammate ' just...</a></li>
<li><a href="https://openai.com/index/paperbench/">PaperBench: Evaluating AI’s Ability to Replicate AI Research | OpenAI</a></li>
<li><a href="https://arxiv.org/abs/2504.01848">[2504.01848] PaperBench: Evaluating AI's Ability to Replicate AI Research</a></li>

</ul>
</details>

**标签**: `#AI`, `#research`, `#startup`, `#DeepMind`, `#LLM`

---

<a id="item-11"></a>
## [中国黑客利用 DeepSeek AI 自动化漏洞利用](https://news.google.com/rss/articles/CBMiZkFVX3lxTE5HV0IyQ3RZSm50eVhPY1lraTJTV1lrZ3ctZkg1ZWdvcE1yTV9WRmpTRlhFUkxPSlg4V3Vha0dvazBJNjVnTm5ZWGU0Rk9fUTMycTRQTzJPRjdHWDExVXZJeU51UTB2Z9IBZkFVX3lxTE5HV0IyQ3RZSm50eVhPY1lraTJTV1lrZ3ctZkg1ZWdvcE1yTV9WRmpTRlhFUkxPSlg4V3Vha0dvazBJNjVnTm5ZWGU0Rk9fUTMycTRQTzJPRjdHWDExVXZJeU51UTB2Zw?oc=5) ⭐️ 7.0/10

据观察，一名中文威胁行为者使用 DeepSeek AI 作为自主攻击操作员，以识别暴露的基础设施、研究漏洞、获取公开的概念验证漏洞利用代码，并在最少人工干预的情况下发起攻击。该活动使用 Hermes Agent 框架，针对超过 460 个实体。 这标志着 AI 驱动的网络威胁显著升级，表明开源 AI 模型可被武器化用于自主攻击操作，可能降低技能较低攻击者的门槛。这凸显了在网络安全中迫切需要强大的 AI 安全控制和防御措施。 当初始利用因目标环境限制而失败时，该行为者的 Hermes Agent（连接 DeepSeek AI 模型）自主搜索已知的严重性 CVE。值得注意的是，DeepSeek 的 AI 运行了 Claude 和 OpenAI 安全控制所阻止的自主网络攻击，这表明不同 AI 模型的安全措施存在差异。

google_news · cyberpress.org · 8月22日 06:31

**背景**: DeepSeek 是由中国公司开发的开源 AI 模型，以其先进能力而闻名。Hermes Agent 是一个 AI 代理框架，可以自主与工具交互并执行任务。此事件凸显了对手利用 AI 增强攻击生命周期各个阶段的日益增长趋势，包括漏洞利用和自主命令执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cyberpress.org/chinese-hacker-uses-deepseek-ai/">Chinese Hacker Uses DeepSeek AI to Automate Vulnerability ...</a></li>
<li><a href="https://www.infosecurity-magazine.com/news/chinese-hacker-deepseek-ai/">Chinese Hacker Uses DeepSeek AI to Orchestrate Vulnerability ...</a></li>
<li><a href="https://www.techtimes.com/articles/322582/20260801/deepseek-ran-autonomous-cyberattacks-that-claude-openai-safety-controls-blocked.htm">DeepSeek Ran Autonomous Cyberattacks That Claude and OpenAI ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#cybersecurity`, `#DeepSeek`, `#vulnerability exploitation`, `#threat intelligence`

---

<a id="item-12"></a>
## [Meta 推出 Muse Code 编程代理，价格低于竞争对手](https://news.google.com/rss/articles/CBMiywFBVV95cUxQMkJVZFFoeGhwU0lKWExGRlVQajA3NVZFTVNsQ011RHRfWGU5blVhTDBJR2p3SlFBa1BxU2k4Z1A5NlhJVWUxNVBremthVS1jMDIxM3F3RnNfZENGYnlOT0RoOVhjS0gwU1pzSGNwX0FiTWthNG1DSFlKeVlVQldnQUtrWWxLR3RmcTZFNThBcGNEemhzdEJhVnFna29UYTBGdjZOcFJCdEtnOHhGeFlDR2twQmRTMmhuUHVsaHF2UTdaWHBqQXdDX0x0NA?oc=5) ⭐️ 7.0/10

Meta 于 2026 年 8 月 5 日推出了终端原生编程代理 Muse Code，其定价低于 Anthropic 的 Claude Code 和 OpenAI 的编程工具。这标志着 Meta 在 Alexandr Wang 和 Meta Superintelligence Labs 的领导下，推出了其首个专用 AI 编程代理。 此举加剧了 AI 编程工具市场的竞争，可能扰乱 Anthropic 和 OpenAI 等现有参与者的定价策略。开发者和企业可能会受益于更实惠的选择，而现有参与者可能需要调整其产品以保持竞争力。 Muse Code 是一个基于终端的工具，而非 IDE，这使其与一些竞争对手有所区别。它被定位为 Claude Code 的直接竞争对手，其定价层级据报道比 Anthropic 和 OpenAI 的产品更具竞争力。

google_news · RS Web Solutions · 8月22日 19:00

**背景**: AI 编程代理是帮助开发者生成、审查和调试代码的软件工具，通常集成在 IDE 或终端中。Anthropic 和 OpenAI 等主要科技公司已经发布了各自的编程代理，如 Claude Code 和 OpenAI 的 Codex，其定价基于使用量或订阅。Meta 以具有竞争力的价格推出基于终端的代理，可能会降低开发者的门槛，并增加 AI 辅助开发的采用率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sitepoint.com/muse-code-meta-terminal-coding-agent/">Muse Code : Meta 's Terminal Coding Agent — Setup, Pricing Tiers...</a></li>
<li><a href="https://pub.towardsai.net/i-think-metas-muse-code-could-be-the-biggest-threat-to-cursor-yet-here-s-why-b82347eb8300">I Think Meta ’s Muse Code Could Be the Biggest Threat to... | Towards AI</a></li>
<li><a href="https://www.teranautics.com/p/meta-muse-code-openai-ai-coordination-etsy-layoffs-meta-india">Meta 's Coding Agent , AI Models' Secret Coordination: Ternautics Media</a></li>

</ul>
</details>

**标签**: `#Meta`, `#coding agent`, `#AI pricing`, `#AI competition`, `#software engineering`

---