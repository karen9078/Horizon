---
layout: default
title: "Horizon Summary: 2026-09-23 (ZH)"
date: 2026-09-23
lang: zh
---

> 从 39 条内容中筛选出 9 条重要资讯。

---

1. [OpenAI 发布 GPT-6 Sol 与 Luna，降价并提升准确率](#item-1) ⭐️ 9.0/10
2. [Anthropic 发布 Claude Opus 5.5，大幅降价](#item-2) ⭐️ 9.0/10
3. [五角大楼称过度依赖 AI 导致伊朗学校遭导弹袭击](#item-3) ⭐️ 9.0/10
4. [OpenAI GPT-6 Astra 据称破解长期未解的恩尼格玛密文](#item-4) ⭐️ 8.0/10
5. [ShinyHunters 声称入侵 FBI 并窃取全部员工数据](#item-5) ⭐️ 8.0/10
6. [OpenAI 为 GPT-6 推出改进版提示缓存](#item-6) ⭐️ 8.0/10
7. [Parallel 借助 GPT-6 Astra 将研究时间和成本减半](#item-7) ⭐️ 8.0/10
8. [John Platt 谈 AI 驱动科学、气候变化与超级智能](#item-8) ⭐️ 7.0/10
9. [JetBrains 推出 Air：面向智能体开发的开放系统](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 GPT-6 Sol 与 Luna，降价并提升准确率](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 9.0/10

OpenAI 发布了 GPT-6 Sol 和 Luna，在 API 中分别以 gpt-6-sol 和 gpt-6-luna 提供。据称 Sol 的错误率仅为 GPT-5.6 的一半，而 Luna 以大约 GPT-5.6 Luna 一半的价格达到了此前更高层级模型的性能。 此次发布将竞争焦点从单纯的智能水平转向更便宜、更可靠的 AI，为开发者提供了更多迭代空间，也让团队更有信心将更大型的任务交给 Codex 等智能体。同时，这也加剧了对 Anthropic 的 Claude Code 等竞争对手的价格压力。 GPT-6 Sol 拥有 922K 上下文窗口，定价为每百万输入/输出 token 2 美元/10 美元；Luna 则定位为快速、高性价比的模型，适合高吞吐量和延迟敏感型工作负载。值得注意的是，“GPT-6 Sol Pro”是一种推理模式而非独立模型，旧的 GPT-5.6 Sol Pro 条目现在沿用新 Sol 的价目表。

hackernews · OpenAI News · 9月22日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49805509)

**背景**: OpenAI 的 GPT 系列是驱动 ChatGPT 和 OpenAI API 的大型语言模型家族。每一代通常都会在推理、编程和成本效益方面带来改进，而 Sol 和 Luna 这样的模型层级让开发者可以在最强能力与更低成本之间做选择。此次发布紧随 GPT-5.6 和 GPT-6 Astra 等早期版本，正值 AI 编程智能体竞争日益激烈之际。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT - 6 Sol and Luna | OpenAI</a></li>
<li><a href="https://www.zdnet.com/innovation/openai-gpt-6-sol-luna-release/">OpenAI 's GPT - 6 Sol doubles its accuracy rate - for half the... - ZDNET</a></li>
<li><a href="https://openrouter.ai/openai/gpt-6-luna">GPT - 6 Luna - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者强调 Luna 价格减半是一大变化，simonw 分享了 GPT-6 Sol、Luna 和 Astra 的鹈鹕基准对比。其他人则讨论了对 GPT-5.6 Sol 等旧模型的情感依恋、Codex Pro 与 Claude Code 20x 套餐之间的实际取舍，并称赞 ChatGPT Plus 对普通用户而言几乎无限量使用。

**标签**: `#OpenAI`, `#GPT-6`, `#LLM`, `#AI agents`, `#model release`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Opus 5.5，大幅降价](https://www.anthropic.com/claude-opus-5-5) ⭐️ 9.0/10

Anthropic 发布了 Claude Opus 5.5，这是其公开呼吁“为前沿 AI 发展设定节奏”之后推出的首个模型，特点是沟通风格更自然，并且全线降价。价格降至每百万输入 token 4 美元、每百万输出 token 20 美元，缓存读取为每百万 token 0.20 美元，缓存写入为 5 美元。 此次降价让开发者能以明显更低的成本获得 Opus 级别的能力，用于构建智能体编程和长时间运行的知识工作应用；同时，这次发布引发了强烈质疑，因为它似乎与 Anthropic 自己最近呼吁放缓前沿发展的立场相矛盾。鉴于 Opus 5 据称是 OpenRouter 上支出最高的模型之一，典型工作负载成本降低 40% 可能使大量生产流量转向 Anthropic。 与 Opus 5 相比，缓存读取从每百万 token 0.50 美元降至 0.20 美元，输入 token 从 5 美元降至 4 美元，输出 token 从 25 美元降至 20 美元，缓存写入从 6.25 美元降至 5 美元，典型工作负载成本约降低 40%。Anthropic 表示，早期测试者认为 Opus 5.5 的写作更清晰、更易理解，会把最重要的信息放在前面，公司将其同时视为可用性和安全性方面的改进。

hackernews · km144 · 9月22日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=49803892)

**背景**: Anthropic 的 Claude 系列按能力分为 Haiku、Sonnet 和 Opus 三个层级，其中 Opus 能力最强。“为前沿设定节奏”（pacing the frontier）指的是一个公开倡议，呼吁各国政府开发技术和治理工具，以刻意放缓先进自动化 AI 系统的发展。Anthropic 的发布节奏因此成为争议焦点，因为该公司一边签署了该倡议，一边仍在持续推出新的前沿模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5.5 \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/models/opus-5-5/overview">Claude Opus 5.5 - Claude Platform Docs</a></li>
<li><a href="https://www.pacingthefrontier.com/">Pacing the Frontier</a></li>

</ul>
</details>

**社区讨论**: 评论者意见明显分化：最高赞评论讽刺 Anthropic 一边以“为前沿设定节奏”的呼吁作为公告开头，一边在正文中详细展示快速进展；也有人对期待已久的降价表示欢迎。一些开发者表示对 DeepSeek v4.1 等更便宜的替代方案已经满意，还有人分享了不同思考等级下的鹈鹕测试输出等实测结果。

**标签**: `#AI/ML`, `#LLM`, `#Anthropic`, `#Claude`, `#AI Pricing`

---

<a id="item-3"></a>
## [五角大楼称过度依赖 AI 导致伊朗学校遭导弹袭击](https://www.bloomberg.com/graphics/2026-iran-school-attack/) ⭐️ 9.0/10

一份五角大楼报告得出结论，过度依赖 Palantir 公司开发的 AI 目标定位工具，导致了美军对伊朗一所学校的导弹袭击，造成 123 名伊朗儿童死亡。报告认定美国“未能尽一切可行努力核实”目标，且这一失误“超出了单纯的疏忽”。报告指出，美国在明知存在击中民用物体的重大风险下仍下令打击该学校，行为鲁莽。 这是首批有据可查的真实案例之一，显示军事目标定位中过度依赖 AI 导致大规模平民伤亡，加剧了全球关于责任归属、自主武器以及 AI 能否为致命错误负责的争论。此事可能加速推动对 AI 赋能战争的国际监管，并改变军方对算法目标决策的论证与审查方式。 报告指出，部分五角大楼人员在数小时内就得知美军击中了学校，并描述了一系列与 Palantir 所建 AI 工具相关的本可避免的失误。批评者警告，AI 军事目标定位的速度可能超出人类核实能力，而五角大楼 2026 年 AI 战略要求成为“AI 优先”的作战力量，引发了对人类监督被削弱的担忧。

hackernews · devonnull · 9月22日 19:03 · [社区讨论](https://news.ycombinator.com/item?id=49806430)

**背景**: 军事 AI 目标定位系统（如 Maven Smart System）利用机器学习分析监视数据并识别目标，承诺实现更快、更精准的“杀伤链”。国际法要求作战方核实目标为军事目标，并采取可行预防措施避免平民伤害，但自主或 AI 辅助武器造成了“责任缺口”，因为现行法律规则难以在机器选定目标时确定责任归属。过去十年，美国日益将 AI 整合进情报分析与目标定位，批评者认为这已超出有意义的人类监督。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gizmodo.com/pentagon-investigators-say-overreliance-on-palantir-ai-tech-contributed-to-u-s-strike-that-killed-123-iranian-children-2000814477">Pentagon Investigators Say Overreliance on Palantir AI Tech...</a></li>
<li><a href="https://www.brennancenter.org/our-work/research-reports/militarys-use-ai-explained">The Military’s Use of AI, Explained | Brennan Center for Justice</a></li>
<li><a href="https://lieber.westpoint.edu/legal-accountability-ai-driven-autonomous-weapons/">Legal Accountability for AI-Driven Autonomous Weapons - Lieber Institute West Point</a></li>

</ul>
</details>

**社区讨论**: 评论者大多拒绝将 AI 视为罪魁祸首，认为选择将致命决策权交给 AI 的人类必须承担责任，并批评报告措辞粉饰了某些人所说的“大规模谋杀”。多人对后续打击的理由以及缺乏对急救人员的保护表示担忧，也有人认为 AI 被当作人类犯罪行为的“替罪羊”。

**标签**: `#AI ethics`, `#military AI`, `#accountability`, `#AI safety`, `#autonomous weapons`

---

<a id="item-4"></a>
## [OpenAI GPT-6 Astra 据称破解长期未解的恩尼格玛密文](https://www.cryptocellar.org/bgac/the-mvueh-break.html) ⭐️ 8.0/10

据 cryptocellar.org 的一篇文章称，OpenAI 的 GPT-6 Astra 成功解密了一条自 2005 年以来一直未被破解的恩尼格玛密文。这一成果在 Hacker News 上引发了 634 分、381 条评论的热烈讨论，争论焦点是这一成就应归功于 AI 多少。 如果得到证实，这将是 AI 驱动密码分析的一个重要里程碑，表明前沿模型能够解决困扰人类破译者近二十年的难题。同时，它也加剧了关于 AI 自主性的广泛争论，因为质疑者认为大部分工作被转交给了 AI 生成的恩尼格玛模拟软件。 解密出的文本为“BTTE UM ANGABE DES MARSQWEGES X BEFINDE MIQ IN X ROSENOW ROSENOW X SOFORT FUNKANTWORT X WASCHBBSCH”，考虑拼写错误后，大意是请求说明行军路线，并要求从 Rosenow 立即通过无线电回复。评论者指出，Gemini 3.8 Flash 据称在约 45 分钟内完成了类似任务，并质疑 Astra 生成的 Python/C++ 恩尼格玛模拟器代码有多少是原创的。

hackernews · sohkamyung · 9月22日 13:52 · [社区讨论](https://news.ycombinator.com/item?id=49801324)

**背景**: 恩尼格玛机是二战期间纳粹德国使用的转子式密码设备，破解它是以艾伦·图灵等人在布莱切利园主导的关键盟军行动。恩尼格玛的密码分析通常利用已知明文、报文结构和机器设置，而一些报文——尤其是较短或加密方式含糊的——数十年来一直未被破解。GPT-6 Astra 是 OpenAI 最新的前沿模型，号称在网络安全和软件工程等领域达到最先进水平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cryptanalysis_of_the_Enigma">Cryptanalysis of the Enigma - Wikipedia</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>
<li><a href="https://cryptii.com/pipes/enigma-machine/">The Enigma machine : Encrypt and decrypt online - cryptii</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者大多持怀疑态度：tantalor 认为“完全靠自己完成”与 Astra 自行编写恩尼格玛模拟软件的说法自相矛盾，并质疑破解过程有多少被外包给了软件。podgorniy 报告称 Gemini 3.8 Flash 在约 45 分钟内一次性完成了类似解密，其他人则分享了破解出的报文，并提到 Veritasium 最近发布的关于恩尼格玛的视频。

**标签**: `#AI`, `#cryptanalysis`, `#Enigma`, `#OpenAI`, `#GPT-6`

---

<a id="item-5"></a>
## [ShinyHunters 声称入侵 FBI 并窃取全部员工数据](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/) ⭐️ 8.0/10

黑客组织 ShinyHunters 声称已入侵 FBI 系统并获取了全部 FBI 员工的数据，据称是通过利用 PeopleSoft 的零日漏洞，并借此访问了 FBI 的 AWS GovCloud 环境。该组织还篡改了一个网站页面，留下“此网站已被 ShinyHunters 接管”的字样，并表示其目的“并非出于经济动机”，可能更接近“胁迫”而非勒索。 如果得到证实，这将是近年来最严重的美国政府数据泄露事件之一，涉及全部 FBI 员工，可能使联邦执法人员的个人和履历信息暴露给外国情报机构和犯罪分子。这也再次引发人们对政府机构所使用的第三方企业软件和云环境安全性的质疑。 ShinyHunters 声称数据来自 PeopleSoft 被攻破后所访问的系统，其中包括用于存储员工和申请人信息的 FBI AWS GovCloud 环境。该组织尚未公开泄露数据，其“非经济动机”的说法以及“胁迫”威胁均未得到证实。

hackernews · spenvo · 9月22日 17:46 · [社区讨论](https://news.ycombinator.com/item?id=49805278)

**背景**: ShinyHunters 是一个知名黑客组织，此前曾声称对 AT&T、Ticketmaster 等公司的数据泄露事件负责。PeopleSoft 是 Oracle 的企业人力资源和校园管理软件，被政府机构和大学广泛使用，此类软件中的零日漏洞可能让攻击者获得进入相关云系统的立足点。2015 年美国人事管理局（OPM）数据泄露事件暴露了 2210 万名美国政府雇员的记录，常被引为这类入侵可能造成大规模损害的例证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/">ShinyHunters claims FBI hack, data theft in PeopleSoft zero-day breach</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rhysida_(hacker_group)">Rhysida (hacker group) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Archive.today">archive.today - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者大多对黑客的可信度和动机持怀疑态度，有人开玩笑说该组织错过了宣称“AI 智能体集群”自主完成入侵的机会。也有人将其与 2015 年 OPM 泄露事件相提并论，认为没有哪个大型数据库是真正安全的；还有人指出，该组织用“胁迫”而非勒索的说法颇为反常。

**标签**: `#cybersecurity`, `#data breach`, `#FBI`, `#hacking`, `#privacy`

---

<a id="item-6"></a>
## [OpenAI 为 GPT-6 推出改进版提示缓存](https://openai.com/index/better-prompt-caching-for-gpt-6) ⭐️ 8.0/10

OpenAI 宣布为 GPT-6 推出改进版提示缓存，具备更高的缓存命中率、新的诊断工具、显式断点，以及旨在降低 API 用户延迟和成本的控制选项。 提示缓存是降低大模型推理成本和延迟最有效的手段之一，因此这些改进会直接影响在 GPT-6 上构建生产级应用的开发者，尤其是那些反复发送共享系统提示、模板或文档的场景。 显式断点允许开发者精确标记可缓存前缀的结束位置，断点之后的内容（例如用户对话）不会被写入缓存，从而避免不必要的缓存写入费用；新的诊断功能则帮助团队监控缓存健康状况和命中率。

rss · OpenAI News · 9月22日 21:00

**背景**: 提示缓存（也称前缀缓存或上下文缓存）将 KV 缓存扩展到跨请求复用，使共享的系统提示或文档只需处理一次，就能在多次调用中重复使用，而不必每次重新计算。服务商通常对缓存命中的输入 token 收取更低费用，因此缓存命中率成为关键的成本指标。OpenAI 此前的 API 已支持提示缓存，本次更新则针对 GPT-6 做了进一步优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/better-prompt-caching-for-gpt-6/">Better prompt caching for GPT‑6 - OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/prompt-caching">Prompt caching | OpenAI API</a></li>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/prompt-caching">Prompt caching - Claude Platform Docs</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-6`, `#prompt caching`, `#LLM inference`, `#API optimization`

---

<a id="item-7"></a>
## [Parallel 借助 GPT-6 Astra 将研究时间和成本减半](https://openai.com/index/parallel-cuts-time-and-cost-with-astra) ⭐️ 8.0/10

OpenAI 宣布，其新模型 GPT-6 Astra 使 Parallel 的 AI 智能体在研究和综合劳动力市场数据时，相比此前模型将时间和成本都减半。在一项测试中，Parallel 的智能体研究了四个州、六个月内的六项不同劳动力市场统计数据。 智能体研究任务在时间和成本上双双减半，表明前沿模型能够显著降低 AI 驱动自动化的经济成本，这可能加速研究型智能体在金融、市场情报及其他数据密集型行业中的采用。 该案例研究是 OpenAI 的宣传性示例，而非独立基准测试，且对比对象是未指明的此前模型。GPT-6 Astra 于 2026 年 9 月 3 日向获批用户首次发布，次日全面开放；其 API 定价基于 token 用量，搜索和计算机使用等工具还需按调用次数额外收费。

rss · OpenAI News · 9月22日 12:00

**背景**: GPT-6 Astra 是 OpenAI 开发的大型语言模型，在计算机使用、浏览、软件工程、网络安全、科学和专业工作方面被定位为最先进水平。Parallel 是一家构建研究型 AI 智能体的公司，其业务包括金融和劳动力市场数据研究，并提供带引用和来源的答案。智能体研究指的是 AI 系统自主规划、搜索并综合信息以完成多步骤研究任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/parallel-cuts-time-and-cost-with-astra/">Parallel cut research time and cost in half with GPT‑6 Astra | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 - Wikipedia</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>

</ul>
</details>

**标签**: `#GPT-6`, `#OpenAI`, `#AI agents`, `#cost efficiency`, `#research automation`

---

<a id="item-8"></a>
## [John Platt 谈 AI 驱动科学、气候变化与超级智能](https://www.latent.space/p/john-platt) ⭐️ 7.0/10

Latent Space 播客发布了对 Google Fellow、气候与科学方向技术负责人 John Platt 的访谈，讨论了如何用 AI 自动化科学发现、应对气候变化，以及在超级智能 AI 时代后代如何为科学做贡献。Platt 最著名的成就是提出了用于训练支持向量机的 SMO 算法和用于模型概率校准的 Platt scaling，这两者至今仍被 scikit-learn 广泛使用。 Platt 的观点之所以重要，是因为他横跨基础机器学习研究与高影响力的应用科学，他提出的将科学问题简化为“可评分任务”的概念，为利用 AI 加速科学发现提供了具体框架。他对气候变化和超级智能 AI 的看法也会影响 Google 等大型实验室的研究方向优先级。 Platt 描述了一种模式：许多科学问题都可以被简化为“可评分任务”——一旦有了评分函数，目标就变成寻找能最大化该分数的代码。他是领导气候与科学两项工作的 Google Fellow，其 SMO 算法和 Platt scaling 至今仍是 scikit-learn 中的标准组件。

rss · Latent Space · 9月22日 21:07

**背景**: John Platt 是 Google 的计算机科学家，以序列最小优化（SMO）算法和 Platt scaling 闻名。SMO 是一种快速训练支持向量机（SVM）的方法，而 Platt scaling 则把分类器输出转换为概率分布。这两种技术都被实现在流行的开源 Python 机器学习库 scikit-learn 中。“AI for Science”指利用机器学习加速科学发现，而“超级智能 AI”则指在所有领域都超越人类智能的假想 AI。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/people/johnplatt/">John C. Platt</a></li>
<li><a href="https://en.wikipedia.org/wiki/Platt_scaling">Platt scaling - Wikipedia</a></li>
<li><a href="https://www.latent.space/p/john-platt">🔬 An Oscar, Two Asteroids, and the Algorithm in Your sklearn: John Platt on AI for Science</a></li>

</ul>
</details>

**标签**: `#AI for Science`, `#Machine Learning`, `#Climate Change`, `#Superintelligent AI`, `#Interview`

---

<a id="item-9"></a>
## [JetBrains 推出 Air：面向智能体开发的开放系统](https://news.google.com/rss/articles/CBMijgFBVV95cUxPbHJtVWJ5UWtQdTVkZnF2VjBvcUV4RUpzWEVlRkRxazZFYXNQOFpJajNhSHdDMi1iYWh5UjJBdnJ5alJRSHIwQVZ5ZXhWeVZwemFqMEo2UUo0dURqdzB5aHNBRm9od1E4WGVkWnZPWGdzQXlQN3VKQmRUWG4yRzYyclUyblFwc0J2bnJwOGFn?oc=5) ⭐️ 7.0/10

2026 年 9 月 22 日，JetBrains 正式推出 JetBrains Air——一套面向智能体软件开发的开放产品体系，覆盖其 IDE、团队交付流程与组织治理层面，并与公司的 Junie 智能体协同。Air 被定位为“智能体开发环境”（Agentic Development Environment），开发者可将编码任务委派给 AI 智能体，同时保持对工作流的掌控，并且兼容用户已有的智能体以及任何符合 ACP 协议的智能体。 JetBrains 是使用最广泛的开发者工具厂商之一，将智能体开发打包为开放且与 IDE 深度集成的系统，可能会影响主流专业团队采用 AI 智能体的方式，而非依赖零散的第三方工具。对开放性和 ACP 兼容性的强调，也释放出在快速扩张的智能体生态中推动互操作性标准的信号。 Air 被定位为“用智能体构建软件的统一系统”，可配合开发者已在使用的智能体以及任何符合 ACP 协议的智能体，并延续了 2026 年 3 月推出的 JetBrains Central——面向智能体驱动开发的开放控制与执行系统。官方表述指出，智能体开发改变了软件的制造方式，却没有降低出错的代价，因此强调理解、修改和验证智能体生成的代码。

google_news · Unite.AI · 9月22日 11:40

**背景**: 智能体开发（agentic development）指的是由 AI 智能体自主执行多步骤编码任务（如编写、重构或测试代码）的工作流，而不仅仅是提供代码补全建议。JetBrains 是 IntelliJ IDEA、PyCharm 等主流 IDE 的开发商，已公开试验智能体开发环境约半年时间。ACP（Agent Client Protocol）是一项新兴接口标准，旨在让不同的 AI 智能体接入兼容的开发工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.jetbrains.com/blog/2026/09/22/introducing-jetbrains-air/">JetBrains Air: Building a System of Products for Agentic ...</a></li>
<li><a href="https://www.jetbrains.com/help/air/quick-start-with-air.html">Quickstart with Air | JetBrains Air Documentation</a></li>
<li><a href="https://blog.jetbrains.com/blog/2026/03/24/introducing-jetbrains-central-an-open-system-for-agentic-software-development/">Introducing JetBrains Central: An Open System for Agentic ...</a></li>

</ul>
</details>

**标签**: `#JetBrains`, `#agentic development`, `#AI agents`, `#developer tools`, `#open system`

---