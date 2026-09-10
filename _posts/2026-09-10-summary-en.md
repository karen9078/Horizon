---
layout: default
title: "Horizon Summary: 2026-09-10 (EN)"
date: 2026-09-10
lang: en
---

> From 36 items, 9 important content pieces were selected

---

1. [Calif Research Unveils WeWorm, First Zero-Click Worm via WeChat Calls](#item-1) ⭐️ 9.0/10
2. [OpenAI Announces GPT-6 Astra, Its Most Capable Business Model](#item-2) ⭐️ 9.0/10
3. [vLLM v0.29.0 Makes Model Runner V2 Default, Adds 770B MoE Support](#item-3) ⭐️ 8.0/10
4. [Apple Announces iPhone Duo, Its First Foldable iPhone](#item-4) ⭐️ 8.0/10
5. [Show HN: Interactive Visualization Scales Speed of Light to 5 km/h](#item-5) ⭐️ 8.0/10
6. [Shopify acquires Tailwind Labs, makers of Tailwind CSS](#item-6) ⭐️ 8.0/10
7. [Raschka Demystifies GPT-6 Astra, Looped Transformers, and Hidden Reasoning](#item-7) ⭐️ 8.0/10
8. [Automattic Board Forces CEO Matt Mullenweg Into Leave of Absence](#item-8) ⭐️ 8.0/10
9. [IBM Releases SOTA Granite Time Series PatchTST-FM-r2 with Commercial-Friendly License](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Calif Research Unveils WeWorm, First Zero-Click Worm via WeChat Calls](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research released a demo of WeWorm, described as the first zero-click worm that spreads through WeChat calls on both iOS and Android, hijacking accounts without the victim answering or interacting with their phone. The team used AI to find the bug and write the first remote code execution (RCE) exploit in about two days, then built the full worm in roughly one more week. This demonstrates a paradigm shift in exploit development: a worm that once required a larger team and months of work was built by a small team in about a week with AI assistance, raising major concerns about AI-accelerated cyber threats affecting WeChat's roughly 1.4 billion users. It also highlights how AI lowers the barrier to creating sophisticated, self-spreading attacks. The attack exploits a memory corruption vulnerability in WeChat's Voice-over-IP (VoIP) stack, compromising a target's account in seconds; even if the victim answers the call, they hear nothing and the exploit still succeeds. Calif demonstrated the worm spreading among three test phones, and the research was published on September 8, 2026.

rss · Simon Willison · Sep 10, 00:56

**Background**: A zero-click exploit requires no action from the victim, making it far more dangerous than attacks that rely on tricking users into clicking links or opening files. A worm is self-replicating malware that spreads automatically from device to device, and remote code execution (RCE) means an attacker can run arbitrary code on a target system. WeChat is a massively popular messaging app in China with roughly 1.4 billion users, and its VoIP calling feature is the vector here.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html">WeChat Zero-Click Worm Took Over Accounts on iPhone and Android via Incoming Calls</a></li>
<li><a href="https://cyberinsider.com/zero-click-worm-spreads-on-iphones-and-android-via-wechat-calls/">Zero-click worm spreads on iPhones and Android via WeChat calls</a></li>
<li><a href="https://www.ibtimes.com/wechats-14-billion-users-faced-dangerous-security-flaw-ai-helped-turn-it-self-spreading-worm-3807225">WeChat’s 1.4 Billion Users Faced a Dangerous Security Flaw ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#AI`, `#exploit`, `#WeChat`, `#zero-click`

---

<a id="item-2"></a>
## [OpenAI Announces GPT-6 Astra, Its Most Capable Business Model](https://openai.com/index/gpt-6-astra-next-generation-work) ⭐️ 9.0/10

OpenAI announced GPT-6 Astra, describing it as its most capable model for business, with advanced reasoning, computer use, and stronger writing and design judgment. The announcement is currently a brief teaser without published technical details, benchmarks, or pricing. A new flagship model from OpenAI positioned for business could reshape how enterprises deploy AI agents for coding, research, and end-to-end workflows, intensifying competition with rivals like Anthropic and Google. If the claimed reasoning and computer-use gains hold up, it could accelerate enterprise adoption of autonomous AI workers. The teaser highlights three capability areas: advanced reasoning, computer use (letting the model operate software via mouse and keyboard actions), and improved writing and design judgment. No context window, pricing, availability date, or benchmark numbers were disclosed in the announcement.

rss · OpenAI News · Sep 9, 11:00

**Background**: OpenAI's GPT series are large language models that power chatbots and AI applications; each new generation typically adds capabilities and improves on prior versions. 'Computer use' refers to AI models that can directly control software interfaces rather than relying only on custom tools, a frontier pioneered by Anthropic's Claude. Advanced reasoning models are trained to solve multi-step problems in logic, math, and programming by revisiting and revising intermediate steps.

<details><summary>References</summary>
<ul>
<li><a href="https://emergent.sh/news/openai-launches-gpt-6-astra-multimodal-ai">OpenAI Launches GPT - 6 Astra : Multimodal AI Model</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/tools-computer-use">Computer use | OpenAI API</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reasoning_model">Reasoning model - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-6`, `#AI`, `#LLM`, `#business`

---

<a id="item-3"></a>
## [vLLM v0.29.0 Makes Model Runner V2 Default, Adds 770B MoE Support](https://github.com/vllm-project/vllm/releases/tag/v0.29.0) ⭐️ 8.0/10

vLLM v0.29.0, released with 594 commits from 277 contributors, makes Model Runner V2 (MRV2) the default execution core for all models and adds support for several new large models including Tencent's 770B/49B-active MoE (Hy4-preview), Kimi K3 NVFP4 checkpoints, Qwen3.8-Flash-Next, and GraniteSWA/GraniteMoeSWA. The release also introduces batch-sharded sampling that cuts per-step logits memory by 1/TP, CUDA graph memory profiling for KV cache auto-sizing, and numerous speculative decoding and RL weight sync improvements. As one of the most widely used open-source LLM inference engines, vLLM's architectural shift to MRV2 and its support for frontier-scale models like Tencent's 770B MoE and Kimi K3 directly affect how efficiently the community can serve cutting-edge models. The performance optimizations in this release could meaningfully reduce latency and memory costs for production LLM deployments across the ecosystem. MRV1 remains in use for a few ROCm models and features MRV2 does not yet support, and the release includes breaking changes such as the removal of ten deprecated model architectures, migration of FlexOlmo/Olmo3/Hunyuan V1/VL to the Transformers backend, removal of the PyAV video decoder, and deprecation of `python -m vllm.entrypoints.openai.api_server` in favor of `vllm serve`. New defaults include FlashInfer all-reduce for TP CUDA groups and deterministic prefix-cache NONE_HASH, while new admission-control flags `--max-num-queued-reqs` and `--max-num-queued-tokens` are added.

github · khluu · Sep 9, 08:54

**Background**: vLLM is an open-source high-throughput inference and serving engine for large language models, widely used to deploy models like Llama, Qwen, and DeepSeek in production. Model Runner V2 is a redesigned execution core that replaces the original V1 design with modular model logic, GPU-native input preparation, and stable persistent batching, addressing technical debt accumulated since V1. MoE (Mixture of Experts) is an architecture where only a sparse subset of specialized sub-networks is activated per token, allowing models to scale to hundreds of billions of parameters while keeping inference costs manageable.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM</a></li>
<li><a href="https://www.oflight.co.jp/en/glossary/moe">MoE ( Mixture of Experts ) | Oflight Inc.</a></li>

</ul>
</details>

**Tags**: `#vllm`, `#llm-inference`, `#model-serving`, `#release`, `#moe`

---

<a id="item-4"></a>
## [Apple Announces iPhone Duo, Its First Foldable iPhone](https://www.apple.com/iphone-duo/) ⭐️ 8.0/10

Apple has announced the iPhone Duo, its first foldable iPhone, marking the company's entry into the foldable smartphone market. The announcement sparked extensive discussion on Hacker News, generating 1109 points and 1959 comments. This is a major product announcement that signals Apple's entry into the foldable phone category, potentially reshaping the market currently led by Samsung. It could influence the broader smartphone industry's design direction and affect millions of iPhone users considering an upgrade. Community members noted that the iPhone Duo appears to have no visible crease based on hands-on videos, addressing a common concern with foldable displays. However, some expressed skepticism about durability, comparing it to well-used Samsung Fold display models that develop creases and crunchy-feeling hinges over time.

hackernews · thecosmicfrog · Sep 9, 18:15 · [Discussion](https://news.ycombinator.com/item?id=49630931)

**Background**: Foldable smartphones feature a flexible display that can bend in half, allowing a device to serve as both a phone and a small tablet. Samsung has led this category with its Galaxy Z Fold series, but Apple has until now avoided the form factor. The iPhone Duo represents Apple's first attempt at a foldable device, and its success could depend on addressing durability and crease issues that have plagued earlier foldables.

**Discussion**: The Hacker News discussion was highly engaged, with users debating market viability, durability, and Apple's design direction. Some questioned whether the Duo would sell well given the iPhone mini's low sales share, while others praised the lack of a crease and expressed excitement about Apple's new design leadership under John Ternus. A common sentiment was to wait and see how the device performs over multiple generations before switching.

**Tags**: `#Apple`, `#iPhone`, `#foldable`, `#hardware`, `#Hacker News`

---

<a id="item-5"></a>
## [Show HN: Interactive Visualization Scales Speed of Light to 5 km/h](https://rivendell.dmitrybrant.com/relativity/) ⭐️ 8.0/10

Developer Dmitry Brant released an interactive web visualization that scales the speed of light down to 5 km/h, allowing users to experience relativistic effects with everyday objects. The first version is available at rivendell.dmitrybrant.com/relativity/ and has sparked a detailed discussion on Hacker News. By making relativistic effects intuitive at human-scale speeds, this tool could improve physics education and public understanding of special relativity, a theory whose effects are normally invisible in everyday life. It also invites comparison with earlier efforts like MIT's 'Slower Speed of Light' game, potentially raising the bar for accuracy in such simulations. The visualization is technically accurate according to community feedback, though some users note that Lorentz invariance subtleties—such as the rotation from two non-parallel boosts—may not be fully represented. The project is open for feedback and is hosted on a personal site.

hackernews · dmitrybrant · Sep 10, 01:58 · [Discussion](https://news.ycombinator.com/item?id=49637385)

**Background**: Special relativity predicts that as objects approach the speed of light, time dilates, lengths contract, and relativistic Doppler shifts occur. These effects are negligible at everyday speeds, so scaling the speed of light down to 5 km/h makes them perceptible. Previous educational tools like MIT's 'Slower Speed of Light' (2012) attempted similar simulations but had reported inaccuracies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Special_relativity">Special relativity - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Relativistic_effects">Relativistic effects</a></li>

</ul>
</details>

**Discussion**: Commenters praised the visualization as more accurate than MIT's 'Slower Speed of Light', with one noting issues in the MIT game's modeling of relativistic Doppler. Others discussed Lorentz invariance subtleties, the counterfactual nature of changing the speed of light given the meter's definition, and referenced science fiction exploring altered physical laws.

**Tags**: `#physics`, `#visualization`, `#relativity`, `#interactive`, `#education`

---

<a id="item-6"></a>
## [Shopify acquires Tailwind Labs, makers of Tailwind CSS](https://tailwindcss.com/blog/tailwind-is-joining-shopify) ⭐️ 8.0/10

Shopify has acquired Tailwind Labs, the company founded by Adam Wathan that develops the widely-used utility-first CSS framework Tailwind CSS, as announced on the official Tailwind blog. The acquisition comes after Tailwind Labs disclosed that AI-driven changes had cut documentation traffic by roughly 40% since early 2023 and led to layoffs affecting about 75% of its engineering team. The deal highlights how AI coding assistants are disrupting the business models of developer-tool companies that rely on documentation traffic and template sales, even for a project as popular as Tailwind CSS. It also raises questions about the future governance and direction of a major open-source CSS framework now owned by a large e-commerce platform. Tailwind Labs stated that traffic to its documentation was down about 40% from early 2023 despite Tailwind being more popular than ever, and that 75% of its engineering team lost their jobs due to AI's impact on the business. The acquisition is framed by community members as Shopify buying the team and brand rather than the open-source framework itself.

hackernews · EdwinHoksberg · Sep 9, 13:27 · [Discussion](https://news.ycombinator.com/item?id=49626190)

**Background**: Tailwind CSS is a utility-first CSS framework that lets developers style web pages by applying small, single-purpose classes directly in HTML markup, rather than writing custom CSS. Tailwind Labs, founded in January 2019 by Adam Wathan, built a business around the open-source framework through documentation, paid UI templates, and related tools. Shopify is a major e-commerce platform that also maintains its own developer ecosystem, including the Ruby on Rails-based Shopify platform and various front-end tools.

<details><summary>References</summary>
<ul>
<li><a href="https://tailwindcss.com/">Tailwind CSS - Rapidly build modern websites without ever leaving your HTML.</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tailwind_CSS">Tailwind CSS - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/company/tailwind-labs">Tailwind Labs | LinkedIn</a></li>

</ul>
</details>

**Discussion**: Commenters largely see the acquisition as a consequence of AI eroding Tailwind Labs' documentation and template business, with some questioning whether Tailwind is still necessary for new sites when vanilla CSS and AI-assisted coding are viable. Others express gratitude to the team and hope the open-source project continues to thrive under Shopify, while noting that running a dev-tools company with both open-source and commercial components is becoming harder in the AI era.

**Tags**: `#Tailwind CSS`, `#acquisition`, `#open source`, `#AI impact`, `#web development`

---

<a id="item-7"></a>
## [Raschka Demystifies GPT-6 Astra, Looped Transformers, and Hidden Reasoning](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and) ⭐️ 8.0/10

Sebastian Raschka published a technical deep-dive analyzing GPT-6 Astra, looped transformers, and hidden reasoning, aiming to demystify recent media hype from The Information. The post explains that looped transformers (also called recurrent depth or depth sharing) reuse weights across repeated passes, saving GPU memory while functioning similarly to stacking more layers. This analysis matters because it corrects misconceptions that looped transformers are a secret, scary technique that makes chain-of-thought monitoring harder, clarifying instead that they are a memory-efficient architectural choice. It helps LLM researchers and practitioners understand the real implications for reasoning transparency and model design. Looped transformers have provable universal computation and approximation properties, and hidden reasoning can occur when internal steps are computed in activation space without appearing in the chain-of-thought. Community discussion references Will Merrill's research on the computational requirements of chain-of-thought and the effects of universal transformers.

hackernews · ModelForge · Sep 9, 14:37 · [Discussion](https://news.ycombinator.com/item?id=49627370)

**Background**: GPT-6 Astra is a large language model developed by OpenAI, initially released to approved users on September 3, 2026, with general availability the following day. Looped transformers, also known as recurrent depth or looped depth sharing, reuse the same weights across multiple passes, making them more memory-efficient than standard deep transformers. Hidden reasoning refers to reasoning that occurs internally in a model's hidden layers or activation space rather than being verbalized in a chain-of-thought.

<details><summary>References</summary>
<ul>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/looped-depth-sharing/">Looped Transformer | Sebastian Raschka, PhD</a></li>
<li><a href="https://www.lesswrong.com/posts/ZrgFfeWuckpwK5Lyi/hidden-reasoning-in-llms-a-taxonomy">Hidden Reasoning in LLMs : A Taxonomy — LessWrong</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra</a></li>

</ul>
</details>

**Discussion**: Commenters largely praised Raschka's clear explanation, with one noting it corrected the misleading framing from The Information that looped transformers are a scary secret technique. Others shared research references, such as Will Merrill's work on chain-of-thought computational requirements and universal transformers, and discussed how looping a transformer on itself is by definition hidden reasoning. One commenter also highlighted an MSPAINT computer-use demo as impressive.

**Tags**: `#LLM`, `#transformers`, `#reasoning`, `#AI research`, `#chain-of-thought`

---

<a id="item-8"></a>
## [Automattic Board Forces CEO Matt Mullenweg Into Leave of Absence](https://techcrunch.com/2026/09/09/automattics-board-forces-ceo-matt-mullenweg-into-leave-of-absence/) ⭐️ 8.0/10

Automattic's board of directors voted to place founder and CEO Matt Mullenweg on a paid leave of absence against his will, installing CFO Mark Davies as interim CEO. Mullenweg announced the move in a company-wide Slack message, claiming board members Ann Dunwoody, Toni Schneider, and Sue Decker 'conspired' behind his back and that he voted against the decision. Automattic is the company behind WordPress.com and a major contributor to the open-source WordPress project, which powers over 43% of the web, so a leadership shakeup at the top has significant implications for the open-source ecosystem and the millions of sites that depend on WordPress. The move signals that the board is willing to act against Mullenweg's long-standing control, which could reshape governance of both the company and the broader WordPress community. Mullenweg said he was given only 50 minutes' notice and was denied his request to consult legal counsel before the vote. The board members named in his Slack message are Ann Dunwoody, Toni Schneider, and Sue Decker, and CFO Mark Davies has been installed as interim CEO.

hackernews · LeoPanthera · Sep 9, 23:49 · [Discussion](https://news.ycombinator.com/item?id=49636283)

**Background**: Matt Mullenweg co-founded the open-source WordPress publishing software in 2003 and founded Automattic in 2005; the company runs WordPress.com and contributes heavily to the WordPress project. WordPress is a free content management system used by more than 43% of websites worldwide, giving Automattic and Mullenweg outsized influence over the open-source ecosystem. In recent years Mullenweg has faced criticism over his handling of the WP Engine dispute and other controversies, and in April 2025 Automattic laid off 16% of its staff.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/09/09/automattics-board-forces-ceo-matt-mullenweg-into-leave-of-absence/">Automattic's board forces CEO Matt Mullenweg into leave of ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Matt_Mullenweg">Matt Mullenweg</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automattic">Automattic - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters largely saw the board's move as necessary but risky: one noted that WordPress powers a large percentage of the internet and that Mullenweg's 'unforced error after unforced error' as CEO made a break advisable, though he doubted Mullenweg would be brought back. Others emphasized that Mullenweg retains a stranglehold on Automattic and WordPress that cannot easily be removed, predicting he will retaliate against the board and that things will get worse before they get better.

**Tags**: `#WordPress`, `#Automattic`, `#leadership`, `#open-source`, `#corporate-governance`

---

<a id="item-9"></a>
## [IBM Releases SOTA Granite Time Series PatchTST-FM-r2 with Commercial-Friendly License](https://huggingface.co/blog/ibm-research/ibm-releases-sota-granite-time-series) ⭐️ 7.0/10

IBM Research has released Granite Time Series PatchTST-FM-r2, a state-of-the-art time series foundation model available on Hugging Face under a commercial-friendly license. The model builds on the PatchTST architecture and is positioned as IBM's latest addition to its Granite Time Series family, enabling broader industrial adoption without restrictive licensing terms. This release is significant because it combines state-of-the-art forecasting performance with a permissive license, lowering the barrier for enterprises to deploy time series foundation models in commercial products. It also intensifies competition in the growing time series foundation model space alongside offerings like Google's TimesFM and Salesforce's Moirai. The model is based on the PatchTST architecture, which segments time series into patches as input tokens for a Transformer backbone, and is part of IBM's Granite Time Series collection on Hugging Face. IBM's broader Granite TSFM family also includes ultra-lightweight models like Tiny Time Mixer (TTM) and TSPulse with just a few million parameters and GPU-free inference.

rss · Hugging Face Blog · Sep 9, 15:36

**Background**: Time series foundation models are pretrained models designed to forecast, classify, and detect anomalies in sequential data such as sales figures, sensor readings, or financial metrics, similar to how large language models handle text. PatchTST, introduced in a 2023 ICLR paper titled 'A Time Series is Worth 64 Words,' is a Transformer-based approach that splits time series into patches to improve long-term forecasting efficiency. IBM's Granite initiative is its family of enterprise-focused foundation models, and the Granite Time Series line extends this to temporal data with models available on Hugging Face.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/yuqinie98/PatchTST">GitHub - yuqinie98/PatchTST: An offical implementation of PatchTST: "A Time Series is Worth 64 Words: Long-term Forecasting with Transformers." (ICLR 2023) https://arxiv.org/abs/2211.14730 · GitHub</a></li>
<li><a href="https://www.ibm.com/granite/docs/models/time-series">Granite Time Series | IBM Granite</a></li>
<li><a href="https://github.com/ibm-granite/granite-tsfm">GitHub - ibm-granite/granite-tsfm: Foundation Models for Time ...</a></li>

</ul>
</details>

**Tags**: `#time series`, `#foundation models`, `#IBM Granite`, `#AI/ML`, `#open source`

---