---
layout: default
title: "Horizon Summary: 2026-09-10 (ZH)"
date: 2026-09-10
lang: zh
---

> 从 36 条内容中筛选出 9 条重要资讯。

---

1. [Calif Research 发布 WeWorm：首个通过微信通话传播的零点击蠕虫](#item-1) ⭐️ 9.0/10
2. [OpenAI 发布 GPT-6 Astra，号称最强商业模型](#item-2) ⭐️ 9.0/10
3. [vLLM v0.29.0 将 Model Runner V2 设为默认，新增 770B MoE 支持](#item-3) ⭐️ 8.0/10
4. [苹果发布首款折叠屏手机 iPhone Duo](#item-4) ⭐️ 8.0/10
5. [Show HN：将光速缩小到 5 公里/小时的交互式可视化](#item-5) ⭐️ 8.0/10
6. [Shopify 收购 Tailwind CSS 背后的公司 Tailwind Labs](#item-6) ⭐️ 8.0/10
7. [Raschka 解析 GPT-6 Astra、循环 Transformer 与隐藏推理](#item-7) ⭐️ 8.0/10
8. [Automattic 董事会强制 CEO Matt Mullenweg 休假](#item-8) ⭐️ 8.0/10
9. [IBM 发布 SOTA 级 Granite 时间序列 PatchTST-FM-r2 模型，采用商业友好许可](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Calif Research 发布 WeWorm：首个通过微信通话传播的零点击蠕虫](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research 发布了一个名为 WeWorm 的演示，号称是首个通过微信通话在 iOS 和 Android 上传播的零点击蠕虫，无需受害者接听或操作手机即可劫持其账号。该团队借助 AI 在大约两天内找到漏洞并写出首个远程代码执行（RCE）利用程序，随后又用约一周时间构建出完整的蠕虫。 这标志着漏洞利用开发模式的转变：过去需要更大团队耗时数月才能完成的蠕虫，如今小团队借助 AI 约一周就能构建出来，这引发了人们对 AI 加速网络威胁的严重担忧，而微信拥有约 14 亿用户。这也凸显了 AI 如何降低制造复杂自传播攻击的门槛。 该攻击利用了微信 VoIP（网络电话）栈中的内存破坏漏洞，可在数秒内攻陷目标账号；即使受害者接听电话，也听不到任何声音，漏洞利用依然成功。Calif 在三部测试手机上演示了蠕虫的传播，该研究于 2026 年 9 月 8 日发布。

rss · Simon Willison · 9月10日 00:56

**背景**: 零点击漏洞利用无需受害者进行任何操作，因此比依赖诱骗用户点击链接或打开文件的攻击危险得多。蠕虫是一种能自动从一台设备传播到另一台设备的自我复制恶意软件，而远程代码执行（RCE）意味着攻击者可在目标系统上运行任意代码。微信是中国极受欢迎的即时通讯应用，拥有约 14 亿用户，其 VoIP 通话功能正是此次攻击的入口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html">WeChat Zero-Click Worm Took Over Accounts on iPhone and Android via Incoming Calls</a></li>
<li><a href="https://cyberinsider.com/zero-click-worm-spreads-on-iphones-and-android-via-wechat-calls/">Zero-click worm spreads on iPhones and Android via WeChat calls</a></li>
<li><a href="https://www.ibtimes.com/wechats-14-billion-users-faced-dangerous-security-flaw-ai-helped-turn-it-self-spreading-worm-3807225">WeChat’s 1.4 Billion Users Faced a Dangerous Security Flaw ...</a></li>

</ul>
</details>

**标签**: `#security`, `#AI`, `#exploit`, `#WeChat`, `#zero-click`

---

<a id="item-2"></a>
## [OpenAI 发布 GPT-6 Astra，号称最强商业模型](https://openai.com/index/gpt-6-astra-next-generation-work) ⭐️ 9.0/10

OpenAI 发布了 GPT-6 Astra，称其为面向商业场景的最强模型，具备高级推理、计算机操作能力，以及更强的写作与设计判断力。目前该公告仅为简短预告，尚未公布技术细节、基准测试成绩或定价信息。 OpenAI 推出的这款面向商业场景的新旗舰模型，可能重塑企业部署 AI 代理进行编程、研究和端到端工作流程的方式，并加剧与 Anthropic、Google 等对手的竞争。如果其宣称的推理与计算机操作能力提升属实，将加速企业对自主 AI 员工的采用。 该预告强调了三大能力方向：高级推理、计算机操作（让模型通过鼠标和键盘动作操作软件），以及更强的写作与设计判断力。公告中未披露上下文窗口、定价、可用日期或基准测试数据。

rss · OpenAI News · 9月9日 11:00

**背景**: OpenAI 的 GPT 系列是驱动聊天机器人和 AI 应用的大型语言模型，每一代新模型通常都会增加新能力并改进旧版本。“计算机操作”指的是 AI 模型能够直接控制软件界面，而不仅仅依赖定制工具，这一前沿方向由 Anthropic 的 Claude 率先探索。高级推理模型经过训练，能够通过反复检查和修正中间步骤来解决逻辑、数学和编程中的多步问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://emergent.sh/news/openai-launches-gpt-6-astra-multimodal-ai">OpenAI Launches GPT - 6 Astra : Multimodal AI Model</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/tools-computer-use">Computer use | OpenAI API</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reasoning_model">Reasoning model - Wikipedia</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-6`, `#AI`, `#LLM`, `#business`

---

<a id="item-3"></a>
## [vLLM v0.29.0 将 Model Runner V2 设为默认，新增 770B MoE 支持](https://github.com/vllm-project/vllm/releases/tag/v0.29.0) ⭐️ 8.0/10

vLLM v0.29.0 正式发布，包含来自 277 位贡献者的 594 次提交，将 Model Runner V2（MRV2）设为所有模型的默认执行核心，并新增对多个大型模型的支持，包括腾讯 770B/49B 激活参数的 MoE 模型（Hy4-preview）、Kimi K3 NVFP4 检查点、Qwen3.8-Flash-Next 以及 GraniteSWA/GraniteMoeSWA。该版本还引入了批量分片采样（将每步 logits 内存降低 1/TP）、用于 KV 缓存自动调优的 CUDA 图内存分析，以及大量投机解码和 RL 权重同步方面的改进。 作为使用最广泛的开源 LLM 推理引擎之一，vLLM 向 MRV2 的架构迁移以及对腾讯 770B MoE、Kimi K3 等前沿规模模型的支持，直接影响社区服务尖端模型的效率。本次发布中的性能优化有望在整个生态系统中显著降低生产级 LLM 部署的延迟和内存成本。 MRV1 仍在少数 ROCm 模型以及 MRV2 尚未支持的功能中使用；本次发布包含多项破坏性变更，例如移除十个已弃用的模型架构、将 FlexOlmo/Olmo3/Hunyuan V1/VL 迁移至 Transformers 后端、移除 PyAV 视频解码器，以及弃用 `python -m vllm.entrypoints.openai.api_server` 转而推荐 `vllm serve`。新的默认设置包括对 TP CUDA 组启用 FlashInfer all-reduce 以及确定性的前缀缓存 NONE_HASH，同时新增了 `--max-num-queued-reqs` 和 `--max-num-queued-tokens` 准入控制参数。

github · khluu · 9月9日 08:54

**背景**: vLLM 是一个开源的高吞吐量大语言模型推理与服务引擎，被广泛用于在生产环境中部署 Llama、Qwen、DeepSeek 等模型。Model Runner V2 是重新设计的执行核心，用模块化的模型逻辑、GPU 原生输入准备和稳定的持久批处理取代了最初的 V1 设计，解决了自 V1 以来积累的技术债务。MoE（混合专家）是一种架构，每个 token 仅激活一小部分专门的子网络，使模型能够扩展到数千亿参数，同时保持推理成本可控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM</a></li>
<li><a href="https://www.oflight.co.jp/en/glossary/moe">MoE ( Mixture of Experts ) | Oflight Inc.</a></li>

</ul>
</details>

**标签**: `#vllm`, `#llm-inference`, `#model-serving`, `#release`, `#moe`

---

<a id="item-4"></a>
## [苹果发布首款折叠屏手机 iPhone Duo](https://www.apple.com/iphone-duo/) ⭐️ 8.0/10

苹果正式发布了 iPhone Duo，这是其首款折叠屏 iPhone，标志着苹果正式进入折叠屏智能手机市场。该消息在 Hacker News 上引发了广泛讨论，获得了 1109 分和 1959 条评论。 这是一项重大的产品发布，标志着苹果正式进入目前由三星主导的折叠屏手机领域，可能重塑市场格局。它可能影响整个智能手机行业的设计方向，并影响数百万考虑升级的 iPhone 用户。 社区成员指出，根据上手视频，iPhone Duo 似乎没有可见的折痕，这解决了折叠屏的一个常见问题。然而，一些人对耐用性表示怀疑，将其与使用一段时间后出现折痕和铰链异响的三星 Fold 展示机进行了比较。

hackernews · thecosmicfrog · 9月9日 18:15 · [社区讨论](https://news.ycombinator.com/item?id=49630931)

**背景**: 折叠屏智能手机采用可弯曲的柔性显示屏，使设备既能作为手机使用，也能作为小型平板电脑。三星凭借 Galaxy Z Fold 系列一直引领这一品类，而苹果此前一直未涉足该形态。iPhone Duo 是苹果首次尝试折叠设备，其成功可能取决于能否解决困扰早期折叠屏的耐用性和折痕问题。

**社区讨论**: Hacker News 上的讨论非常热烈，用户就市场可行性、耐用性和苹果的设计方向展开了辩论。一些人质疑，鉴于 iPhone mini 的销售份额较低，Duo 是否会有好的销量；另一些人则称赞其没有折痕，并对 John Ternus 领导下苹果的新设计方向表示兴奋。一个普遍的观点是，先观望该设备在几代产品中的表现，再决定是否换用。

**标签**: `#Apple`, `#iPhone`, `#foldable`, `#hardware`, `#Hacker News`

---

<a id="item-5"></a>
## [Show HN：将光速缩小到 5 公里/小时的交互式可视化](https://rivendell.dmitrybrant.com/relativity/) ⭐️ 8.0/10

开发者 Dmitry Brant 发布了一个交互式网页可视化，将光速缩小到 5 公里/小时，让用户能用日常物体体验相对论效应。第一个版本已在 rivendell.dmitrybrant.com/relativity/上线，并在 Hacker News 上引发了详细讨论。 通过让相对论效应在人类尺度速度下变得直观，这个工具有望改善物理教育和公众对狭义相对论的理解——这种理论的效应在日常生活中通常不可见。它还引发了与 MIT 早期作品《Slower Speed of Light》游戏的比较，可能提高此类模拟的准确性标准。 根据社区反馈，该可视化在技术上是准确的，但一些用户指出洛伦兹不变性的微妙之处——例如两个非平行助推产生的旋转——可能没有完全体现。该项目开放反馈，并托管在个人网站上。

hackernews · dmitrybrant · 9月10日 01:58 · [社区讨论](https://news.ycombinator.com/item?id=49637385)

**背景**: 狭义相对论预测，当物体接近光速时，会发生时间膨胀、长度收缩和相对论多普勒频移。这些效应在日常速度下可以忽略不计，因此将光速缩小到 5 公里/小时能让它们变得可感知。此前像 MIT 的《Slower Speed of Light》（2012）这样的教育工具尝试过类似模拟，但据报道存在不准确之处。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Special_relativity">Special relativity - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Relativistic_effects">Relativistic effects</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该可视化比 MIT 的《Slower Speed of Light》更准确，其中一人指出 MIT 游戏在相对论多普勒建模方面的问题。其他人讨论了洛伦兹不变性的微妙之处、鉴于米的定义改变光速的反事实性质，并引用了探索改变物理定律的科幻作品。

**标签**: `#physics`, `#visualization`, `#relativity`, `#interactive`, `#education`

---

<a id="item-6"></a>
## [Shopify 收购 Tailwind CSS 背后的公司 Tailwind Labs](https://tailwindcss.com/blog/tailwind-is-joining-shopify) ⭐️ 8.0/10

Shopify 已收购由 Adam Wathan 创立、开发广受欢迎的实用优先 CSS 框架 Tailwind CSS 的公司 Tailwind Labs，这一消息在 Tailwind 官方博客上公布。此前 Tailwind Labs 曾披露，AI 带来的变化导致其文档流量自 2023 年初以来下降约 40%，并造成约 75% 的工程团队被裁员。 这笔交易凸显了 AI 编程助手正在颠覆依赖文档流量和模板销售的开发者工具公司的商业模式，即便是像 Tailwind CSS 这样流行的项目也难以幸免。同时，这也引发了人们对这一重要开源 CSS 框架在被大型电商平台收购后的治理和未来走向的疑问。 Tailwind Labs 表示，尽管 Tailwind 比以往任何时候都更受欢迎，但其文档流量自 2023 年初以来下降了约 40%，并且由于 AI 对业务的影响，75% 的工程团队失去了工作。社区成员认为，Shopify 收购的是团队和品牌，而不是开源框架本身。

hackernews · EdwinHoksberg · 9月9日 13:27 · [社区讨论](https://news.ycombinator.com/item?id=49626190)

**背景**: Tailwind CSS 是一个实用优先的 CSS 框架，允许开发者直接在 HTML 标记中应用小型、单一用途的类来为网页设置样式，而无需编写自定义 CSS。Tailwind Labs 由 Adam Wathan 于 2019 年 1 月创立，围绕这一开源框架通过文档、付费 UI 模板和相关工具建立了商业模式。Shopify 是一家大型电商平台，也维护着自己的开发者生态系统，包括基于 Ruby on Rails 的 Shopify 平台和各种前端工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tailwindcss.com/">Tailwind CSS - Rapidly build modern websites without ever leaving your HTML.</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tailwind_CSS">Tailwind CSS - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/company/tailwind-labs">Tailwind Labs | LinkedIn</a></li>

</ul>
</details>

**社区讨论**: 评论者大多认为此次收购是 AI 侵蚀 Tailwind Labs 文档和模板业务的结果，一些人质疑在原生 CSS 和 AI 辅助编码可行的情况下，新网站是否还需要 Tailwind。其他人则对团队表示感谢，并希望该开源项目在 Shopify 旗下继续蓬勃发展，同时指出在 AI 时代，同时运营开源和商业组件的开发者工具公司正变得越来越困难。

**标签**: `#Tailwind CSS`, `#acquisition`, `#open source`, `#AI impact`, `#web development`

---

<a id="item-7"></a>
## [Raschka 解析 GPT-6 Astra、循环 Transformer 与隐藏推理](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and) ⭐️ 8.0/10

Sebastian Raschka 发表了一篇技术深度分析文章，剖析 GPT-6 Astra、循环 Transformer 和隐藏推理，旨在澄清 The Information 近期报道带来的媒体炒作。文章指出，循环 Transformer（也称循环深度或深度共享）通过重复传递复用权重，在节省 GPU 显存的同时，其效果类似于堆叠更多层。 该分析的重要性在于纠正了将循环 Transformer 视为某种秘密、可怕且会加大思维链监控难度的技术的误解，澄清它实际上是一种节省显存的架构选择。这有助于大语言模型研究者和从业者理解其对推理透明度和模型设计的真正影响。 循环 Transformer 具有可证明的通用计算和逼近性质，当内部步骤在激活空间中计算而不出现在思维链中时，就会产生隐藏推理。社区讨论引用了 Will Merrill 关于思维链计算需求以及通用 Transformer 影响的研究。

hackernews · ModelForge · 9月9日 14:37 · [社区讨论](https://news.ycombinator.com/item?id=49627370)

**背景**: GPT-6 Astra 是 OpenAI 开发的大语言模型，于 2026 年 9 月 3 日向获批用户首发，次日全面开放。循环 Transformer（又称循环深度或循环深度共享）在多次传递中复用同一组权重，因此比标准深层 Transformer 更节省显存。隐藏推理指推理发生在模型隐藏层或激活空间内部，而非通过思维链用语言表达出来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/looped-depth-sharing/">Looped Transformer | Sebastian Raschka, PhD</a></li>
<li><a href="https://www.lesswrong.com/posts/ZrgFfeWuckpwK5Lyi/hidden-reasoning-in-llms-a-taxonomy">Hidden Reasoning in LLMs : A Taxonomy — LessWrong</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra</a></li>

</ul>
</details>

**社区讨论**: 评论者大多称赞 Raschka 的解释清晰易懂，有人指出它纠正了 The Information 将循环 Transformer 描述为可怕秘密技术的误导性说法。其他人分享了研究参考，如 Will Merrill 关于思维链计算需求和通用 Transformer 的工作，并讨论了将 Transformer 自身循环本质上就是隐藏推理。还有评论者称赞 MSPAINT 计算机使用演示令人印象深刻。

**标签**: `#LLM`, `#transformers`, `#reasoning`, `#AI research`, `#chain-of-thought`

---

<a id="item-8"></a>
## [Automattic 董事会强制 CEO Matt Mullenweg 休假](https://techcrunch.com/2026/09/09/automattics-board-forces-ceo-matt-mullenweg-into-leave-of-absence/) ⭐️ 8.0/10

Automattic 董事会投票决定，强制创始人兼 CEO Matt Mullenweg 带薪休假，并任命 CFO Mark Davies 为临时 CEO。Mullenweg 在公司全员 Slack 频道中宣布了这一消息，称董事会成员 Ann Dunwoody、Toni Schneider 和 Sue Decker“暗中串通”，而他本人投了反对票。 Automattic 是 WordPress.com 的运营公司，也是开源 WordPress 项目的主要贡献者，而 WordPress 支撑着全球超过 43% 的网站，因此高层领导变动对开源生态以及依赖 WordPress 的数百万网站都有重大影响。此举表明董事会愿意对 Mullenweg 长期以来的控制权采取行动，可能重塑公司乃至整个 WordPress 社区的治理格局。 Mullenweg 表示，他仅提前 50 分钟收到通知，且董事会在投票前拒绝了他咨询法律顾问的请求。他在 Slack 中点名的董事会成员包括 Ann Dunwoody、Toni Schneider 和 Sue Decker，而 CFO Mark Davies 已被任命为临时 CEO。

hackernews · LeoPanthera · 9月9日 23:49 · [社区讨论](https://news.ycombinator.com/item?id=49636283)

**背景**: Matt Mullenweg 于 2003 年联合创办了开源发布软件 WordPress，并于 2005 年创立 Automattic；该公司运营 WordPress.com，并为 WordPress 项目做出大量贡献。WordPress 是一个免费的内容管理系统，全球超过 43% 的网站都在使用，这使 Automattic 和 Mullenweg 在开源生态中拥有巨大影响力。近年来，Mullenweg 因处理 WP Engine 纠纷及其他争议而受到批评，2025 年 4 月 Automattic 还裁掉了 16% 的员工。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/09/09/automattics-board-forces-ceo-matt-mullenweg-into-leave-of-absence/">Automattic's board forces CEO Matt Mullenweg into leave of ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Matt_Mullenweg">Matt Mullenweg</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automattic">Automattic - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者大多认为董事会的决定虽有必要但风险很大：有人指出 WordPress 支撑着互联网很大一部分，而 Mullenweg 作为 CEO“一错再错”，休假是明智之举，但此人怀疑 Mullenweg 不会回归。也有人强调，Mullenweg 对 Automattic 和 WordPress 的控制权难以轻易解除，并预测他会对董事会进行报复，事态在好转之前还会进一步恶化。

**标签**: `#WordPress`, `#Automattic`, `#leadership`, `#open-source`, `#corporate-governance`

---

<a id="item-9"></a>
## [IBM 发布 SOTA 级 Granite 时间序列 PatchTST-FM-r2 模型，采用商业友好许可](https://huggingface.co/blog/ibm-research/ibm-releases-sota-granite-time-series) ⭐️ 7.0/10

IBM Research 发布了 Granite Time Series PatchTST-FM-r2，这是一个在 Hugging Face 上以商业友好许可提供的最先进时间序列基础模型。该模型基于 PatchTST 架构构建，是 IBM Granite 时间序列系列的最新成员，使更广泛的工业应用无需受限于严格的许可条款。 此次发布意义重大，因为它将最先进的预测性能与宽松的许可相结合，降低了企业在商业产品中部署时间序列基础模型的门槛。同时，它也在不断壮大的时间序列基础模型领域加剧了竞争，与 Google 的 TimesFM 和 Salesforce 的 Moirai 等产品形成对标。 该模型基于 PatchTST 架构，该架构将时间序列分割为补丁（patch）作为 Transformer 主干的输入 token，并且是 IBM 在 Hugging Face 上 Granite 时间序列集合的一部分。IBM 更广泛的 Granite TSFM 系列还包括 Tiny Time Mixer（TTM）和 TSPulse 等超轻量级模型，仅需几百万参数且无需 GPU 即可推理。

rss · Hugging Face Blog · 9月9日 15:36

**背景**: 时间序列基础模型是预训练模型，用于对销售数据、传感器读数或金融指标等序列数据进行预测、分类和异常检测，类似于大语言模型处理文本的方式。PatchTST 在 2023 年 ICLR 论文《A Time Series is Worth 64 Words》中提出，是一种基于 Transformer 的方法，通过将时间序列分割为补丁来提高长期预测效率。IBM 的 Granite 计划是其面向企业的基础模型系列，而 Granite 时间序列产品线将这一理念扩展到时间数据，并在 Hugging Face 上提供模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/yuqinie98/PatchTST">GitHub - yuqinie98/PatchTST: An offical implementation of PatchTST: "A Time Series is Worth 64 Words: Long-term Forecasting with Transformers." (ICLR 2023) https://arxiv.org/abs/2211.14730 · GitHub</a></li>
<li><a href="https://www.ibm.com/granite/docs/models/time-series">Granite Time Series | IBM Granite</a></li>
<li><a href="https://github.com/ibm-granite/granite-tsfm">GitHub - ibm-granite/granite-tsfm: Foundation Models for Time ...</a></li>

</ul>
</details>

**标签**: `#time series`, `#foundation models`, `#IBM Granite`, `#AI/ML`, `#open source`

---