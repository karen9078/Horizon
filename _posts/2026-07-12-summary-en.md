---
layout: default
title: "Horizon Summary: 2026-07-12 (EN)"
date: 2026-07-12
lang: en
---

> From 44 items, 15 important content pieces were selected

---

1. [xAI's Grok Build CLI Uploads Entire Repos Including .env Files](#item-1) ⭐️ 9.0/10
2. [GPT-5.6 Proves 50-Year-Old Graph Theory Conjecture in Under an Hour](#item-2) ⭐️ 9.0/10
3. [vLLM v0.25.0: Model Runner V2 Default, PagedAttention Removed](#item-3) ⭐️ 8.0/10
4. [RISCBoy: Open-Source RISC-V Handheld Console](#item-4) ⭐️ 8.0/10
5. [UPI Transaction Architecture Deep Dive](#item-5) ⭐️ 8.0/10
6. [Prefer STRICT Tables in SQLite](#item-6) ⭐️ 8.0/10
7. [VultronRetriever Models Top MTEB Leaderboard](#item-7) ⭐️ 8.0/10
8. [U-Boot Bootloader Flaws Allow Code Execution Before OS Boot](#item-8) ⭐️ 8.0/10
9. [Mesh LLM: Distributed AI Computing on Iroh](#item-9) ⭐️ 7.0/10
10. [Zhipu Founder Launches 'Touch High' Plan for AGI](#item-10) ⭐️ 7.0/10
11. [Claude Code Desktop Adds Built-in Browser](#item-11) ⭐️ 7.0/10
12. [Google Opposes European Site Blocking as US Piracy Laws Gain Momentum](#item-12) ⭐️ 7.0/10
13. [BrainCo bets on wearable BCI without brain surgery](#item-13) ⭐️ 7.0/10
14. [EU Plans Fines for Big Tech Over Consumer Protection Failures](#item-14) ⭐️ 7.0/10
15. [Microsoft and Google Back Go for AI Agents](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [xAI's Grok Build CLI Uploads Entire Repos Including .env Files](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) ⭐️ 9.0/10

A wire-level analysis of xAI's Grok Build CLI (version 0.2.93) reveals that the tool uploads the entire repository contents, including git history and sensitive files like .env, to xAI servers regardless of the 'Improve the model' toggle setting. This is a critical privacy violation because it exposes proprietary code and secrets to xAI even when users explicitly opt out of data collection, undermining trust in AI coding tools and raising serious security concerns for developers and organizations. The analysis shows that the CLI transmits file contents verbatim and unredacted, persists data to a named GCS bucket, and the upload mechanism is not disclosed in the CLI's setup materials. The 'Improve the model' toggle makes no difference — ON or OFF, the whole repo is uploaded the same way.

hackernews · jhoho · Jul 12, 01:09 · [Discussion](https://news.ycombinator.com/item?id=48877371)

**Background**: Grok Build CLI is a coding agent and terminal tool launched by xAI in May 2026, powered by Grok 4.5, designed to assist with complex software engineering tasks. It is available to SuperGrok and X Premium Plus subscribers. The tool is intended to read code and provide assistance, but users expect that when they disable data collection, their code is not sent to xAI servers.

<details><summary>References</summary>
<ul>
<li><a href="https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547">What xAI Grok Build CLI actually sends to xAI - a wire-level analysis (grok 0.2.93) · GitHub</a></li>
<li><a href="https://x.ai/news/grok-build-cli">Introducing Grok Build | SpaceXAI</a></li>
<li><a href="https://www.eigent.ai/blog/grok-build-cli">Grok Build CLI Review 2026: Features & Alternatives</a></li>

</ul>
</details>

**Discussion**: The community expressed shock and outrage, with many calling the behavior a 'mass surveillance campaign' and a severe security flaw. Some users noted they had chosen not to use xAI products due to such concerns, while others suggested sandboxing tools like bubblewrap to mitigate risks. There was also skepticism about the AI-generated analysis, with calls for independent verification.

**Tags**: `#privacy`, `#security`, `#xAI`, `#AI tools`, `#data leakage`

---

<a id="item-2"></a>
## [GPT-5.6 Proves 50-Year-Old Graph Theory Conjecture in Under an Hour](https://www.qbitai.com/2026/07/447873.html) ⭐️ 9.0/10

OpenAI's GPT-5.6 Sol Ultra autonomously proved the cycle double cover conjecture, a 50-year-old open problem in graph theory, in less than one hour. The model used 64 sub-agents working in parallel and generated a 3-page PDF proof. This marks the first time an AI has autonomously solved a long-standing open problem in mathematics, demonstrating advanced reasoning and multi-agent coordination. It could transform how mathematical research is conducted, with AI assisting or even leading discoveries. The proof transforms the problem into edge labeling and linear equations over finite fields, assigning two labels per edge such that edges with the same label form cycles. OpenAI also released the full 700-character prompt, which specifies acceptance criteria, definitions, boundary conditions, and failure cases without prescribing fixed steps.

telegram · zaihuapd · Jul 12, 03:49

**Background**: The cycle double cover conjecture asks whether every bridgeless graph (a graph with no edge whose removal disconnects the graph) has a collection of cycles that together cover each edge exactly twice. It was independently posed by Szekeres (1973) and Seymour (1979) and is a major open problem in graph theory. GPT-5.6's Sol Ultra mode features built-in multi-agent orchestration, allowing it to spawn 64 sub-agents to work on different parts of the problem simultaneously.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cycle_double_cover_conjecture">Cycle double cover conjecture</a></li>
<li><a href="https://chatforest.com/builders-log/openai-gpt-5-6-sol-ultra-mode-subagents-parallel-architecture-builder-guide/">GPT-5.6 Sol Ultra Mode: Built-In Multi-Agent Orchestration ...</a></li>
<li><a href="https://www.techtimes.com/articles/319808/20260707/gpt-56-sol-review-faster-coding-half-fable-5-cost-benchmark-problem.htm">GPT-5.6 Sol Review: Faster Coding, Half Fable 5 Cost, and a ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#graph theory`, `#LLM`, `#mathematical proof`, `#OpenAI`

---

<a id="item-3"></a>
## [vLLM v0.25.0: Model Runner V2 Default, PagedAttention Removed](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 8.0/10

vLLM v0.25.0 makes Model Runner V2 the default execution path for all dense models and removes the legacy PagedAttention implementation. The release also introduces new models like LLaVA-OneVision-2 and GLM-5, a Streaming Parser Engine, and universal speculative decoding for heterogeneous vocabularies. This release marks a major architectural shift in vLLM, improving performance and modularity while simplifying the codebase. The removal of PagedAttention, once a core innovation, signals the maturity of newer backends and sets a new standard for LLM inference efficiency. Model Runner V2 now supports EVS for efficient video token pruning, realtime embeddings, and dynamic speculative decoding with full CUDA graphs. The Transformers modeling backend has been optimized to match native vLLM speed, and new models include GLM-5, MiniMax-M3, and Hy3.

github · khluu · Jul 11, 20:06

**Background**: vLLM is an open-source library for high-throughput LLM inference and serving, originally developed at UC Berkeley. PagedAttention was its key innovation for managing attention key-value cache efficiently, but newer backends like Model Runner V2 have superseded it with better performance and modularity.

<details><summary>References</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM | vLLM Blog</a></li>
<li><a href="https://docs.vllm.ai/en/v0.22.1/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/paged_attention/">Paged Attention - vLLM</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#release`, `#performance`, `#open source`

---

<a id="item-4"></a>
## [RISCBoy: Open-Source RISC-V Handheld Console](https://github.com/Wren6991/RISCBoy) ⭐️ 8.0/10

RISCBoy is an open-source portable game console designed from scratch using the RISC-V instruction set architecture, created by Raspberry Pi engineer Luke Wren. It is described as a Gameboy Advance from an alternate universe where RISC-V existed in 2001. This project showcases the potential of RISC-V in embedded systems and retro gaming, combining an open-source ISA with a nostalgic form factor. It highlights the growing ecosystem of RISC-V hardware and could inspire more open-source gaming devices. The console is built entirely from scratch, including the RISC-V core, and is fully open-source with hardware design files available on GitHub. It uses AHB/APB bus protocols, which are typically associated with ARM but are actually open standards.

hackernews · mariuz · Jul 11, 21:58 · [Discussion](https://news.ycombinator.com/item?id=48876245)

**Background**: RISC-V is a free and open instruction set architecture (ISA) that anyone can implement without royalties, unlike proprietary ISAs like ARM and x86. The Gameboy Advance was a popular 32-bit handheld console released by Nintendo in 2001, featuring an ARM7 CPU and backward compatibility with Game Boy games. RISCBoy emulates this experience using a modern open-source ISA.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V">RISC-V - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/RISC-V_architecture">RISC-V architecture</a></li>

</ul>
</details>

**Discussion**: The community praised the project for its technical depth and novelty, with comments noting the creator's previous work on PicoDVI (DVI/HDMI from RP2040). Some were surprised that AHB/APB protocols are open, not ARM-proprietary, highlighting a common misconception.

**Tags**: `#RISC-V`, `#open-source hardware`, `#retro gaming`, `#embedded systems`

---

<a id="item-5"></a>
## [UPI Transaction Architecture Deep Dive](https://timeseriesofindia.com/economy/reads/upi-architecture/) ⭐️ 8.0/10

An article provides an in-depth analysis of UPI's transaction architecture, covering its design, intermediaries, and scalability, with community discussion on privacy and global comparisons. This analysis matters because UPI is India's dominant real-time payment system, processing billions of transactions monthly, and understanding its architecture helps engineers and policymakers assess its strengths and weaknesses. The article notes that UPI handles about 22 billion transactions per year, averaging ~700 QPS at the NPCI switch, with peak loads potentially much higher, and features a crore/billion toggle for readability.

hackernews · prtk25 · Jul 11, 16:33 · [Discussion](https://news.ycombinator.com/item?id=48873457)

**Background**: UPI (Unified Payments Interface) is an Indian instant payment system developed by NPCI in 2016. It enables inter-bank peer-to-peer and person-to-merchant transactions via mobile phones, using a virtual payment address linked to a bank account. The system involves multiple intermediaries, including the payer's bank, payee's bank, and NPCI as the central switch.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unified_Payments_Interface">Unified Payments Interface - Wikipedia</a></li>
<li><a href="https://medium.com/@avinashkariya05910/deep-dive-system-design-of-upi-unified-payments-interface-eff3b0334b0d">Deep Dive: System Design of UPI (Unified Payments Interface) | by Avinash Kariya | Medium</a></li>
<li><a href="https://www.thesgn.blog/blog/upi">UPI System Design Explained | High-Level Architecture of ...</a></li>

</ul>
</details>

**Discussion**: Community comments highlight privacy concerns due to multiple intermediaries and identity linkage, while praising UPI's success in driving digital adoption among elderly users. Some compare its QPS (700) unfavorably to systems like Nasdaq's 100k+ QPS, but note that peak loads are higher. The crore/billion toggle is appreciated as a UX improvement.

**Tags**: `#UPI`, `#payment systems`, `#architecture`, `#scalability`, `#privacy`

---

<a id="item-6"></a>
## [Prefer STRICT Tables in SQLite](https://evanhahn.com/prefer-strict-tables-in-sqlite/) ⭐️ 8.0/10

A guide by Evan Hahn advocates for using STRICT tables in SQLite to enforce data types, preventing common mistakes like inserting text into integer columns. The article highlights that STRICT tables, introduced in SQLite 3.37.0, provide rigid type checking. This matters because SQLite's default flexible typing can lead to data corruption, especially in multi-application or production environments. Adopting STRICT tables improves data integrity and aligns SQLite with traditional SQL databases, making it more reliable for serious use. STRICT tables only allow columns of types INT, INTEGER, REAL, TEXT, BLOB, or ANY, and reject type mismatches on insert/update. However, there is no ALTER TABLE to convert an existing table to STRICT; you must copy data to a new table, as noted by community member simonw.

hackernews · ingve · Jul 11, 17:33 · [Discussion](https://news.ycombinator.com/item?id=48873940)

**Background**: SQLite traditionally uses dynamic typing, where column types are suggestions rather than strict rules. This flexibility allows storing any value in any column, but can lead to data integrity issues. STRICT tables, introduced in version 3.37.0 (2021-11-27), enforce rigid type enforcement, making SQLite behave more like traditional SQL databases.

<details><summary>References</summary>
<ul>
<li><a href="https://sqlite.org/stricttables.html">STRICT Tables - SQLite</a></li>
<li><a href="https://sqlite.org/datatype3.html">Datatypes In SQLite</a></li>
<li><a href="https://evanhahn.com/prefer-strict-tables-in-sqlite/">Prefer STRICT tables in SQLite - evanhahn.com</a></li>

</ul>
</details>

**Discussion**: Community members like simonw and dfabulich engaged in a nuanced debate. simonw created a tool to convert non-strict tables to strict, while dfabulich linked to SQLite's official stance on flexible typing, arguing that the benefits of flexible typing often outweigh the risks. Others expressed a desire for STRICT to become the default, citing enterprise reliability concerns.

**Tags**: `#SQLite`, `#database`, `#data integrity`, `#best practices`

---

<a id="item-7"></a>
## [VultronRetriever Models Top MTEB Leaderboard](https://www.reddit.com/r/MachineLearning/comments/1utmxq8/vultronretriever_family_of_models_released_on/) ⭐️ 8.0/10

VultronRetriever family of embedding models (Prime-8B, Core-4.5B, Flash-0.8B) has been released on HuggingFace, achieving #1 on the MTEB leaderboard in their respective classes, with up to 16x smaller index storage and 12x higher throughput compared to previous 9B-class leaders. These models demonstrate that state-of-the-art retrieval performance can be achieved with dramatically reduced resource requirements, enabling fully offline deployment on edge devices like iPhones, which could democratize access to high-quality semantic search and retrieval-augmented generation (RAG) systems. The VultronRetrieverPrime-8B model uses the Hydra Architecture for late interaction retrieval, which provides high precision at up to half the memory of comparable models. All models were trained on datasets with 0% cross-dataset duplication and 0% evaluation contamination, showing no overfitting on private MTEB evaluations.

reddit · r/MachineLearning · /u/madkimchi · Jul 11, 15:22

**Background**: The MTEB (Massive Text Embedding Benchmark) leaderboard is a widely recognized benchmark for evaluating text embedding models on various tasks including retrieval, clustering, and classification. Late interaction retrieval, pioneered by models like ColBERT, uses token-level representations to enable more precise matching than single-vector embeddings, at the cost of larger index sizes. The Hydra Architecture is a novel approach that combines late interaction retrieval with efficient generation.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/spaces/mteb/leaderboard">MTEB Leaderboard - a Hugging Face Space by mteb</a></li>
<li><a href="https://weaviate.io/blog/late-interaction-overview">An Overview of Late Interaction Retrieval Models: ColBERT ...</a></li>
<li><a href="https://docs.hydra.so/intro/architecture">Architecture - Hydra</a></li>

</ul>
</details>

**Tags**: `#embedding models`, `#MTEB leaderboard`, `#efficient retrieval`, `#offline AI`, `#HuggingFace`

---

<a id="item-8"></a>
## [U-Boot Bootloader Flaws Allow Code Execution Before OS Boot](https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/) ⭐️ 8.0/10

Six vulnerabilities were discovered in U-Boot's FIT signature verification code, with two enabling arbitrary code execution and four causing denial of service. The flaws affect over 50 stable releases since v2013.07 and numerous downstream vendor branches. These vulnerabilities allow attackers to execute malicious code before the operating system and security software start, enabling stealthy firmware attacks that can disable security features or implant persistent malware. Systems with remote firmware update capabilities, such as BMCs, are particularly at risk as they can be exploited without physical access. The vulnerabilities are tracked as BRLY-2026-037 through BRLY-2026-042. Patches have been submitted and accepted by U-Boot maintainers, but deployment depends on hardware vendors integrating them into firmware updates; end-of-life devices may never receive fixes.

telegram · zaihuapd · Jul 11, 08:32

**Background**: U-Boot is a widely used open-source bootloader for embedded devices, responsible for loading the operating system. FIT (Flattened Image Tree) is a format for packaging kernel, device tree, and other images with cryptographic signatures to ensure authenticity. The vulnerabilities reside in the signature verification logic, which is supposed to prevent unauthorized code from being executed during boot.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.u-boot-project.org/en/latest/usage/fit/signature.html">U - Boot FIT Signature Verification — Das U - Boot unknown version...</a></li>
<li><a href="https://cybersecuritynews.com/u-boot-fit-signature-verification/">Six U - Boot FIT Signature Verification Flaws Enable Code Execution...</a></li>
<li><a href="https://thehackernews.com/2026/07/six-new-u-boot-flaws-could-let.html">Six New U - Boot Flaws Could Let Malicious Images Crash Devices or...</a></li>

</ul>
</details>

**Tags**: `#security`, `#firmware`, `#U-Boot`, `#vulnerability`, `#bootloader`

---

<a id="item-9"></a>
## [Mesh LLM: Distributed AI Computing on Iroh](https://www.iroh.computer/blog/mesh-llm) ⭐️ 7.0/10

Mesh LLM is a new open-source project that pools heterogeneous devices (laptops, servers, cloud nodes) to perform distributed LLM inference, exposing an OpenAI-compatible API via the iroh networking library. This approach democratizes access to large language models by allowing users to combine modest local hardware into a powerful inference cluster, reducing reliance on expensive cloud GPUs. The project uses iroh's peer-to-peer networking to connect devices by cryptographic keys, and the skippy engine splits large models across nodes. Performance claims include 16 tok/s for Qwen 235B MoE across 2 nodes.

hackernews · tionis · Jul 11, 22:38 · [Discussion](https://news.ycombinator.com/item?id=48876505)

**Background**: Iroh is a Rust-based peer-to-peer networking library that routes connections by cryptographic key rather than IP address, enabling direct device-to-device communication even behind NATs. Mesh LLM leverages iroh to create a distributed inference mesh without centralized servers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.iroh.computer/blog/mesh-llm">Mesh LLM: distributed AI computing on iroh - Iroh</a></li>
<li><a href="https://github.com/Mesh-LLM/mesh-llm">GitHub - Mesh-LLM/mesh-llm: Distributed AI/LLM for the people ...</a></li>
<li><a href="https://www.iroh.computer/blog/v1">Iroh 1.0 - Dial Keys, not IPs - Iroh</a></li>

</ul>
</details>

**Discussion**: Community comments express interest in distributed inference for small models and skepticism about performance over consumer networks. A contributor noted the skippy engine and confirmed 16 tok/s for Qwen 235B MoE across 2 nodes.

**Tags**: `#distributed computing`, `#LLM inference`, `#peer-to-peer`, `#AI infrastructure`, `#iroh`

---

<a id="item-10"></a>
## [Zhipu Founder Launches 'Touch High' Plan for AGI](https://mp.weixin.qq.com/s/3CQSkf_kBnXiCDgS4L-Cgg) ⭐️ 7.0/10

Zhipu AI founder Tang Jie announced the 'Touch High' plan, committing billions of yuan to research on mechanistic interpretability to make black-box models transparent. The plan outlines four key challenges for AGI: long-horizon tasks, autonomous agent systems, fully self-training, and extreme safety governance. This initiative signals a major shift in China's AI landscape toward fundamental AGI research rather than short-term commercialization. Success in mechanistic interpretability could unlock safer and more controllable AI systems, benefiting the entire open-source community. Zhipu's GLM-5.2 model is already considered close to the frontier of overseas models and is popular in the open-source community. The company plans to invest billions of yuan specifically in mechanistic interpretability, aiming to open the 'black box' of large language models.

telegram · zaihuapd · Jul 11, 13:59

**Background**: Mechanistic interpretability aims to understand how neural networks produce specific outputs by analyzing internal components like neurons and features. Current large language models are often seen as 'black boxes' because their decision-making processes are opaque, even when the model weights are open-source. Zhipu AI is a leading Chinese AI company known for its open-source GLM series models.

<details><summary>References</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/32774980722">2030年的大模型将会是什么样的？机械可解释性又是什么？</a></li>
<li><a href="https://www.zyxy.net/archives/24191">机械可解释性（Mechanistic Interpretability）：利用稀疏自编码器（S...</a></li>
<li><a href="https://www.bestblogs.dev/article/81379ea0">致开发者： GLM - 5 . 2 全量开放，前沿 智 能属于所有人 | BestBlogs.dev</a></li>

</ul>
</details>

**Tags**: `#AGI`, `#AI research`, `#智谱`, `#mechanical interpretability`, `#open source`

---

<a id="item-11"></a>
## [Claude Code Desktop Adds Built-in Browser](https://x.com/ClaudeDevs/status/2075635283211772279) ⭐️ 7.0/10

Claude Code Desktop now includes a built-in browser that allows users to open and interact with websites directly within the application, such as reading documentation, viewing design mockups, or testing local development servers. This feature streamlines the AI-assisted coding workflow by eliminating the need to switch between the IDE and an external browser, enabling Claude to access web resources in real time and improving developer productivity. The built-in browser is sandboxed for security, and users can configure whether to retain browsing sessions. It supports clicking and interacting with web pages, similar to working with a local development server.

telegram · zaihuapd · Jul 11, 14:34

**Background**: Claude Code Desktop is a desktop application that provides a dedicated environment for AI-assisted software development, featuring Chat, Cowork, and Code tabs. The new built-in browser extends its capabilities by allowing Claude to directly fetch and interact with online resources, which is especially useful for tasks like reading API documentation or previewing web designs. Sandboxing is a security technique that isolates the browser process to prevent malicious content from affecting the host system.

<details><summary>References</summary>
<ul>
<li><a href="https://code.claude.com/docs/zh-CN/desktop">Desktop application - Claude Code Docs</a></li>
<li><a href="https://code.claude.com/docs/en/desktop">Desktop application - Claude Code Docs</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/519213813">浏览器沙盒--它是什么，我们为什么需要它？ - 知乎 如何在谷歌浏览器中使用安全沙箱 - CSDN博客 沙盘 (Sandboxie)64位5.64.3-沙盘 (Sandboxie)官方最新下载_3DM软件 沙盒浏览器 - Windows官方下载 | 微软应用商店 | Microsoft Store 浏览器沙箱（sandBox）到底是什么？ - 知乎 沙盘双开器下载-Sandboxie（沙盘双开器）正式版下载 [电脑版]-pc下载...</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#AI辅助编程`, `#桌面版更新`, `#浏览器集成`

---

<a id="item-12"></a>
## [Google Opposes European Site Blocking as US Piracy Laws Gain Momentum](https://torrentfreak.com/google-opposes-site-blocking-in-europe-as-u-s-piracy-blocking-plans-gain-momentum/) ⭐️ 7.0/10

Google formally submitted a filing to the European Commission opposing the expansion of site-blocking measures, arguing that blocking DNS resolvers, IP addresses, and VPNs is ineffective and disproportionate, often overblocking legitimate services. Meanwhile, similar anti-piracy legislation is gaining traction in the US Congress, with Representative Issa planning to advance a site-blocking bill. This highlights a growing global debate over internet censorship and anti-piracy enforcement, with major tech companies like Google pushing back against broad blocking measures. The outcome could affect internet infrastructure, digital rights, and how online piracy is tackled worldwide. Google's filing cited examples from Italy's anti-piracy system, which mistakenly blocked Google Drive subdomains and Cloudflare IP addresses hosting 42 million domains. Google has not yet publicly commented on the US legislative plans, but its EU filing argues that better legal alternatives, not broader blocking, should be the focus.

telegram · zaihuapd · Jul 11, 15:10

**Background**: Site blocking involves ISPs or DNS providers preventing access to certain websites, often used to combat piracy. DNS resolvers translate domain names into IP addresses; blocking them can disrupt access to many sites. Overblocking occurs when legitimate services are inadvertently blocked along with infringing ones.

**Tags**: `#site blocking`, `#Google`, `#anti-piracy`, `#internet policy`, `#legislation`

---

<a id="item-13"></a>
## [BrainCo bets on wearable BCI without brain surgery](https://www.cnbc.com/2026/07/11/chinas-brainco-bets-on-wearable-brain-tech.html) ⭐️ 7.0/10

Chinese BCI company BrainCo is focusing on non-invasive wearable brain-computer interfaces using dry electrodes and AI to decode weak EEG signals, targeting prosthetics, medical conditions, and eventually consumer electronics. This approach offers a safer, more accessible alternative to invasive BCIs like Neuralink, potentially accelerating adoption in medical rehabilitation and consumer wellness. It also highlights China's growing role in the global BCI industry. BrainCo has an FDA-approved bionic hand that reads neuromuscular signals from amputees, and a sleep-aid device using low-frequency electrical pulses. The company plans to license its BCI platform to other enterprises as a major future revenue source.

telegram · zaihuapd · Jul 11, 15:49

**Background**: Brain-computer interfaces (BCIs) enable direct communication between the brain and external devices. Non-invasive BCIs use sensors placed on the scalp to detect EEG signals, which are weak and noisy, requiring advanced signal processing and AI decoding. Dry electrodes eliminate the need for conductive gel, improving comfort and usability.

<details><summary>References</summary>
<ul>
<li><a href="https://wearablesensing.com/">Home - Wearable Sensing | Dry EEG</a></li>
<li><a href="https://www.nature.com/articles/s42003-025-08511-z">Progress, challenges and future of linguistic neural decoding ...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12791105/">Non-Invasive Brain-Computer Interfaces: Converging Frontiers ...</a></li>

</ul>
</details>

**Tags**: `#brain-computer interface`, `#non-invasive BCI`, `#AI`, `#prosthetics`, `#wearable tech`

---

<a id="item-14"></a>
## [EU Plans Fines for Big Tech Over Consumer Protection Failures](https://www.ft.com/content/25640be5-a5bd-4548-81f9-bd0e16f87f35) ⭐️ 7.0/10

EU Justice Commissioner Michael McGrath announced that the European Commission plans to propose new rules by the end of this year to strengthen online consumer protection, targeting addictive design, subscription traps, and other dark patterns. The EU also seeks enforcement powers to fine large tech companies for cross-border systemic violations. This marks a significant regulatory escalation that could force major tech platforms to redesign user interfaces and business practices to avoid hefty fines. It also extends consumer protection beyond existing digital regulations, potentially affecting smaller online merchants and game developers. McGrath noted that current consumer protection rules enforced by member states have never resulted in fines, failing to deter violations. The EU is also debating whether to impose social media bans on young users.

telegram · zaihuapd · Jul 12, 06:25

**Background**: Dark patterns are user interface designs that trick users into taking actions they did not intend, such as making unwanted purchases or signing up for recurring subscriptions. Addictive design refers to features like infinite scroll, push notifications, and variable rewards that are intentionally crafted to maximize user engagement, often at the expense of user well-being. The EU has been at the forefront of regulating digital platforms, with laws like the Digital Services Act and the Digital Markets Act already imposing obligations on large tech companies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dark_pattern">Dark pattern - Wikipedia</a></li>
<li><a href="https://commission.europa.eu/topics/consumers/consumer-rights-and-complaints/enforcement-consumer-protection_en">Enforcement of consumer protection - European Commission</a></li>

</ul>
</details>

**Tags**: `#EU regulation`, `#consumer protection`, `#big tech`, `#dark patterns`, `#online safety`

---

<a id="item-15"></a>
## [Microsoft and Google Back Go for AI Agents](https://news.google.com/rss/articles/CBMiYkFVX3lxTE10ZkNTb0tGVnFXQVRyMWttSkdNekIwLW4yeWhseV9nVkliZkxYV0JjY29NN2NBX3QxMGdTYURWekFZVGhVN1ZQWHhFd0NvVl81LU1jYmxyb0tKSTZRbGdVdmZ3?oc=5) ⭐️ 7.0/10

Microsoft has joined Google in endorsing the Go programming language for developing AI agents, while OpenAI and Anthropic have not yet adopted it. This alignment of major tech companies on Go for AI agents signals a potential shift in the industry, as Go's performance and concurrency features may offer advantages over Python for agentic workloads. The news comes from a report by The New Stack, noting that Go's efficiency and simplicity make it attractive for building scalable AI agents, though OpenAI and Anthropic continue to rely on Python.

google_news · The New Stack · Jul 11, 14:04

**Background**: AI agents are autonomous systems that use AI to perform tasks, often requiring high concurrency and low latency. Go, developed by Google, is known for its fast compilation, goroutines for concurrency, and ease of deployment, making it a strong candidate for agent infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://pub.huizhou92.com/why-go-might-be-a-better-language-than-python-for-ai-agent-development-722119dd9028">Why Go Might Be a Better Language Than Python for AI Agent ...</a></li>

</ul>
</details>

**Tags**: `#Go`, `#AI agents`, `#Microsoft`, `#Google`, `#programming languages`

---