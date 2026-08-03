---
layout: default
title: "Horizon Summary: 2026-08-03 (ZH)"
date: 2026-08-03
lang: zh
---

> 从 24 条内容中筛选出 11 条重要资讯。

---

1. [Karpathy 点赞 sqliteai/waste：在笔记本上流式运行 2.78T 参数的 Kimi K3](#item-1) ⭐️ 8.0/10
2. [Qwen3.8-Max：开放权重的新旗舰模型](#item-2) ⭐️ 8.0/10
3. [Kakehashi：实验性用户空间在 Linux ARM 上运行 macOS 二进制文件](#item-3) ⭐️ 8.0/10
4. [SwiftUI 七年：对其平庸的批判性审视](#item-4) ⭐️ 8.0/10
5. [OpenAI 将 GPT-5.6 价格下调高达 80%](#item-5) ⭐️ 8.0/10
6. [中国 AI 三连发：MiniMax H3、Seedance 2.5、DeepSeek V4 同日发布](#item-6) ⭐️ 8.0/10
7. [Isopolis：基于谷歌 3D 瓦片的旧金山等距像素地图](#item-7) ⭐️ 7.0/10
8. [英语学习者核心词汇的变迁（1953–2023）](#item-8) ⭐️ 7.0/10
9. [Jira 旨在成为 AI 编码代理的控制平面](#item-9) ⭐️ 7.0/10
10. [DeepSeek 智能体发起自主网络攻击](#item-10) ⭐️ 7.0/10
11. [OpenAI 推出 Daybreak，以对抗 Claude Mythos 并加强软件安全](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Karpathy 点赞 sqliteai/waste：在笔记本上流式运行 2.78T 参数的 Kimi K3](https://github.com/sqliteai/waste) ⭐️ 8.0/10

Andrej Karpathy 在 GitHub 上为 sqliteai/waste 项目点了星，该项目引入了一个无依赖的 C 推理引擎，通过从 NVMe 流式传输激活的权重，在超出可用内存的情况下运行完整的 2.78 万亿参数 Kimi K3 模型。这使得该巨型模型可以在笔记本电脑上运行。 这位极具影响力的 AI 人物的认可，突显了一种在消费级硬件上运行最先进模型的新方法，可能使大规模 AI 的获取更加民主化。这可能推动行业转向更高效、内存受限的推理解决方案，并减少对大规模云集群的依赖。 该引擎可嵌入，用 C 语言编写，包含 23 个 C 文件、17 个 Python 文件和 3 个 shell 脚本，采用 Apache 2.0 许可证。它直接从 NVMe 流式传输激活的权重，从而在内存限制之外进行推理，归属于 SQLite Cloud, Inc.。

github · karpathy · 8月2日 17:19

**背景**: SQLite 是一种广泛使用的嵌入式数据库，sqliteai 组织正在为其探索 AI 原生扩展，例如设备端推理和智能体能力。WASTE 引擎代表了数据库与 AI 技术的融合，通过利用存储带宽而非内存容量，使大型语言模型能够在本地硬件上高效运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/sqliteai/waste">GitHub - sqliteai/waste: Run the full 2.78-trillion-parameter Kimi K3 model beyond available RAM by streaming activated weights directly from NVMe. A dependency-free, embeddable C inference engine. · GitHub</a></li>
<li><a href="https://huggingface.co/moonshotai/Kimi-K3/discussions/148">moonshotai/Kimi-K3 · Waste engine: Run the full 2.78T-parameter Kimi K3 on a laptop</a></li>
<li><a href="https://marcobambini.substack.com/p/the-waste-inference-engine">The WASTE inference engine - Marco Bambini</a></li>

</ul>
</details>

**社区讨论**: Hugging Face 和 Substack 上的社区讨论对该项目的潜力表示兴奋，一位评论者指出与他们自己的开源工作有协同效应。独立代码审计以及在笔记本电脑上运行 2.78T 模型的能力被强调为重大成就。

**标签**: `#AI`, `#SQLite`, `#GitHub`, `#Karpathy`, `#Open Source`

---

<a id="item-2"></a>
## [Qwen3.8-Max：开放权重的新旗舰模型](https://qwen.ai/blog?id=qwen3.8) ⭐️ 8.0/10

阿里巴巴的 Qwen 团队发布了 Qwen3.8-Max，这是一个拥有 2.4 万亿参数的混合专家（MoE）旗舰模型，并宣布计划在下周开源其权重，这标志着 Qwen-Max 级别的模型首次以开放权重形式发布。 此次发布可能对 AI 生态系统产生重大影响，因为它提供了一个顶级的开放权重模型，有望与 Fable 5 等专有模型竞争，并使开发者能够在本地运行先进的 AI。这也标志着行业向开放发展的趋势，可能影响监管讨论和竞争格局。 Qwen3.8-Max 采用混合专家架构，拥有 2.4 万亿参数，公司声称其性能“仅次于 Fable 5”。然而，目前尚未发布基准测试表、许可证或独立评估，开放权重将于下周提供。

hackernews · ai2027 · 8月3日 02:16 · [社区讨论](https://news.ycombinator.com/item?id=49150470)

**背景**: 开放权重模型允许用户下载并在本地运行，但与完全开源模型不同，其许可证可能限制使用方式。Qwen 一直是开放权重 LLM 领域的重要参与者，之前的模型如 Qwen3.6-27B 被广泛用于本地应用。Qwen3.8-Max 以开放权重发布，可能为可访问的高性能 AI 树立新标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eesel.ai/blog/qwen38-max-review">Qwen 3.8 Max review: Alibaba's 2.4T flagship, tested (2026)</a></li>
<li><a href="https://docs.qwencloud.com/changelog/models">Model releases - QwenCloud</a></li>
<li><a href="https://aitoolsreview.co.uk/insights/qwen-3-8-max">Qwen 3.8 Max Review: Alibaba's 2.4T Model, Tested</a></li>

</ul>
</details>

**社区讨论**: 社区成员对开放权重发布感到兴奋，一位用户指出 Qwen3.6-27B 已经是最好的本地模型之一，希望 3.8 能有所改进。另一位用户表达了对开放权重模型可能被禁止的担忧，其他人则开玩笑谈论市场反应和“cowork”这一术语。

**标签**: `#AI`, `#LLM`, `#open-source`, `#coding`, `#Qwen`

---

<a id="item-3"></a>
## [Kakehashi：实验性用户空间在 Linux ARM 上运行 macOS 二进制文件](https://github.com/wie-project/kakehashi) ⭐️ 8.0/10

Kakehashi，一个实验性的用户空间翻译层，现已拥有可在 Linux ARM64 上原生运行 macOS CLI 二进制文件的工作原型，包括 7-Zip、curl 和 Xcode 的 Git 工具。该项目是开源的，托管在 GitHub 上。 该项目解决了跨平台兼容性中的一个重大技术挑战，有望使 macOS 软件无需虚拟化或模拟即可在 Linux ARM 设备上运行。如果成功，它可能通过提供对 macOS 专属命令行工具的访问，扩展 Linux ARM 生态系统。 当前原型显示，7-Zip 在 8k 文件树上通过了多线程压缩测试，尽管比原生 Linux 执行慢约 5.2 倍，但已有优化计划。curl 在自动化 Docker 测试中通过了 200 多个命令和选项，Xcode 的 Git 工具已具备基本的版本控制功能。

hackernews · vlad_kalinkin · 8月2日 16:26 · [社区讨论](https://news.ycombinator.com/item?id=49145937)

**背景**: 兼容层是一种接口，通过翻译系统调用，使一个操作系统的二进制文件能在另一个操作系统上运行。macOS 二进制文件使用 Mach-O 格式，与 Linux 的 ELF 格式不同，这使得直接执行具有挑战性。像 Darling 这样的项目旨在实现更广泛的 macOS 兼容性，而 Kakehashi 则专注于 ARM64 上的 CLI 工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/wie-project/kakehashi">GitHub - wie-project/kakehashi: Userspace macOS translation ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Compatibility_layer">Compatibility layer - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mach-O">Mach-O - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区表现出浓厚兴趣，一位评论者提到 Darling 项目并建议潜在合作，另一位则持谨慎乐观态度，指出该项目仍处于早期阶段。还有对项目名称的幽默批评，以及一个技术问题，询问基于 ROM 的方法是否能简化设计。

**标签**: `#macOS compatibility`, `#Linux ARM`, `#userspace`, `#reverse engineering`, `#open source`

---

<a id="item-4"></a>
## [SwiftUI 七年：对其平庸的批判性审视](https://ykvm.com/2026/07/swiftui-a-story-of-mediocrity/) ⭐️ 8.0/10

ykvm.com 上发布的一篇批评性文章指出，经过七年发展，SwiftUI 在复杂 UI 方面仍然平庸，并认为在性能关键任务中仍需使用 UIKit。该文章引发了包含 127 条评论的广泛社区讨论。 这一分析对苹果开发者意义重大，因为它挑战了 SwiftUI 是 UI 开发未来的假设。它指出了持续存在的性能和复杂性问题，可能影响框架的采用和开发策略。 文章指出，虽然 SwiftUI 适合简单 UI，但复杂且性能优先的应用仍应依赖 UIKit。社区评论也呼应了这一观点，开发者指出在高级任务中需要降级使用 UIKit、Metal 或 Core Animation。

hackernews · mpweiher · 8月2日 18:59 · [社区讨论](https://news.ycombinator.com/item?id=49147263)

**背景**: SwiftUI 是苹果于 2019 年推出的声明式 UI 框架，旨在取代命令式的 UIKit。虽然它提供了响应式数据流和跨平台支持等现代特性，但在复杂界面中一直面临性能和局限性的批评。UIKit 仍然是许多开发者的成熟可靠选择，尤其是在性能关键的应用中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sevensquaretech.com/swiftui-vs-uikit-detailed-comparison/">SwiftUI vs UIKit in 2025: Best Framework for iOS Apps</a></li>
<li><a href="https://7span.com/blog/swiftui-vs-uikit">SwiftUI vs UIKit in 2026: UI Framework Comparison for iOS ...</a></li>
<li><a href="https://trysonar.app/blog/swiftui-vs-uikit-2026-when-each-wins">SwiftUI vs UIKit in 2026: When Each Wins | Sonar Blog</a></li>

</ul>
</details>

**社区讨论**: 社区评论既有赞同也有细微差别。一些开发者分享了实用策略，如对简单 UI 使用 SwiftUI，对复杂任务使用 UIKit，而另一些人则质疑纯声明式响应式框架是否适合通用原生 UI。还有人担心苹果在现有框架之外进行创新的能力。

**标签**: `#SwiftUI`, `#UIKit`, `#Apple`, `#UI frameworks`, `#software development`

---

<a id="item-5"></a>
## [OpenAI 将 GPT-5.6 价格下调高达 80%](https://news.google.com/rss/articles/CBMickFVX3lxTFBUZmU3akRYZVJ4ZWZyZnlIejMtODRiRmFUZWpnNGo4amllaFJXdDdjTTFnX01MT19yMThNZGxVMnVidm9VSk1Bd2NaV1IwenAteVl2dHcwYzVaaHZoSzVoTUtYbHVYRU9KaWpNejlzUW96UQ?oc=5) ⭐️ 8.0/10

OpenAI 已将其 GPT-5.6 模型的价格下调高达 80%，具体将 Luna 定价削减 80%，Terra 削减 20%，并在 API 中引入了更快的 Sol 模式。 这一大幅降价使长期运行的 AI 智能体更具成本效益和实用性，促进了在企业工作流程和软件工程中的更广泛应用。这也加剧了 AI 模型市场的竞争，可能迫使竞争对手调整其定价策略。 降价适用于特定的 GPT-5.6 变体：Luna（削减 80%）和 Terra（削减 20%），同时 API 中新增了更快的 Sol 模式。此外，两个未标记的 OpenAI 检查点 Zinc 和 Magnesium 出现在 DesignArena 上，暗示了未来的发布。

google_news · Memeburn · 8月2日 14:28

**背景**: GPT-5.6 是 OpenAI 的大型语言模型，提供多种变体（Luna、Terra、Sol），具有不同的性能和定价层级。长期运行的 AI 智能体是长时间运行的系统，通常需要持续的 API 调用，因此成本是实际部署的关键因素。检查点（checkpointing）和上下文滚动（context rollover）等技术帮助这些智能体在会话间保持状态，但更低的 token 成本直接降低了运营费用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/">Advancing the price -performance frontier with GPT - 5 . 6 | OpenAI</a></li>
<li><a href="https://www.youtube.com/watch?v=wlOIQ266b6Q">GPT 5 . 6 Sol Fast Mode, OpenAI Cut Prices 80% and GLM... - YouTube</a></li>
<li><a href="https://artificialanalysis.ai/models/gpt-5-6-terra-xhigh">GPT - 5 . 6 Terra (xhigh) - Intelligence, Performance & Price Analysis</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.6`, `#pricing`, `#AI agents`, `#cost reduction`

---

<a id="item-6"></a>
## [中国 AI 三连发：MiniMax H3、Seedance 2.5、DeepSeek V4 同日发布](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5xSW9FNF9GS1h0d2VEMl80S3hTbnBmN1l3b1prVG1OTXZUVzMwUzJCVi1PRlJMOTZObzhDRmkxWlR2a2NXNThORnNMdm9JT1hEYkxj?oc=5) ⭐️ 8.0/10

同一天，中国 AI 公司 MiniMax、字节跳动和 DeepSeek 分别发布了各自的最新大模型：MiniMax H3、Seedance 2.5 和 DeepSeek V4。这标志着中国本土 AI 发展的一个重要里程碑，展示了快速的进步和激烈的竞争。 同日发布多款先进模型，凸显了中国在 AI 领域加速发展的能力，以及其在基础模型方面与全球竞争的雄心。这标志着国内竞争与创新的新阶段，可能重塑全球 AI 格局。 MiniMax H3 是一个开放权重的全模态生成模型，能在统一上下文中理解和生成文本、图像、视频和音频，可生成 15 秒 2K 视频并带有原生立体声。Seedance 2.5 是字节跳动 Seed 团队的新一代视频生成模型，基于 Seedance 2.0 的统一多模态架构。DeepSeek V4 提供 V4-Pro 和 V4-Flash 两个版本，支持 1M 上下文，并提供兼容 OpenAI/Anthropic 的接口；V4-Pro 是混合专家模型，总参数 1.6T，激活参数 49B。

google_news · 36 Kr · 8月3日 00:11

**背景**: 中国一直在快速推进其大型 AI 模型，DeepSeek、MiniMax 和字节跳动等公司不断突破多模态理解和生成的边界。这些模型是中国企业日益与西方同行在 AI 研究和应用领域竞争的大趋势的一部分。三款主要模型的同时发布，凸显了中国在 AI 自主创新方面的决心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between Tasks and Modalities - MiniMax Research | MiniMax</a></li>
<li><a href="https://www.marktechpost.com/2026/08/01/minimax-releases-minimax-h3-an-omni-modal-video-model-that-generates-15-second-2k-clips-with-native-stereo-audio/">MiniMax Releases MiniMax H3: An Omni-Modal Video Model That Generates 15-Second 2K Clips With Native Stereo Audio - MarkTechPost</a></li>
<li><a href="https://deepseekv4.dev/">DeepSeek V 4 : Future-Ready Reasoning for Teams</a></li>

</ul>
</details>

**标签**: `#AI`, `#China`, `#Large Language Models`, `#DeepSeek`, `#MiniMax`

---

<a id="item-7"></a>
## [Isopolis：基于谷歌 3D 瓦片的旧金山等距像素地图](https://sf.isopolis.city/) ⭐️ 7.0/10

一个名为 Isopolis（sf.isopolis.city）的新项目展示了旧金山的等距像素地图，该地图基于谷歌真实感 3D 瓦片生成。创作者使用 Claude Code 构建了一个爬虫，用于流式传输 3D 瓦片并用 three.js 渲染，从而生成了城市风格化的像素艺术视图。 该项目展示了谷歌真实感 3D 瓦片的创新应用，将现代 3D 数据与经典像素艺术美学相结合。它证明了 AI 辅助编程和公共 3D 数据集的易用性如何促成创意可视化，并可能激发其他城市的类似项目。 该地图基于谷歌真实感 3D 瓦片构建，这些瓦片为人口稠密地区提供高分辨率 3D 数据。开发者最初探索了美国政府免费的 LIDAR 数据，但发现谷歌的 3D 瓦片纹理质量更好；渲染流程使用 three.js 和用 Claude Code 创建的自定义爬虫。

hackernews · nuwandavek · 8月3日 00:46 · [社区讨论](https://news.ycombinator.com/item?id=49149966)

**背景**: 等距像素艺术是一种使用等距投影（无消失点）来创建 3D 物体的 2D 表示的风格，常用于游戏和插画。谷歌真实感 3D 瓦片是谷歌地图瓦片 API 的一部分，提供真实世界位置的高分辨率 3D 网格，开发者可用于沉浸式可视化。该项目结合这些技术，创建了旧金山独特的可探索地图。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.google.com/maps/documentation/tile/3d-tiles">Photorealistic 3D Tiles | Google Maps Tile API | Google for Developers</a></li>
<li><a href="https://mapsplatform.google.com/maps-products/map-tiles/">2D, 3D, and Street View Map Tiles - Google Maps Platform</a></li>
<li><a href="https://pixelparmesan.com/blog/fundamentals-of-isometric-pixel-art">Fundamentals of Isometric Pixel Art - Pixel Parmesan</a></li>

</ul>
</details>

**社区讨论**: 社区对该项目的视觉吸引力和技术执行表示赞赏，一位用户指出制作好的等距地图难度很大。一些用户指出了 AI 生成的异常，例如道路看起来像河流以及不存在的池塘，而其他人则将其与 Isometric.nyc 和 Floor796 等类似项目进行比较。开发者分享了幕后细节，包括使用谷歌 3D 瓦片和 Claude Code。

**标签**: `#isometric`, `#pixel art`, `#3D tiles`, `#San Francisco`, `#visualization`

---

<a id="item-8"></a>
## [英语学习者核心词汇的变迁（1953–2023）](https://pudding.cool/2026/07/essential-words/) ⭐️ 7.0/10

The Pudding 发布了一项数据驱动分析，展示了 1953 年至 2023 年间英语学习者核心词汇的变化，揭示了词汇的大幅更替以及从人际美德向抽象社会概念的转变。 这很重要，因为它反映了更广泛的社会和文化变迁，并对教育者和课程设计者具有实际意义，他们需要使教材与当前的沟通需求保持一致。该分析还引发了关于语言教学如何适应不断变化的价值观和现实的讨论。 分析发现，虽然“社会交际”层面的词汇数量基本不变，但到 2023 年，1953 年词汇中近四分之一已消失，而 2023 年词汇中有 39%是新词。像“humble”、“loyalty”和“generous”等词被“community”、“identity”和“narrative”等词取代，表明从紧密的人际关系转向更抽象、更遥远的归属形式。

hackernews · c-oreills · 8月2日 15:41 · [社区讨论](https://news.ycombinator.com/item?id=49145590)

**背景**: 这篇文章基于对七十年间英语教学中使用的词汇表的分析。它可能参考了诸如《通用词汇表》或类似资源的标准词汇列表，追踪核心词汇选择的变化。这不仅反映了语言的变化，也反映了社会的优先事项，因为语言教学往往反映学习者的文化和实际需求。

**社区讨论**: 评论强调了词汇选择的主观性，一位用户指出“正确”的词汇取决于学习者的目标（如旅行、看电视或读报纸）。另一位评论者将“humble”等词向“identity”的转变与不平等加剧和部落化联系起来，还有人分享了个人学习经历，并批评了文章的滚动设计。

**标签**: `#linguistics`, `#education`, `#data analysis`, `#language learning`, `#societal change`

---

<a id="item-9"></a>
## [Jira 旨在成为 AI 编码代理的控制平面](https://news.google.com/rss/articles/CBMiigFBVV95cUxNaXVHcFJpNzJqQzhOaFBoZjVTQ2lOT29ySDZ2bXhubW0zYm5aZnpjcnJNQkpWcTZTeXZ1R0xzY1NzTkFEc3M0OEx4NmwyZjJUZzY0SjFlQzRwRTAyNlIxbUl2MldBeTNXdmYxekwxX2tBMF80eXNFelBiQmNKVEZmcVFpSDlHZjRDa3c?oc=5) ⭐️ 7.0/10

Atlassian 宣布 Jira 将作为 AI 编码代理的编排中心，付费客户可以直接将工作项分配给 Claude Code、Cursor 和 GitHub Copilot 等工具，无需额外费用。此外，每个付费计划都将包含一个内置编码代理，可将工单转换为拉取请求。 此举将 Jira 定位为管理 AI 驱动开发工作流的核心平台，可能影响 AI 工具与项目管理集成的方式。它可能通过简化规划与编码之间的交接，显著影响软件工程团队，并可能影响 AI 辅助开发的更广泛行业趋势。 该集成原生支持 GitHub Copilot、Cursor 和 Claude Code，并且 Jira Automation 正在扩展为 AI 代理的开放控制平面。该公告于 2026 年 7 月 15 日发布，适用于付费的 Jira Cloud 计划。

google_news · HackerNoon · 8月2日 17:19

**背景**: AI 编码代理是能够自主执行编码任务的软件工具，例如生成代码、修复错误或创建拉取请求，通常由自然语言提示触发。Jira 是软件团队常用的项目管理工具，用于跟踪问题和规划迭代。通过集成这些代理，Jira 旨在弥合项目规划与代码执行之间的差距，实现更自动化和事件驱动的开发工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://yusmpgroup.com/news/jira-ai-coding-agents-orchestration">Jira Becomes AI Coding-Agent Control Plane | YuSMP</a></li>
<li><a href="https://www.atlassian.com/blog/development/scale-agent-impact-with-jira-automation">From prompts to orchestration: Scale AI coding agent impact ...</a></li>
<li><a href="https://support.atlassian.com/jira-software-cloud/docs/work-with-ai-agents-in-jira/">Work with AI agents in Jira - Jira Cloud | Atlassian Support</a></li>

</ul>
</details>

**标签**: `#AI`, `#Jira`, `#software engineering`, `#project management`, `#AI agents`

---

<a id="item-10"></a>
## [DeepSeek 智能体发起自主网络攻击](https://news.google.com/rss/articles/CBMigwFBVV95cUxNUGZnWFJyS1lBTGZuVjFlWmhfSmlvc3BSaDlVZFJYbmkzdXlpRmtCQmpPd2VuNlNxU2Utb1l5ZkIzaks1U0MxbHowbUJON3ZWTlJtQmUwS2l4cnN3d19NWFUxOFkxUWpsZGhXY0NpTGJ2SENPZlc0MTNkR1dtb19EeHJNTQ?oc=5) ⭐️ 7.0/10

一名中文威胁行为者利用 DeepSeek AI 模型结合开源 Hermes Agent，对暴露的服务器发起自主网络攻击，人工参与有限。攻击由 DeepSeek 作为主要推理引擎进行编排，而 Hermes Agent 负责终端访问、任务自动化和可复用攻击模块。 这标志着 AI 驱动的网络安全威胁迈出了重要一步，表明自主代理可以在最少人工干预的情况下进行攻击。它凸显了国家行为体和恶意行为者扩大进攻行动的潜力，提高了网络攻击的节奏和范围，并强调了针对 AI 驱动威胁采取防御措施的紧迫性。 DeepSeek 识别出 Langflow 漏洞（CVE-2026-33017，CVSS 9.8），并自主尝试通过从 GitHub 下载公开 PoC 漏洞利用代码进行攻击。该活动涉及对七个漏洞的自主 AI 扫描，并在某些阶段进行手动利用，Palo Alto Networks Unit 42 对此进行了详细说明。

google_news · varindia.com · 8月2日 05:47

**背景**: 自主网络攻击利用 AI 代理进行侦察、选择目标并执行漏洞利用，只需最少的人工监督。DeepSeek 模型由一家中国 AI 公司开发，充当推理引擎，而 Hermes Agent 是一个开源工具，可自动化终端操作。这一发展之前已有 AI 代理驱动大规模自主攻击的报道，表明 AI 驱动的威胁正朝着更复杂的方向发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.varindia.com/news/deepseek-agent-launches-autonomous-cyberattacks">DeepSeek Agent Launches Autonomous Cyberattacks</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/hacker-uses-deepseek-ai-to-autonomously-attack-vulnerable-servers/">Hacker uses DeepSeek AI to autonomously attack vulnerable servers</a></li>
<li><a href="https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/">Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks</a></li>

</ul>
</details>

**标签**: `#AI`, `#cybersecurity`, `#autonomous agents`, `#DeepSeek`

---

<a id="item-11"></a>
## [OpenAI 推出 Daybreak，以对抗 Claude Mythos 并加强软件安全](https://news.google.com/rss/articles/CBMivAFBVV95cUxQSTdxeEN3VHg0ZnB0aF9FenVicjI2MlJDVW5KYjlLUGUzU09WTDlsdElhUzFmOGdTdmdjMThHd0t3TE5BQjNUcmZpLTlxSG1CS0k0YlktWEdjdEE1RnlIMlNBYXpwMnhmYXN6bWZFd1hTbTc0enNWbkpwOFhjODc5cUc2VlBYNTNLZDFrUVIyUEtQVjBDdFJPd09BMHNJalhOWHkzazZ3OW9uSmhqYV9EQ0hnQThhYTZYdEx3eA?oc=5) ⭐️ 7.0/10

OpenAI 推出了 Daybreak，这是一套网络安全工具，包括 Codex Security 和 GPT-5.5-Cyber，旨在帮助组织大规模发现、验证和修补漏洞。此次发布被视为对 Anthropic 的 Claude Mythos 的直接回应，后者是一款具有先进漏洞发现能力的强大模型。 此举加剧了 OpenAI 与 Anthropic 在人工智能驱动的网络安全领域的竞争，可能加速人工智能在防御性安全领域的应用。同时，它也回应了人们对人工智能在发现和利用软件漏洞方面作用的日益担忧，OpenAI 将 Daybreak 定位为以防御者为中心的解决方案。 Daybreak 强调授权、人工判断、监控、安全防护以及与安全社区的合作。通过 Trusted Access for Cyber，经过验证的防御者可以获得高级访问权限，该计划将更强大的工具与更严格的验证和监督相结合。此次发布紧随 Anthropic 于 2026 年 6 月发布 Claude Mythos 5 和 Fable 5 之后。

google_news · آي-فون إسلام · 8月2日 08:39

**背景**: Claude Mythos 是 Anthropic 的一系列大型语言模型，以其出色的软件漏洞发现能力而闻名。出于安全考虑，Anthropic 最初未向公众开放 Mythos，但后来发布了受限版本 Claude Mythos 5，以及更安全的“Mythos 级”模型 Claude Fable 5。OpenAI 的 Daybreak 旨在提供类似的防御能力，但侧重于赋能安全专业人员，而不仅仅是展示原始模型能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/daybreak/">Daybreak | OpenAI for cybersecurity</a></li>
<li><a href="https://openai.com/index/daybreak-securing-the-world/">Daybreak: Tools for securing every organization in the world</a></li>
<li><a href="https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html">OpenAI Launches Daybreak for AI-Powered Vulnerability ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI`, `#software security`, `#product launch`

---