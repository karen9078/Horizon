---
layout: default
title: "Horizon Summary: 2026-08-26 (ZH)"
date: 2026-08-26
lang: zh
---

> 从 41 条内容中筛选出 15 条重要资讯。

---

1. [OpenAI 的 Jalapeño 芯片在测试中超越 Nvidia Blackwell](#item-1) ⭐️ 9.0/10
2. [苹果发布 M6 和 M5 Ultra 芯片，性能和 AI 计算大幅提升](#item-2) ⭐️ 8.0/10
3. [FDA 批准首款可穿戴双葡萄糖-酮体监测仪](#item-3) ⭐️ 8.0/10
4. [Nitter 和 XCancel 收到停止侵权通知](#item-4) ⭐️ 8.0/10
5. [Firefox 157 将在所有平台默认启用 JPEG XL](#item-5) ⭐️ 8.0/10
6. [EVE Online 开始从 Stackless Python 2.7 迁移到 Python 3](#item-6) ⭐️ 8.0/10
7. [IBM Granite 4.2：采用混合架构的密集推理大语言模型](#item-7) ⭐️ 8.0/10
8. [量化感知修复：4 位模型超越全精度原版](#item-8) ⭐️ 8.0/10
9. [Vercel 保护 Next.js 应用免受 2026 年 8 月 RCE 漏洞影响](#item-9) ⭐️ 8.0/10
10. [Vercel 推出 Run SDK，实现 AI 代理的安全代码执行](#item-10) ⭐️ 8.0/10
11. [OpenAI 首席财务官阐释智能充裕背后的全栈](#item-11) ⭐️ 7.0/10
12. [GitHub 在生产环境中评估 LLM 的经验教训](#item-12) ⭐️ 7.0/10
13. [Vercel Connect 正式发布：为 AI 代理提供运行时作用域凭据](#item-13) ⭐️ 7.0/10
14. [OpenAI 的 Codex 集成 WebMCP 以增强智能体交互](#item-14) ⭐️ 7.0/10
15. [Pi 可扩展工作流：用于多智能体编排的确定性 DSL](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI 的 Jalapeño 芯片在测试中超越 Nvidia Blackwell](https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia) ⭐️ 9.0/10

OpenAI 与博通推出了定制推理芯片 Jalapeño，据称在基准测试中超越了 Nvidia 的 Blackwell，提供了更高的吞吐量和更好的能效。结果于 2026 年 8 月 25 日发布，基于 SemiAnalysis 的 InferenceX 基准测试。 这一进展标志着 AI 推理硬件可能发生范式转变，因为主要 AI 实验室不再完全依赖 Nvidia GPU。如果 OpenAI 的定制芯片在大规模应用中证明可行，可能会加剧竞争并推动 AI 芯片市场的创新，影响 AI 部署的成本和性能。 Jalapeño 专为 LLM 推理设计，注重低延迟和高吞吐量。根据基准测试，它在每用户令牌数和每千瓦吞吐量上均优于当前最先进的处理器，其芯片尺寸与 Nvidia 的 Rubin 相当，但 NVFP4 PFLOPs 仅为后者的三分之一。

hackernews · Semianalysis · 8月25日 14:06 · [社区讨论](https://news.ycombinator.com/item?id=49434378)

**背景**: AI 推理硬件是指用于在新数据上运行已训练 AI 模型的物理基础设施。传统上，Nvidia GPU 主导了这一领域，但像 OpenAI 这样的公司现在正在设计定制 ASIC，以优化其特定工作负载的性能和成本。Jalapeño 芯片正是这一趋势的产物，由 OpenAI 与博通合作开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip | OpenAI</a></li>
<li><a href="https://techcrunch.com/2026/08/25/openais-jalapeno-chip-is-built-for-fast-inference-at-scale-benchmarks-show/">OpenAI’s Jalapeño chip is built for fast inference at scale, benchmarks show | TechCrunch</a></li>
<li><a href="https://openai.com/index/jalapeno-first-results/">Jalapeño’s first results show industry-leading speed and efficiency in AI inference | OpenAI</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映了兴奋和怀疑。一些人将推理芯片的出现与早期 GPU 市场相提并论，而另一些人则质疑 FP4 精度的实用性，并指出人脑仍然高效得多。此外，也有人赞赏 SemiAnalysis 非传统的分析风格。

**标签**: `#AI hardware`, `#OpenAI`, `#Nvidia`, `#chip design`, `#inference`

---

<a id="item-2"></a>
## [苹果发布 M6 和 M5 Ultra 芯片，性能和 AI 计算大幅提升](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/) ⭐️ 8.0/10

2026 年 8 月 25 日，苹果发布了 M6 和 M5 Ultra 芯片，标志着性能和 AI 计算的重大飞跃。M6 是苹果首款 2nm 芯片，配备 12 核 CPU、12 核 GPU 和双 16 核神经引擎，而 M5 Ultra 是苹果有史以来最强大的芯片，采用四芯片架构，包含四个 3nm 芯片和 1.2TB/s 内存带宽。 这一发布意义重大，凸显了苹果在 AI 计算和芯片性能方面的积极进取，可能重塑与高通、英特尔等竞争对手的竞争格局。新芯片预计将为未来的 Mac 提供动力，为用户带来显著的性能提升，并支持设备端更先进的 AI 应用。 M6 采用 2nm 工艺，而 M5 Ultra 通过 UltraFusion 连接四个第三代 3nm 芯片，标志着苹果首次采用四芯片架构。M5 Ultra 在 Mac Studio 上最高支持 512GB 内存和 16TB 存储，顶配价格高达 24,699 美元。

hackernews · interpol_p · 8月25日 13:01 · [社区讨论](https://news.ycombinator.com/item?id=49433292)

**背景**: 苹果芯片是基于 ARM 的片上系统，集成了 CPU、GPU、NPU 和统一内存。M6 和 M5 Ultra 是苹果从 Intel 处理器过渡的一部分，旨在提供更好的性能和能效。M6 的 2nm 工艺代表了制造技术的重大进步，而四芯片的 M5 Ultra 则突破了芯片封装技术的极限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_M6">Apple M 6 - Wikipedia</a></li>
<li><a href="https://xenospectrum.com/en/apple-silicon-chip-architecture/">Apple 's M 6 Chip Debuts 2nm Process, While... | XenoSpectrum</a></li>
<li><a href="https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/">Apple introduces M6 and M5 Ultra for a big leap in ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论既有兴奋也有怀疑。用户 alluro2 称赞了性能提升，而 bayindirh 幽默地将竞争动态比作 90 年代末。一些评论者如 gardaani 讨论了苹果可能跳过 M6 Pro/Max/Ultra 以专注于 AI 能力的 M7 的传闻，mrtksn 则指出了高端配置的高昂价格。

**标签**: `#Apple`, `#hardware`, `#AI compute`, `#chip design`, `#performance`

---

<a id="item-3"></a>
## [FDA 批准首款可穿戴双葡萄糖-酮体监测仪](https://www.fda.gov/news-events/press-announcements/fda-authorizes-first-wearable-device-continuously-monitors-both-ketone-levels-and-blood-sugar) ⭐️ 8.0/10

美国食品药品监督管理局（FDA）已批准雅培公司的 Libre Duo 10 天连续双葡萄糖-酮体监测系统，这是美国首款可连续监测酮体水平的可穿戴设备，也是全球首款在同一设备中同时监测酮体和葡萄糖的设备。 该设备像传统连续血糖监测仪（CGM）一样植入手臂皮下，可提供长达 10 天的读数。它专为糖尿病患者设计，包括使用胰岛素的患者，可能对 DKA 风险人群或使用 SGLT-2 抑制剂的患者特别有用。

hackernews · sunnynagra · 8月25日 19:07 · [社区讨论](https://news.ycombinator.com/item?id=49439017)

**背景**: 连续血糖监测仪（CGM）通过提供实时血糖水平而无需指尖采血，彻底改变了糖尿病护理。酮体是身体分解脂肪供能时产生的物质，水平升高可能表明危险的糖尿病酮症酸中毒（DKA），这是糖尿病的严重并发症。传统上，酮体水平通过尿液或血液检测，但连续监测一直受限。这款新设备将葡萄糖和酮体传感集成到一个可穿戴设备中，提供更全面的代谢状态视图。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fda.gov/news-events/press-announcements/fda-authorizes-first-wearable-device-continuously-monitors-both-ketone-levels-and-blood-sugar">FDA Authorizes First Wearable Device That Continuously ...</a></li>
<li><a href="https://www.pharmacytimes.com/view/fda-clears-first-continuous-glucose-ketone-monitor">FDA Clears First Continuous Glucose-Ketone Monitor</a></li>
<li><a href="https://www.upi.com/Top_News/US/2026/08/25/fda-oks-blood-sugar-ketone-monitor/5521787688375/">FDA approves first wearable device to monitor blood sugar ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映了个人情感、谨慎乐观和技术怀疑的混合。一位用户分享了一位朋友死于 DKA 的感人轶事，并对进展表示感激。另一位用户对无创血糖传感表示怀疑，但欢迎为 1 型糖尿病患者提供额外工具，并希望改善报销。一位最近使用类似设备（Stelo）的用户指出植入无痛。一些人质疑“可穿戴”一词，因为它是皮下植入的，还有人指出酮体监测可能只对血糖控制极差或极好的患者有用，对普通糖尿病患者用处不大。

**标签**: `#FDA`, `#wearable`, `#diabetes`, `#health tech`, `#medical devices`

---

<a id="item-4"></a>
## [Nitter 和 XCancel 收到停止侵权通知](https://github.com/zedeus/nitter/issues/1442) ⭐️ 8.0/10

Nitter 和 XCancel 是流行的 X/Twitter 隐私保护前端，它们收到了停止侵权通知，导致所有 Nitter 实例暂时关闭。开发者正在等待法律建议，这些工具的未来充满不确定性。 这一法律行动威胁到允许用户无需登录或跟踪即可浏览 X/Twitter 的工具的可用性，影响了注重隐私的用户和开源社区。它还引发了对类似项目法律保护的担忧，以及更广泛的互联网自由斗争。 Nitter 和 XCancel 都收到了停止侵权通知，但具体细节很少。Nitter 开发者表示，在寻求法律建议期间，所有实例将在可预见的未来保持关闭。

hackernews · Banditoz · 8月25日 17:08 · [社区讨论](https://news.ycombinator.com/item?id=49437283)

**背景**: Nitter 是一个免费开源的 Twitter 替代前端，专注于隐私和性能，允许用户在没有 JavaScript、跟踪或账户的情况下浏览推文。XCancel 是一个类似的第三方界面，允许用户无需登录即可查看 X 内容。这些工具在希望避免 X 的登录墙和数据收集行为的用户中很受欢迎。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nitter">Nitter - Wikipedia</a></li>
<li><a href="https://nitter.app/about">nitter</a></li>
<li><a href="https://maketecheasier.com/browse-x-anonymously-with-xcancel/">How to Browse X Anonymously With XCancel - Make Tech Easier</a></li>

</ul>
</details>

**社区讨论**: 社区表达了失望和沮丧，一些人表示如果 Nitter 不可用，他们将完全停止阅读 X 内容。其他人建议使用 Mastodon、Bluesky 和 Threads 等替代品，还有人呼吁在其他司法管辖区为这类项目提供法律保护。

**标签**: `#privacy`, `#open-source`, `#legal`, `#twitter`, `#internet-freedom`

---

<a id="item-5"></a>
## [Firefox 157 将在所有平台默认启用 JPEG XL](https://groups.google.com/a/mozilla.org/g/dev-platform/c/3YMV4MS34KA?pli=1) ⭐️ 8.0/10

Firefox 157 将在所有平台默认启用 JPEG XL，标志着浏览器对下一代图像格式支持的重大转变。据报道，Chromium 也在采用 JPEG XL，表明行业正在更广泛地推进。 这是 JPEG XL 广泛采用的重要一步，与旧版 JPEG 相比，它提供了更优越的压缩和功能。这可能会带来更快的网页性能和更低的带宽消耗，惠及用户和开发者。 Firefox 和 Chromium 都在使用基于 Rust 的 jxl-rs 库，这引发了关于 Apple 的 C++ libjxl 实现的疑问。这一转变可能还需要为尚不支持 JPEG XL 的网站和上传字段提供变通方案。

hackernews · yboris · 8月25日 17:55 · [社区讨论](https://news.ycombinator.com/item?id=49437946)

**背景**: JPEG XL 是由 JPEG 委员会、Google 和 Cloudinary 开发的下一代图像格式，支持有损和无损压缩。它专为响应式网页环境设计，并提供无缝 JPEG 转码等功能，可降低存储成本。该格式由 ISO/IEC 18181 标准定义。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JPEG_XL">JPEG XL - Wikipedia</a></li>
<li><a href="https://jpeg.org/jpegxl/">JPEG - JPEG XL</a></li>
<li><a href="https://jpegxl.info/">JPEG XL: Superior Image Compression</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 JPEG XL 的采用表示乐观，一些人希望它最终能完全取代 JPEG。同时，也有人对上传字段的浏览器支持以及自动转换工具的需求表示实际担忧。

**标签**: `#JPEG XL`, `#Firefox`, `#Web Standards`, `#Image Formats`, `#Browser Development`

---

<a id="item-6"></a>
## [EVE Online 开始从 Stackless Python 2.7 迁移到 Python 3](https://simonwillison.net/2026/Aug/25/eve-online-move-to-python-3/) ⭐️ 8.0/10

EVE Online 宣布开始从 Stackless Python 2.7 迁移到 Python 3，使用 futurize 脚本处理 240 万行代码，并手动审查约 20,000 处 Python 2 和 3 之间的行为差异。 此次迁移意义重大，因为 EVE Online 是生产环境中规模最大、运行时间最长的 Python 代码库之一，其成功升级将为其他仍面临迁移的大型 Python 2 项目提供宝贵经验。同时，它也凸显了升级像 Stackless 这样深度定制的 Python 运行时所带来的挑战。 迁移将使用 futurize 脚本，该脚本将 Python 2 代码转换为同时兼容 Python 2 和 3 的代码，随后手动审查约 20,000 处行为差异，例如整数除法。公告未说明如何替换 Stackless，但之前的演示描述了在 EVE Frontier 中使用 carbonengine/scheduler 库。

rss · Simon Willison · 8月25日 22:59

**背景**: Stackless Python 是 Python 的增强版本，提供微线程（绿色线程），避免了传统操作系统线程的开销，这对 EVE Online 的大规模多人服务器架构至关重要。EVE Online 自 2003 年起一直运行在 Stackless Python 上，上一次重大升级是在 2010 年升级到 Stackless Python 2.7。Python 2 已于 2020 年停止维护，因此迁移到 Python 3 对于持续的安全和维护是必要的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stackless_Python">Stackless Python - Wikipedia</a></li>
<li><a href="https://wiki.python.org/moin/StacklessPython.html">StacklessPython - Python Wiki</a></li>
<li><a href="https://python-future.org/futurize.html">futurize: Py2 to Py2/3 — Python-Future documentation</a></li>

</ul>
</details>

**社区讨论**: Lobsters 上的社区讨论普遍对这次迁移的规模表示兴趣和赞赏，一些用户分享了他们自己进行大规模 Python 2 到 3 升级的经验。同时，也有人对 EVE Online 将如何处理 Stackless 的替换表示好奇，因为其集成度很深。

**标签**: `#Python`, `#Migration`, `#EVE Online`, `#Stackless`, `#Large-scale systems`

---

<a id="item-7"></a>
## [IBM Granite 4.2：采用混合架构的密集推理大语言模型](https://huggingface.co/blog/ibm-granite/granite-4-2) ⭐️ 8.0/10

IBM 发布了 Granite 4.2，这是一个密集、仅解码器的推理大语言模型系列，提供三种尺寸（3B、8B 和 30B），具备显式的思维链推理和混合 Mamba-2/Transformer 架构。这些模型可以根据任务复杂度在思考、非思考或低努力模式下运行。 此次发布标志着 IBM 首个推理大语言模型系列，将效率与显式推理能力相结合，对于需要性能和可解释性的企业 AI 应用具有重要意义。混合架构为纯 Transformer 模型提供了潜在替代方案，影响了向更高效、更专业化 LLM 发展的更广泛趋势。 所有三种尺寸共享相同的架构设计，并遵循一致的训练流程：从头预训练、监督微调（SFT）和多阶段强化学习（RL）。混合架构结合了少量标准 Transformer 注意力层和大部分 Mamba-2 状态空间层，模型以 Apache 2.0 许可证发布。

rss · Hugging Face Blog · 8月25日 15:14

**背景**: Granite 4.2 基于 IBM 早期的 Granite 版本构建，这些版本是强大的指令跟随助手。新版本增加了显式推理能力，允许模型在回答前生成思维链。混合 Mamba/Transformer 架构是对传统单一 Transformer 堆栈的突破，旨在实现超高效同时保持高性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/ibm-granite/granite-4-2">A Blog post by IBM Granite on Hugging Face</a></li>
<li><a href="https://www.ibm.com/new/announcements/ibm-granite-4-0-hyper-efficient-high-performance-hybrid-models">IBM Granite 4.0: Hyper-efficient, High Performance Hybrid Models for Enterprise</a></li>
<li><a href="https://medium.com/data-science-in-your-pocket/ibm-granite-4-deep-dive-into-the-hybrid-mamba-transformer-llm-family-c5d01978f27a">IBM Granite 4: Deep Dive Into the Hybrid Mamba/Transformer LLM Family | by Sai Dheeraj Gummadi | Data Science in Your Pocket | Medium</a></li>

</ul>
</details>

**标签**: `#LLM`, `#IBM`, `#Hugging Face`, `#Model Architecture`, `#Training`

---

<a id="item-8"></a>
## [量化感知修复：4 位模型超越全精度原版](https://huggingface.co/blog/MultiverseComputingCAI/quantization-aware-healing) ⭐️ 8.0/10

引入了量化感知修复（QAH）方法，该方法生成的 4 位量化模型性能优于其全精度（bfloat16）版本。当应用于压缩至 600 亿参数并量化为 MXFP4 的 GPT-OSS 120B 模型时，它在 9 个基准测试中的 7 个上超越了原始模型。 这是模型压缩领域的一项重大进展，表明量化模型不仅能匹配甚至能超越全精度性能。这可能使得在资源受限设备上部署大型模型成为可能，同时提高效率和准确性，对 AI 在生产环境中的部署产生深远影响。 QAH 与压缩方法无关，仅需访问未压缩教师模型的 logit 级别信息。然而，其增益尚未在层剪枝、SliceGPT 或低秩分解等其他结构压缩方法中得到验证。

rss · Hugging Face Blog · 8月25日 11:39

**背景**: 量化通过降低模型精度（例如从 32 位浮点数降至 4 位整数）来减少内存和计算成本，但常常会降低准确性。量化感知训练（QAT）是一种常见的缓解技术，通过在训练过程中考虑量化来减少精度损失。QAH 扩展了这一思路，利用原始模型的 logits 来修复压缩和量化后的模型，从而获得超越原始模型的性能提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.20953v1">Quantization-Aware Healing: A Practical Recipe for Recovering Compressed, 4-Bit LLMs</a></li>
<li><a href="https://huggingface.co/blog/MultiverseComputingCAI/quantization-aware-healing">Quantization -Aware Healing: a compressed, 4 - bit model that...</a></li>
<li><a href="https://data-today.net/quantization-aware-healing-4bit-beats-full-precision/">Compressed 4 - bit LLM outperforms full precision with... | Data Today</a></li>

</ul>
</details>

**标签**: `#quantization`, `#model compression`, `#efficient AI`, `#deep learning`, `#Hugging Face`

---

<a id="item-9"></a>
## [Vercel 保护 Next.js 应用免受 2026 年 8 月 RCE 漏洞影响](https://vercel.com/changelog/nextjs-august-2026-security-release) ⭐️ 8.0/10

Vercel 宣布，其平台上托管的 Next.js 应用已受到 2026 年 8 月安全公告中披露的两个严重远程代码执行（RCE）漏洞的保护，无需客户采取任何行动。这些漏洞包括源自 libheif 依赖的 GHSA-2xp9-vwfh-vxw4，以及影响 Windows 托管服务器的 CVE-2026-75604。 这些严重漏洞可能允许未经身份验证的攻击者在易受攻击的 Next.js 服务器上执行任意代码，对应用及其数据构成重大风险。Vercel 的自动保护使其客户免受影响，但自托管用户必须立即升级，这凸显了在更广泛的 Next.js 生态系统中及时修补的重要性。 AVIF 漏洞（GHSA-2xp9-vwfh-vxw4）在 Image Optimization 处理特制的 AVIF 输入时触发，Vercel 已在其托管服务中禁用 AVIF 优化。Windows 漏洞（CVE-2026-75604）影响使用 Pages Router 和未启用 Cache Components 的 App Router 的服务器；Vercel 基于 Linux 的运行时不受影响。

rss · Vercel Blog · 8月25日 16:39

**背景**: Next.js 是一个流行的 React 框架，用于构建服务端渲染的 Web 应用。Image Optimization 是内置功能，可自动调整和优化图像大小，并依赖 libheif 等库来处理 AVIF 格式。Pages Router 和 App Router 是 Next.js 中的两种路由系统，而 Cache Components 是较新的功能，支持组件级缓存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nextjs.org/docs/messages/sharp-version-avif">Sharp Version Does Not Support AVIF | Next.js</a></li>
<li><a href="https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents">next.config.js: cacheComponents | Next.js</a></li>
<li><a href="https://nextjs.org/docs/pages">Pages Router - Next.js</a></li>

</ul>
</details>

**标签**: `#security`, `#Next.js`, `#Vercel`, `#vulnerability`, `#RCE`

---

<a id="item-10"></a>
## [Vercel 推出 Run SDK，实现 AI 代理的安全代码执行](https://vercel.com/blog/introducing-run) ⭐️ 8.0/10

Vercel 发布了 Run SDK，这是一个 JavaScript/TypeScript 执行环境，在 worker 线程内的 QuickJS 沙箱中运行不受信任的代码，将其与宿主应用和网络隔离。它支持宿主函数以实现受控访问，并内置了人工审批和身份验证检查点，可以暂停和恢复执行。 这解决了 AI 代理开发中的一个关键安全漏洞，即使用 eval 执行生成的代码可能会暴露机密和内部服务。通过提供具有明确宿主函数边界和审批机制的安全沙箱，它使得代理能够更安全地部署到与真实应用交互的场景中，并可能成为行业标准实践。 Run SDK 在 worker 线程内的全新 QuickJS 上下文中评估代码，无法直接访问 Node.js 或网络。宿主函数是作为全局变量暴露的普通函数，调用通过序列化跨越沙箱边界；SDK 支持通过重放程序来恢复中断的运行，同时复用已完成的宿主函数调用的记录结果。

rss · Vercel Blog · 8月25日 04:00

**背景**: AI 代理经常生成 TypeScript 程序来协调工具和处理结果，但使用 eval 执行此类代码会赋予其与宿主应用相同的权限，包括访问机密和内部服务。像 QuickJS 这样的小型可嵌入 JavaScript 引擎提供了隔离的执行环境。人工审批是代理框架中常见的模式，用于在敏感操作时暂停执行，如 OpenAI Agents SDK 和微软的代理框架所示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bellard.org/quickjs/">QuickJS Javascript Engine</a></li>
<li><a href="https://openai.github.io/openai-agents-python/human_in_the_loop/">Human-in-the-loop - OpenAI Agents SDK</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/add-human-in-the-loop">Add a human-in-the-loop approval step (preview) - Microsoft ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#security`, `#sandboxing`, `#JavaScript`, `#SDK`

---

<a id="item-11"></a>
## [OpenAI 首席财务官阐释智能充裕背后的全栈](https://openai.com/index/the-full-stack-behind-abundant-intelligence) ⭐️ 7.0/10

OpenAI 首席财务官 Sarah Friar 发布官方公告，阐释芯片、算力、模型和产品方面的进步如何相互叠加，以更大规模、更低成本提供更有用的智能。该文将 AI 进展视为全栈现象，而非单一突破。 这一战略概述表明 OpenAI 关注成本降低和可扩展性，这对 AI 的广泛采用至关重要。同时，它也为投资者和行业勾勒了公司路线图，可能影响对 AI 基础设施投资的预期。 该公告强调从硬件到应用整个 AI 栈的复合收益。它没有引入新的技术细节，而是提供了高层次的叙述，可能关联 OpenAI 更广泛的商业战略和成本效率目标。

rss · OpenAI News · 8月25日 07:05

**背景**: AI 栈是指支持 AI 系统的分层技术集合，包括硬件、算力、存储、框架和应用。作为领先的 AI 实验室，OpenAI 一直在扩展其基础设施和模型，以降低成本并提升能力，这一趋势在整个行业中都有体现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/ai-stack">What is an AI stack? - IBM</a></li>
<li><a href="https://hakia.com/tech-insights/ai-infrastructure-stack/">AI Infrastructure Stack Explained: Components, Architecture ...</a></li>
<li><a href="https://www.cfo.com/news/openai-cfo-sarah-friar-shares-outlook-at-world-economic-forum-elon-musk-lawfare/738015/">OpenAI CFO Sarah Friar discusses AI development, IPOs... | CFO .com</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI infrastructure`, `#compute`, `#models`, `#strategy`

---

<a id="item-12"></a>
## [GitHub 在生产环境中评估 LLM 的经验教训](https://github.blog/ai-and-ml/llms/how-to-evaluate-llms-before-production/) ⭐️ 7.0/10

GitHub 发布了一篇博客文章，详细介绍了他们在实际秘密扫描中评估 LLM 的经验教训，重点是减少误报。文章强调超越基准测试，进行针对产品的评估。 这一指导对于在生产环境中部署 LLM 的从业者具有重要意义，因为它提供了一家大型科技公司的实用方法论。它强调了严格测试和产品决策的重要性，而非通用基准，这可以提高 AI 系统的可靠性和安全性。 这篇文章基于 GitHub 在秘密扫描方面的经验，秘密扫描用于识别提交到仓库中的令牌和密钥等凭据。文章可能讨论了平衡精确率和召回率等挑战，以及为特定用例定制评估集的必要性。

rss · GitHub AI and ML · 8月25日 21:35

**背景**: 在生产环境中部署模型之前，LLM 评估至关重要，因为模型可能在基准测试中表现良好，但在实际场景中失败。GitHub 的秘密扫描使用 LLM 来减少误报，这是安全应用中的常见挑战。这篇博客文章可能提供了一个超越标准指标的评估框架，考虑领域特定准确性和操作约束等因素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.blog/ai-and-ml/llms/how-to-evaluate-llms-before-production/">How to evaluate LLMs before production - The GitHub Blog</a></li>
<li><a href="https://www.startuphub.ai/ai-news/artificial-intelligence/2026/llm-evaluation-beyond-benchmarks">LLM Evaluation : Beyond Benchmarks | StartupHub.ai</a></li>
<li><a href="https://layerlens.ai/blog/llm-evaluation-metrics-for-production-systems">LLM Evaluation Metrics for Production Systems | LayerLens</a></li>

</ul>
</details>

**标签**: `#LLM`, `#evaluation`, `#production`, `#GitHub`, `#AI`

---

<a id="item-13"></a>
## [Vercel Connect 正式发布：为 AI 代理提供运行时作用域凭据](https://vercel.com/blog/the-end-of-credential-sprawl-for-agents) ⭐️ 7.0/10

Vercel Connect 现已正式发布，用运行时作用域、短期凭据取代 AI 代理的长期令牌。该平台现在支持超过 100 个连接器，并包含面向生产环境的治理能力。 这解决了 AI 代理开发中的一个关键安全漏洞，消除了长期令牌泄露的风险。它实现了细粒度、按请求的访问控制，这对于代理越来越多地与多个外部服务交互至关重要。 凭据在运行时通过 OIDC 身份请求，应用中不存储提供方机密。令牌可按任务作用域、支持指定用户主体，并自动刷新，而撤销只需一条命令。

rss · Vercel Blog · 8月25日 04:00

**背景**: 长期令牌一直是一个持续的安全风险，因为它们永不过期且通常具有广泛权限，一旦泄露就非常危险。Vercel Connect 利用 OIDC 允许应用程序在运行时请求短期、作用域的令牌，从而减少了攻击面。这种方法符合 AI 代理凭据管理的最佳实践，如最小权限范围和临时令牌。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vercel.com/blog/the-end-of-credential-sprawl-for-agents">The end of credential sprawl for agents - Vercel</a></li>
<li><a href="https://ascii.co.uk/news/article/news-20260619-8043d639/vercel-connect-enables-runtime-credential-exchange-for-ai-ag">Vercel Connect Enables Runtime Credential Exchange... | ASCII News</a></li>
<li><a href="https://vercel-com.nproxy.org/docs/connect">Vercel Connect</a></li>

</ul>
</details>

**标签**: `#security`, `#AI agents`, `#credentials`, `#Vercel`, `#devtools`

---

<a id="item-14"></a>
## [OpenAI 的 Codex 集成 WebMCP 以增强智能体交互](https://news.google.com/rss/articles/CBMivgFBVV95cUxQa1NEdnRlTk5SUmJZNDNOekQ2TFE2djk3SmRHYVhlZ0pYaUFkVkJrbHZqanRzRVFHWlRiRVVfOHo3dkVKSDJEM0tOZUxWVks1TC1zVTlyUktxWlZiNFQyRHdGMEpCWXBjNVBKdkNXQmFFNFpjMkxnNTBXY1loNi1pOVM5dGdVUkdaMEw0aGxjWjV2cTl2Rms5bWRNVzRWRnY1aFJtMEstNkc3QmFFUkowc2xjVWgzQTlreWxweHdR?oc=5) ⭐️ 7.0/10

OpenAI 已将实验性开放标准 WebMCP 集成到其 Codex 智能体中，使网站能够直接向 AI 智能体暴露结构化工具。这一集成使 Codex 能够更动态、更协作地与 Web 服务交互，该消息由 OpenAI 的 Eric Provencher 宣布。 这一进展意义重大，因为它增强了 AI 智能体准确高效地执行真实 Web 任务的能力，可能改变 AI 与 Web 应用交互的方式。它可能通过实现更可靠的自动化并减少智能体猜测用户界面的需求，使开发者和企业受益。 WebMCP 是一个实验性开放标准，允许网站为智能体定义结构化工具，Codex 可以自动理解规范并编写必要的工具。集成过程被描述为简单直接，ChatGPT 学习网站提供了相关指南，OpenAI 还发起了 WebMCP 挑战赛以鼓励创新。

google_news · StartupHub.ai · 8月25日 21:04

**背景**: Codex 是 OpenAI 的 AI 编程智能体，帮助工程团队自动化拉取请求、代码审查等任务。WebMCP（Web 模型上下文协议）是一个实验性标准，将 MCP（模型上下文协议）的概念扩展到 Web 服务，允许智能体通过定义的工具与网站交互，而不是进行非结构化的浏览。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.startuphub.ai/ai-news/artificial-intelligence/2026/openai-s-codex-adds-webmcp-for-enhanced-agent-interactions">OpenAI 's Codex Adds WebMCP for Enhanced Agent... | StartupHub.ai</a></li>
<li><a href="https://openai.com/webmcp-challenge/">WebMCP Challenge | OpenAI</a></li>
<li><a href="https://learn.chatgpt.com/docs/webmcp">Use WebMCP to give AI agents a direct way to work with your website</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Codex`, `#WebMCP`, `#AI agents`, `#web services`

---

<a id="item-15"></a>
## [Pi 可扩展工作流：用于多智能体编排的确定性 DSL](https://news.google.com/rss/articles/CBMifkFVX3lxTE5zN0Y2cmdXZEtYR3lZUkhsaXhUckpwalNkT2xQbGV1LVYxWkNONkF2QzJqdV9RZ09rWTgxOTgteG85NXBpM0N2WXNYc3ZPRk1pMWRKSVE2aWRzLVY2U0RESkpBaDlpTTRPVUFteXB2Sy1CNXpnNUVmRDJMemYtdw?oc=5) ⭐️ 7.0/10

Pasquale Pillitteri 发布了一篇指南，解释了 Pi Extensible Workflows，这是一种用于多智能体编排的确定性 DSL。该 DSL 提供智能体形状的原语、并行执行、运行预算和可恢复日志，并基于 JavaScript 实现控制流。 这很重要，因为确定性编排对于可靠的多智能体系统至关重要，满足了 AI 应用中对结构化、可恢复工作流的需求。它为开发者提供了一种构建复杂智能体交互并实现可预测结果的方法，可能提高生产就绪度。 该 DSL 用 JavaScript 实现，因此继承了循环、条件语句和函数，而 DSL 提供智能体特定的动词。工作流可以声明输出 JSON 模式，确保返回结构化数据。核心安装包括 reviewLoop 启动器和持久的子智能体工具，如 subagents_run 和 subagents_inspect。

google_news · Pasquale Pillitteri · 8月25日 09:57

**背景**: 多智能体编排涉及协调多个 AI 智能体以完成复杂任务。传统方法通常依赖 LLM 驱动的控制流，这可能是非确定性的。Pi Extensible Workflows 通过使用显式定义控制流的 DSL 提供了一种确定性替代方案，使工作流更可预测且可恢复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://the-agent-daily.org/the-pi-side-of-agents/deep-dives/pi-extensible-workflows-deterministic-orchestration">Pi Extensible Workflows: Putting the Loop Back in Code</a></li>
<li><a href="https://vekexasia.github.io/pi-extensible-workflows/index.html">pi-extensible-workflows documentation</a></li>
<li><a href="https://github.com/vekexasia/pi-extensible-workflows">GitHub - vekexasia/pi-extensible-workflows: Deterministic ...</a></li>

</ul>
</details>

**标签**: `#multi-agent systems`, `#DSL`, `#orchestration`, `#AI`

---