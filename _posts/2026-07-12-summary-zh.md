---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> 从 44 条内容中筛选出 15 条重要资讯。

---

1. [xAI 的 Grok Build CLI 上传整个仓库，包括.env 文件](#item-1) ⭐️ 9.0/10
2. [GPT-5.6 一小时攻克 50 年图论猜想](#item-2) ⭐️ 9.0/10
3. [vLLM v0.25.0：Model Runner V2 成为默认，PagedAttention 被移除](#item-3) ⭐️ 8.0/10
4. [RISCBoy：基于 RISC-V 的开源掌机](#item-4) ⭐️ 8.0/10
5. [UPI 交易架构深度解析](#item-5) ⭐️ 8.0/10
6. [SQLite 中应优先使用 STRICT 表](#item-6) ⭐️ 8.0/10
7. [VultronRetriever 模型登顶 MTEB 排行榜](#item-7) ⭐️ 8.0/10
8. [U-Boot 引导程序漏洞可在系统启动前执行代码](#item-8) ⭐️ 8.0/10
9. [Mesh LLM：基于 Iroh 的分布式 AI 计算](#item-9) ⭐️ 7.0/10
10. [智谱创始人启动“摸高计划”攻关 AGI](#item-10) ⭐️ 7.0/10
11. [Claude Code 桌面版新增内置浏览器](#item-11) ⭐️ 7.0/10
12. [谷歌反对欧洲网站屏蔽，美国反盗版立法加速](#item-12) ⭐️ 7.0/10
13. [强脑科技押注可穿戴脑机接口，无需开颅](#item-13) ⭐️ 7.0/10
14. [欧盟拟对大型科技公司消费者保护失职处以罚款](#item-14) ⭐️ 7.0/10
15. [微软和谷歌支持 Go 语言用于 AI 智能体](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [xAI 的 Grok Build CLI 上传整个仓库，包括.env 文件](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) ⭐️ 9.0/10

对 xAI 的 Grok Build CLI（版本 0.2.93）的流量分析显示，该工具会上传整个仓库内容，包括 git 历史和.env 等敏感文件，无论“改进模型”开关是否开启。 这是一个严重的隐私违规行为，因为即使用户明确选择退出数据收集，它也会将专有代码和机密暴露给 xAI，破坏了用户对 AI 编码工具的信任，并给开发者和组织带来严重的安全隐患。 分析显示，CLI 会逐字未脱敏地传输文件内容，将数据持久化到指定的 GCS 存储桶，并且上传机制未在 CLI 的设置材料中披露。“改进模型”开关没有区别——无论开或关，整个仓库都会以相同方式上传。

hackernews · jhoho · 7月12日 01:09 · [社区讨论](https://news.ycombinator.com/item?id=48877371)

**背景**: Grok Build CLI 是 xAI 于 2026 年 5 月推出的一款编码代理和终端工具，由 Grok 4.5 驱动，旨在协助完成复杂的软件工程任务。该工具面向 SuperGrok 和 X Premium Plus 订阅用户。该工具本应读取代码并提供帮助，但用户期望在禁用数据收集时，他们的代码不会被发送到 xAI 服务器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547">What xAI Grok Build CLI actually sends to xAI - a wire-level analysis (grok 0.2.93) · GitHub</a></li>
<li><a href="https://x.ai/news/grok-build-cli">Introducing Grok Build | SpaceXAI</a></li>
<li><a href="https://www.eigent.ai/blog/grok-build-cli">Grok Build CLI Review 2026: Features & Alternatives</a></li>

</ul>
</details>

**社区讨论**: 社区表达了震惊和愤怒，许多人称这种行为是“大规模监控活动”和严重的安全漏洞。一些用户表示，由于此类担忧，他们选择不使用 xAI 产品，而另一些用户则建议使用 bubblewrap 等沙盒工具来降低风险。也有人对 AI 生成的分析表示怀疑，呼吁进行独立验证。

**标签**: `#privacy`, `#security`, `#xAI`, `#AI tools`, `#data leakage`

---

<a id="item-2"></a>
## [GPT-5.6 一小时攻克 50 年图论猜想](https://www.qbitai.com/2026/07/447873.html) ⭐️ 9.0/10

OpenAI 的 GPT-5.6 Sol Ultra 在不到一小时内自主证明了图论中存在约 50 年的循环双覆盖猜想，使用了 64 个子代理并行工作，并生成了一份 3 页的 PDF 证明。 这标志着 AI 首次自主解决了一个长期未解决的数学开放问题，展示了高级推理和多代理协调能力。它可能改变数学研究的方式，让 AI 辅助甚至主导发现。 该证明将问题转化为有限域上的边标号和线性方程组，为每条边分配两个标签，使得相同标签的边构成圈。OpenAI 还公布了完整的约 700 字符的提示词，明确了验收标准、定义、边界条件和失败情形，而不规定固定步骤。

telegram · zaihuapd · 7月12日 03:49

**背景**: 循环双覆盖猜想询问是否每个无桥图（即删除任何一条边都不会使图断开的图）都存在一组圈，使得每条边恰好被覆盖两次。该猜想由 Szekeres（1973 年）和 Seymour（1979 年）独立提出，是图论中的一个重要开放问题。GPT-5.6 的 Sol Ultra 模式具有内置的多代理编排能力，可以生成 64 个子代理同时处理问题的不同部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cycle_double_cover_conjecture">Cycle double cover conjecture</a></li>
<li><a href="https://chatforest.com/builders-log/openai-gpt-5-6-sol-ultra-mode-subagents-parallel-architecture-builder-guide/">GPT-5.6 Sol Ultra Mode: Built-In Multi-Agent Orchestration ...</a></li>
<li><a href="https://www.techtimes.com/articles/319808/20260707/gpt-56-sol-review-faster-coding-half-fable-5-cost-benchmark-problem.htm">GPT-5.6 Sol Review: Faster Coding, Half Fable 5 Cost, and a ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#graph theory`, `#LLM`, `#mathematical proof`, `#OpenAI`

---

<a id="item-3"></a>
## [vLLM v0.25.0：Model Runner V2 成为默认，PagedAttention 被移除](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 8.0/10

vLLM v0.25.0 将 Model Runner V2 设为所有稠密模型的默认执行路径，并移除了旧的 PagedAttention 实现。该版本还引入了 LLaVA-OneVision-2 和 GLM-5 等新模型、一个流式解析引擎，以及支持异构词表的通用推测解码。 此版本标志着 vLLM 的重大架构转变，在简化代码库的同时提升了性能和模块化程度。移除曾经的核心创新 PagedAttention，表明新后端已成熟，并为 LLM 推理效率树立了新标准。 Model Runner V2 现在支持 EVS（高效视频采样）用于视频 token 剪枝、实时嵌入，以及支持完整 CUDA 图的动态推测解码。Transformers 建模后端经过优化，速度已与原生 vLLM 持平，新增模型包括 GLM-5、MiniMax-M3 和 Hy3。

github · khluu · 7月11日 20:06

**背景**: vLLM 是一个用于高吞吐量 LLM 推理和服务的高性能开源库，最初由加州大学伯克利分校开发。PagedAttention 是其管理注意力键值缓存的关键创新，但 Model Runner V2 等新后端凭借更好的性能和模块化设计已取代了它。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM | vLLM Blog</a></li>
<li><a href="https://docs.vllm.ai/en/v0.22.1/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/paged_attention/">Paged Attention - vLLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#release`, `#performance`, `#open source`

---

<a id="item-4"></a>
## [RISCBoy：基于 RISC-V 的开源掌机](https://github.com/Wren6991/RISCBoy) ⭐️ 8.0/10

RISCBoy 是一款从头设计的开源便携游戏机，采用 RISC-V 指令集架构，由树莓派工程师 Luke Wren 打造。它被描述为来自 RISC-V 在 2001 年就已存在的平行宇宙的 Gameboy Advance。 该项目展示了 RISC-V 在嵌入式系统和复古游戏中的潜力，将开源 ISA 与怀旧形态相结合。它凸显了 RISC-V 硬件生态的成长，并可能激发更多开源游戏设备的出现。 该游戏机完全从头构建，包括 RISC-V 核心，硬件设计文件在 GitHub 上完全开源。它使用了 AHB/APB 总线协议，这些协议通常与 ARM 关联，但实际上是开放标准。

hackernews · mariuz · 7月11日 21:58 · [社区讨论](https://news.ycombinator.com/item?id=48876245)

**背景**: RISC-V 是一种免费开放的指令集架构（ISA），任何人都可以免版税实现，不同于 ARM 和 x86 等专有 ISA。Gameboy Advance 是任天堂于 2001 年发布的一款流行的 32 位掌机，采用 ARM7 CPU 并兼容 Game Boy 游戏。RISCBoy 使用现代开源 ISA 模拟了这一体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V">RISC-V - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/RISC-V_architecture">RISC-V architecture</a></li>

</ul>
</details>

**社区讨论**: 社区称赞该项目技术深度和新颖性，评论提到创建者之前的工作 PicoDVI（基于 RP2040 的 DVI/HDMI）。一些人惊讶于 AHB/APB 协议是开放的而非 ARM 专有，这凸显了一个常见误解。

**标签**: `#RISC-V`, `#open-source hardware`, `#retro gaming`, `#embedded systems`

---

<a id="item-5"></a>
## [UPI 交易架构深度解析](https://timeseriesofindia.com/economy/reads/upi-architecture/) ⭐️ 8.0/10

一篇文章深入分析了 UPI 的交易架构，涵盖其设计、中介机构和可扩展性，并引发了关于隐私和全球比较的社区讨论。 这一分析很重要，因为 UPI 是印度主要的实时支付系统，每月处理数十亿笔交易，了解其架构有助于工程师和政策制定者评估其优缺点。 文章指出，UPI 每年处理约 220 亿笔交易，在 NPCI 交换机上平均每秒约 700 笔，峰值负载可能更高，并设有千万/十亿切换功能以提高可读性。

hackernews · prtk25 · 7月11日 16:33 · [社区讨论](https://news.ycombinator.com/item?id=48873457)

**背景**: UPI（统一支付接口）是印度国家支付公司（NPCI）于 2016 年开发的即时支付系统。它通过手机实现银行间个人对个人和个人对商户的交易，使用与银行账户关联的虚拟支付地址。该系统涉及多个中介机构，包括付款人银行、收款人银行和作为中央交换机的 NPCI。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unified_Payments_Interface">Unified Payments Interface - Wikipedia</a></li>
<li><a href="https://medium.com/@avinashkariya05910/deep-dive-system-design-of-upi-unified-payments-interface-eff3b0334b0d">Deep Dive: System Design of UPI (Unified Payments Interface) | by Avinash Kariya | Medium</a></li>
<li><a href="https://www.thesgn.blog/blog/upi">UPI System Design Explained | High-Level Architecture of ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了由于多个中介机构和身份关联带来的隐私问题，同时赞扬了 UPI 在推动老年用户数字化采用方面的成功。一些人将其每秒查询数（700）与纳斯达克的 10 万以上每秒查询数进行不利比较，但指出峰值负载更高。千万/十亿切换功能作为用户体验改进受到赞赏。

**标签**: `#UPI`, `#payment systems`, `#architecture`, `#scalability`, `#privacy`

---

<a id="item-6"></a>
## [SQLite 中应优先使用 STRICT 表](https://evanhahn.com/prefer-strict-tables-in-sqlite/) ⭐️ 8.0/10

Evan Hahn 的一篇指南提倡在 SQLite 中使用 STRICT 表来强制数据类型，防止将文本插入整数列等常见错误。文章指出，STRICT 表在 SQLite 3.37.0 中引入，提供了严格的类型检查。 这很重要，因为 SQLite 默认的灵活类型可能导致数据损坏，尤其是在多应用或生产环境中。采用 STRICT 表可提高数据完整性，使 SQLite 与传统 SQL 数据库对齐，从而在严肃使用中更加可靠。 STRICT 表只允许 INT、INTEGER、REAL、TEXT、BLOB 或 ANY 类型的列，并在插入/更新时拒绝类型不匹配。然而，没有 ALTER TABLE 语句可以将现有表转换为 STRICT；社区成员 simonw 指出，必须将数据复制到新表中。

hackernews · ingve · 7月11日 17:33 · [社区讨论](https://news.ycombinator.com/item?id=48873940)

**背景**: SQLite 传统上使用动态类型，列类型只是建议而非严格规则。这种灵活性允许在任何列中存储任何值，但可能导致数据完整性问题。STRICT 表在 3.37.0 版本（2021-11-27）中引入，强制执行严格类型，使 SQLite 的行为更接近传统 SQL 数据库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sqlite.org/stricttables.html">STRICT Tables - SQLite</a></li>
<li><a href="https://sqlite.org/datatype3.html">Datatypes In SQLite</a></li>
<li><a href="https://evanhahn.com/prefer-strict-tables-in-sqlite/">Prefer STRICT tables in SQLite - evanhahn.com</a></li>

</ul>
</details>

**社区讨论**: 社区成员如 simonw 和 dfabulich 进行了细致的讨论。simonw 创建了一个工具将非严格表转换为严格表，而 dfabulich 引用了 SQLite 官方关于灵活类型的立场，认为灵活类型的好处通常大于风险。其他人则希望 STRICT 成为默认设置，并提到了企业可靠性方面的担忧。

**标签**: `#SQLite`, `#database`, `#data integrity`, `#best practices`

---

<a id="item-7"></a>
## [VultronRetriever 模型登顶 MTEB 排行榜](https://www.reddit.com/r/MachineLearning/comments/1utmxq8/vultronretriever_family_of_models_released_on/) ⭐️ 8.0/10

VultronRetriever 系列嵌入模型（Prime-8B、Core-4.5B、Flash-0.8B）已在 HuggingFace 上发布，在 MTEB 排行榜各自类别中排名第一，相比之前的 9B 类领先模型，索引存储最多缩小 16 倍，吞吐量提升 12 倍。 这些模型表明，以极低的资源需求即可实现最先进的检索性能，从而能够在 iPhone 等边缘设备上完全离线部署，这可能使高质量语义搜索和检索增强生成（RAG）系统的访问更加普及。 VultronRetrieverPrime-8B 模型采用 Hydra 架构实现后期交互检索，在内存仅为同类模型一半的情况下提供高精度。所有模型均在 0% 跨数据集重复和 0% 评估污染的数据集上训练，在私有 MTEB 评估中未显示过拟合。

reddit · r/MachineLearning · /u/madkimchi · 7月11日 15:22

**背景**: MTEB（大规模文本嵌入基准）排行榜是评估文本嵌入模型在检索、聚类和分类等任务上性能的广泛认可的基准。由 ColBERT 等模型开创的后期交互检索使用 token 级表示，比单向量嵌入实现更精确的匹配，但代价是索引更大。Hydra 架构是一种将后期交互检索与高效生成相结合的新方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/spaces/mteb/leaderboard">MTEB Leaderboard - a Hugging Face Space by mteb</a></li>
<li><a href="https://weaviate.io/blog/late-interaction-overview">An Overview of Late Interaction Retrieval Models: ColBERT ...</a></li>
<li><a href="https://docs.hydra.so/intro/architecture">Architecture - Hydra</a></li>

</ul>
</details>

**标签**: `#embedding models`, `#MTEB leaderboard`, `#efficient retrieval`, `#offline AI`, `#HuggingFace`

---

<a id="item-8"></a>
## [U-Boot 引导程序漏洞可在系统启动前执行代码](https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/) ⭐️ 8.0/10

U-Boot 的 FIT 签名验证代码中发现 6 个漏洞，其中 2 个可导致任意代码执行，4 个可造成拒绝服务。这些漏洞影响自 v2013.07 以来的 50 多个稳定版本及大量下游厂商分支。 这些漏洞允许攻击者在操作系统和安全软件启动之前执行恶意代码，从而实现隐蔽的固件攻击，可禁用安全功能或植入持久性恶意软件。具有远程固件更新能力的系统（如 BMC）尤其危险，因为无需物理接触即可利用。 这些漏洞编号为 BRLY-2026-037 至 BRLY-2026-042。补丁已提交并被 U-Boot 维护者接受，但部署取决于硬件厂商将其集成到固件更新中；已停止支持的老旧设备可能永远无法获得修复。

telegram · zaihuapd · 7月11日 08:32

**背景**: U-Boot 是嵌入式设备广泛使用的开源引导程序，负责加载操作系统。FIT（Flattened Image Tree）是一种用于打包内核、设备树及其他镜像并附带加密签名的格式，以确保真实性。漏洞位于签名验证逻辑中，该逻辑本应防止未授权代码在启动时被执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.u-boot-project.org/en/latest/usage/fit/signature.html">U - Boot FIT Signature Verification — Das U - Boot unknown version...</a></li>
<li><a href="https://cybersecuritynews.com/u-boot-fit-signature-verification/">Six U - Boot FIT Signature Verification Flaws Enable Code Execution...</a></li>
<li><a href="https://thehackernews.com/2026/07/six-new-u-boot-flaws-could-let.html">Six New U - Boot Flaws Could Let Malicious Images Crash Devices or...</a></li>

</ul>
</details>

**标签**: `#security`, `#firmware`, `#U-Boot`, `#vulnerability`, `#bootloader`

---

<a id="item-9"></a>
## [Mesh LLM：基于 Iroh 的分布式 AI 计算](https://www.iroh.computer/blog/mesh-llm) ⭐️ 7.0/10

Mesh LLM 是一个新的开源项目，它通过 iroh 网络库将异构设备（笔记本电脑、服务器、云节点）汇集起来进行分布式 LLM 推理，并暴露兼容 OpenAI 的 API。 这种方法通过允许用户将本地普通硬件组合成强大的推理集群，减少了对昂贵云 GPU 的依赖，从而民主化了对大型语言模型的访问。 该项目使用 iroh 的点对点网络通过加密密钥连接设备，并由 skippy 引擎将大模型分割到多个节点。性能声称包括在 2 个节点上对 Qwen 235B MoE 达到 16 tok/s。

hackernews · tionis · 7月11日 22:38 · [社区讨论](https://news.ycombinator.com/item?id=48876505)

**背景**: Iroh 是一个基于 Rust 的点对点网络库，通过加密密钥而非 IP 地址路由连接，即使在 NAT 后也能实现设备间直接通信。Mesh LLM 利用 iroh 创建无需中心服务器的分布式推理网格。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.iroh.computer/blog/mesh-llm">Mesh LLM: distributed AI computing on iroh - Iroh</a></li>
<li><a href="https://github.com/Mesh-LLM/mesh-llm">GitHub - Mesh-LLM/mesh-llm: Distributed AI/LLM for the people ...</a></li>
<li><a href="https://www.iroh.computer/blog/v1">Iroh 1.0 - Dial Keys, not IPs - Iroh</a></li>

</ul>
</details>

**社区讨论**: 社区评论对小型模型的分布式推理表示兴趣，并对消费级网络上的性能表示怀疑。一位贡献者提到了 skippy 引擎，并确认在 2 个节点上对 Qwen 235B MoE 达到 16 tok/s。

**标签**: `#distributed computing`, `#LLM inference`, `#peer-to-peer`, `#AI infrastructure`, `#iroh`

---

<a id="item-10"></a>
## [智谱创始人启动“摸高计划”攻关 AGI](https://mp.weixin.qq.com/s/3CQSkf_kBnXiCDgS4L-Cgg) ⭐️ 7.0/10

智谱 AI 创始人唐杰宣布启动“摸高计划”，投入百亿级资源攻坚机械可解释性，推动黑盒模型透明化。该计划将通往 AGI 的路径概括为四座高峰：长程任务、自治智能体系统、完全自我训练和极致安全治理。 这一举措标志着中国 AI 领域从短期商业变现向基础 AGI 研究的重大转变。机械可解释性的突破有望带来更安全、更可控的 AI 系统，惠及整个开源社区。 智谱的 GLM-5.2 模型被认为接近海外最前沿模型能力，并因其开源特性在技术社群中受欢迎。公司计划投入百亿级资源专门攻坚机械可解释性，旨在打开大语言模型的“黑箱”。

telegram · zaihuapd · 7月11日 13:59

**背景**: 机械可解释性旨在通过分析神经元和特征等内部组件，理解神经网络如何产生特定输出。当前大语言模型常被视为“黑箱”，因为其决策过程不透明，即使模型权重开源也是如此。智谱 AI 是中国领先的 AI 公司，以其开源的 GLM 系列模型而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/32774980722">2030年的大模型将会是什么样的？机械可解释性又是什么？</a></li>
<li><a href="https://www.zyxy.net/archives/24191">机械可解释性（Mechanistic Interpretability）：利用稀疏自编码器（S...</a></li>
<li><a href="https://www.bestblogs.dev/article/81379ea0">致开发者： GLM - 5 . 2 全量开放，前沿 智 能属于所有人 | BestBlogs.dev</a></li>

</ul>
</details>

**标签**: `#AGI`, `#AI research`, `#智谱`, `#mechanical interpretability`, `#open source`

---

<a id="item-11"></a>
## [Claude Code 桌面版新增内置浏览器](https://x.com/ClaudeDevs/status/2075635283211772279) ⭐️ 7.0/10

Claude Code 桌面版现已内置浏览器，用户可以直接在应用内打开和交互网站，例如阅读文档、查看设计稿或测试本地开发服务器。 该功能消除了在 IDE 和外部浏览器之间切换的需要，让 Claude 能够实时访问网络资源，从而简化 AI 辅助编程工作流，提升开发效率。 内置浏览器采用沙盒设计以确保安全，用户可配置是否保留浏览会话。它支持点击和交互网页，体验与操作本地开发服务器类似。

telegram · zaihuapd · 7月11日 14:34

**背景**: Claude Code 桌面版是一款提供 AI 辅助软件开发专用环境的桌面应用，包含 Chat、Cowork 和 Code 三个选项卡。新增的内置浏览器扩展了其能力，允许 Claude 直接获取和交互在线资源，特别适用于阅读 API 文档或预览网页设计等任务。沙盒是一种安全技术，通过隔离浏览器进程来防止恶意内容影响主机系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/zh-CN/desktop">Desktop application - Claude Code Docs</a></li>
<li><a href="https://code.claude.com/docs/en/desktop">Desktop application - Claude Code Docs</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/519213813">浏览器沙盒--它是什么，我们为什么需要它？ - 知乎 如何在谷歌浏览器中使用安全沙箱 - CSDN博客 沙盘 (Sandboxie)64位5.64.3-沙盘 (Sandboxie)官方最新下载_3DM软件 沙盒浏览器 - Windows官方下载 | 微软应用商店 | Microsoft Store 浏览器沙箱（sandBox）到底是什么？ - 知乎 沙盘双开器下载-Sandboxie（沙盘双开器）正式版下载 [电脑版]-pc下载...</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI辅助编程`, `#桌面版更新`, `#浏览器集成`

---

<a id="item-12"></a>
## [谷歌反对欧洲网站屏蔽，美国反盗版立法加速](https://torrentfreak.com/google-opposes-site-blocking-in-europe-as-u-s-piracy-blocking-plans-gain-momentum/) ⭐️ 7.0/10

谷歌正式向欧盟委员会提交文件，反对扩大网站屏蔽措施，称屏蔽 DNS 解析器、IP 地址和 VPN 的做法无效且不成比例，经常误伤合法服务。与此同时，美国国会也在推进类似的反盗版立法，众议员 Issa 计划推动网站屏蔽法案。 这凸显了全球范围内关于互联网审查和反盗版执法的辩论日益激烈，谷歌等大型科技公司反对广泛的屏蔽措施。其结果可能影响互联网基础设施、数字权利以及全球在线盗版问题的解决方式。 谷歌在文件中引用了意大利反盗版系统的例子，该系统曾误封 Google Drive 子域名以及托管 4200 万域名的 Cloudflare IP 地址。谷歌尚未对美国立法计划公开表态，但其欧盟文件主张应专注于提供更好的合法替代服务，而非扩大屏蔽。

telegram · zaihuapd · 7月11日 15:10

**背景**: 网站屏蔽是指互联网服务提供商或 DNS 提供商阻止访问特定网站，常用于打击盗版。DNS 解析器将域名转换为 IP 地址；屏蔽它们可能会干扰对许多网站的访问。误封（overblocking）是指合法服务与侵权服务一起被意外屏蔽。

**标签**: `#site blocking`, `#Google`, `#anti-piracy`, `#internet policy`, `#legislation`

---

<a id="item-13"></a>
## [强脑科技押注可穿戴脑机接口，无需开颅](https://www.cnbc.com/2026/07/11/chinas-brainco-bets-on-wearable-brain-tech.html) ⭐️ 7.0/10

中国脑机接口公司强脑科技（BrainCo）专注于非侵入式可穿戴脑机接口，利用干电极和人工智能解码微弱的脑电信号，目标涵盖假肢、医疗领域，并最终进入消费电子市场。 这种方法提供了一种比 Neuralink 等侵入式脑机接口更安全、更易获取的替代方案，可能加速在医疗康复和消费健康领域的应用。同时，这也凸显了中国在全球脑机接口产业中日益重要的作用。 强脑科技拥有 FDA 批准的仿生手，可读取截肢者的神经肌电信号，以及一款利用低频电脉冲辅助睡眠的设备。该公司计划将其脑机接口平台授权给其他企业，作为未来的主要收入来源。

telegram · zaihuapd · 7月11日 15:49

**背景**: 脑机接口（BCI）实现大脑与外部设备之间的直接通信。非侵入式 BCI 使用放置在头皮上的传感器检测脑电信号，这些信号微弱且嘈杂，需要先进的信号处理和人工智能解码。干电极无需导电凝胶，提高了舒适性和可用性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wearablesensing.com/">Home - Wearable Sensing | Dry EEG</a></li>
<li><a href="https://www.nature.com/articles/s42003-025-08511-z">Progress, challenges and future of linguistic neural decoding ...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12791105/">Non-Invasive Brain-Computer Interfaces: Converging Frontiers ...</a></li>

</ul>
</details>

**标签**: `#brain-computer interface`, `#non-invasive BCI`, `#AI`, `#prosthetics`, `#wearable tech`

---

<a id="item-14"></a>
## [欧盟拟对大型科技公司消费者保护失职处以罚款](https://www.ft.com/content/25640be5-a5bd-4548-81f9-bd0e16f87f35) ⭐️ 7.0/10

欧盟司法专员 Michael McGrath 宣布，欧盟委员会计划在今年年底前提出加强在线消费者保护的新规则，打击成瘾性设计、订阅陷阱及其他暗黑模式。欧盟还希望获得对跨境系统性案件的执法权，可对大型科技公司处以罚款。 这标志着监管力度的显著升级，可能迫使大型科技平台重新设计用户界面和商业实践以避免高额罚款。新规还将消费者保护扩展到现有数字法规之外，可能影响小型在线商家和游戏开发商。 McGrath 指出，目前由成员国执行的消费者保护规则从未导致罚款，不足以威慑违法行为。欧盟同时也在辩论是否对年轻用户实施社交媒体禁令。

telegram · zaihuapd · 7月12日 06:25

**背景**: 暗黑模式是一种用户界面设计，旨在欺骗用户执行非本意的操作，例如进行非自愿购买或注册重复订阅。成瘾性设计指无限滚动、推送通知和可变奖励等功能，这些功能被有意设计以最大化用户参与度，往往以用户福祉为代价。欧盟一直处于数字平台监管的前沿，已通过《数字服务法》和《数字市场法》等法律对大型科技公司施加义务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dark_pattern">Dark pattern - Wikipedia</a></li>
<li><a href="https://commission.europa.eu/topics/consumers/consumer-rights-and-complaints/enforcement-consumer-protection_en">Enforcement of consumer protection - European Commission</a></li>

</ul>
</details>

**标签**: `#EU regulation`, `#consumer protection`, `#big tech`, `#dark patterns`, `#online safety`

---

<a id="item-15"></a>
## [微软和谷歌支持 Go 语言用于 AI 智能体](https://news.google.com/rss/articles/CBMiYkFVX3lxTE10ZkNTb0tGVnFXQVRyMWttSkdNekIwLW4yeWhseV9nVkliZkxYV0JjY29NN2NBX3QxMGdTYURWekFZVGhVN1ZQWHhFd0NvVl81LU1jYmxyb0tKSTZRbGdVdmZ3?oc=5) ⭐️ 7.0/10

微软已加入谷歌的行列，支持使用 Go 编程语言开发 AI 智能体，而 OpenAI 和 Anthropic 尚未采用。 主要科技公司在 AI 智能体开发上对齐 Go 语言，标志着行业潜在转变，因为 Go 的性能和并发特性可能为智能体工作负载提供优于 Python 的优势。 该消息来自 The New Stack 的报道，指出 Go 的高效和简洁使其对构建可扩展的 AI 智能体具有吸引力，但 OpenAI 和 Anthropic 仍依赖 Python。

google_news · The New Stack · 7月11日 14:04

**背景**: AI 智能体是使用 AI 执行任务的自主系统，通常需要高并发和低延迟。Go 由谷歌开发，以其快速编译、用于并发的 goroutine 和易于部署而闻名，使其成为智能体基础设施的有力候选。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pub.huizhou92.com/why-go-might-be-a-better-language-than-python-for-ai-agent-development-722119dd9028">Why Go Might Be a Better Language Than Python for AI Agent ...</a></li>

</ul>
</details>

**标签**: `#Go`, `#AI agents`, `#Microsoft`, `#Google`, `#programming languages`

---