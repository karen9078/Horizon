---
layout: default
title: "Horizon Summary: 2026-07-27 (EN)"
date: 2026-07-27
lang: en
---

> From 29 items, 9 important content pieces were selected

---

1. [vLLM v0.26.0: Inkling Model Family, DeepSeek-V4 Optimizations, and More](#item-1) ⭐️ 8.0/10
2. [LLMs Slash Formal Verification Costs](#item-2) ⭐️ 8.0/10
3. [US citizen charged after GrapheneOS phone wipes during airport search](#item-3) ⭐️ 8.0/10
4. [Relay market enables token resellers and fraud in AI cloud services](#item-4) ⭐️ 8.0/10
5. [EU Proposes Browser-Level Privacy to Kill Cookie Banners](#item-5) ⭐️ 8.0/10
6. [OpenAI Agents Python SDK v0.19.0 Adds Programmatic Tool Calling](#item-6) ⭐️ 7.0/10
7. [PGSimCity Visualizes PostgreSQL Internals Interactively](#item-7) ⭐️ 7.0/10
8. [NVIDIA's Physical AI Revenue Hits $10B, Eyes $100B](#item-8) ⭐️ 7.0/10
9. [OpenAI Urges White House to Speed Frontier AI Reviews](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0: Inkling Model Family, DeepSeek-V4 Optimizations, and More](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 introduces support for the new Inkling model family, significant performance optimizations for DeepSeek-V4, fp32 lm_head support via head_dtype, and flexible attention backends that can be selected per KV-cache group. This release enhances vLLM's versatility and performance, benefiting users deploying large language models in production by supporting more model architectures and improving inference efficiency. The release includes 411 commits from 212 contributors, with notable additions like piecewise CUDA graph support for Inkling, a specialized routing kernel for DeepSeek-V4, and KV offloading metrics for tiered storage.

github · khluu · Jul 27, 01:06

**Background**: vLLM is an open-source high-throughput LLM inference engine that optimizes memory and computation for serving large language models. The Inkling model family is a general-purpose multimodal model from Thinking Machines Lab, supporting text, image, and audio inputs. DeepSeek-V4 is a large language model that benefits from custom kernels for improved performance.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/thinkingmachines/Inkling">thinkingmachines/ Inkling · Hugging Face</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling : Our Open-Weights Model - Thinking Machines Lab</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#model optimization`, `#GPU kernels`, `#open source`

---

<a id="item-2"></a>
## [LLMs Slash Formal Verification Costs](https://www.imperialviolet.org/2026/07/26/zstd-lean.html) ⭐️ 8.0/10

A blog post argues that large language models (LLMs) have made formal verification dramatically cheaper, reducing the cost from roughly 20x the cost of software development to near zero, potentially transforming software reliability. This shift could make formal verification practical for mainstream software development, drastically reducing bugs and security vulnerabilities. It may also change the economics of exploit development, as verification becomes cheaper than finding exploits. The post specifically mentions using LLMs with the Lean theorem prover and tools like Verus for Rust. Community comments note that writing formal specifications may become a key programmer skill, and that LLM-generated proofs can now be produced at a fraction of previous costs.

hackernews · zdw · Jul 26, 20:53 · [Discussion](https://news.ycombinator.com/item?id=49062291)

**Background**: Formal verification uses mathematical proofs to guarantee software correctness, but has historically been extremely expensive (often 20x development cost). LLMs can now generate proofs automatically, drastically reducing the human effort required. Tools like Lean and Verus integrate theorem proving into programming languages, making verification more accessible.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2505.15740">[2505.15740] HybridProver: Augmenting Theorem Proving with ...</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree with the thesis, with some sharing personal projects like OpenATP for benchmarking ATP systems. One commenter notes confusion in the crypto space about the actual cost of LLM-based verification, citing a tweet claiming $150k in API tokens for a Lean formalization of the Ethereum VM.

**Tags**: `#formal verification`, `#LLM`, `#software reliability`, `#theorem proving`, `#Lean`

---

<a id="item-3"></a>
## [US citizen charged after GrapheneOS phone wipes during airport search](https://www.techspot.com/news/113236-us-prosecutors-charge-atlanta-man-after-grapheneos-phone.html) ⭐️ 8.0/10

A US citizen was charged after his GrapheneOS phone automatically wiped itself when he entered a duress PIN during a border search at Atlanta airport. The incident has sparked debate on the legal consequences of using security features designed to protect data under coercion. This case highlights the tension between digital privacy rights and government border search powers, potentially setting a precedent for how courts treat the use of duress PINs and encryption features. It affects all travelers who use strong privacy tools and raises questions about the legality of wiping devices during lawful searches. The duress PIN feature in GrapheneOS triggers a silent factory reset when entered, unlike a standard PIN that unlocks the phone. The user reportedly entered the duress PIN instead of unlocking the device when agents demanded access, leading to the wipe and subsequent charges.

hackernews · eecc · Jul 26, 22:21 · [Discussion](https://news.ycombinator.com/item?id=49063022)

**Background**: GrapheneOS is a security-focused Android-based operating system that offers advanced privacy features, including a duress PIN that wipes the device when entered under coercion. US border agents have broad authority to search electronic devices, and intentionally destroying evidence during a search can lead to obstruction charges. The case is ongoing and raises complex legal questions about the intersection of security tools and criminal law.

<details><summary>References</summary>
<ul>
<li><a href="https://www.androidauthority.com/grapheneos-duress-pin-us-prosecution-3691271/">GrapheneOS duress PIN could land a man in prison - Android Authority</a></li>
<li><a href="https://www.androidauthority.com/grapheneos-duress-pin-3584795/">I use a duress PIN to protect my data — here’s how it works</a></li>
<li><a href="https://privacygear.nl/en/guides/grapheneos-duress-pin-guide/">GrapheneOS duress PIN : wipe your phone under... — PrivacyGear.nl</a></li>

</ul>
</details>

**Discussion**: Commenters debated whether using a duress PIN is a legitimate security practice or an illegal act of obstruction. Some argued that users must accept legal consequences when choosing such features, while others suggested that decoy OS systems like VeraCrypt's hidden volume could be a better alternative. There was also technical clarification that GrapheneOS's duress PIN does not overwrite data but performs a factory reset, which may not fully prevent forensic recovery.

**Tags**: `#GrapheneOS`, `#digital rights`, `#border security`, `#encryption`, `#legal`

---

<a id="item-4"></a>
## [Relay market enables token resellers and fraud in AI cloud services](https://vectoral.com/blog/token-relay-market) ⭐️ 8.0/10

An investigation reveals an underground relay market where token resellers pool API keys and use proxy services to sell discounted AI and cloud services, exploiting billing systems and free credits. This market enables fraud and gives unfair competitive advantages to resellers, undermining the pricing models of legitimate providers and potentially harming startups that rely on free credits. Resellers use open-source tooling to build proxy services that route requests through pooled API keys, often obtained via stolen accounts or free credit abuse, selling tokens at a fraction of the official price.

hackernews · mlenhard · Jul 26, 15:17 · [Discussion](https://news.ycombinator.com/item?id=49058993)

**Background**: AI and cloud providers like AWS and Azure offer free credits to attract new customers. However, fraudsters exploit these programs by creating multiple accounts, using stolen payment methods, or abusing billing systems to accumulate credits, which are then resold at a discount in relay markets.

<details><summary>References</summary>
<ul>
<li><a href="https://devblogs.co/posts/an-inside-look-at-the-relay-market-powering-token-resellers-and-fraud">An Inside Look at the Relay Market Powering Token Resellers and...</a></li>
<li><a href="https://cctest.ai/en/articles/inside-the-ai-token-relay-market-cheap-inference-account-pools-and-fraud">AI Token Relay Market : Cheap APIs and Fraud Risks - CCTest</a></li>

</ul>
</details>

**Discussion**: Commenters note that similar resale markets existed for previous internet giants' products, and that free credit abuse is a key enabler. Some highlight the challenge of preventing token fraud in subscription models, while others point to solutions like WorkOS Radar being developed to combat this.

**Tags**: `#AI`, `#cloud computing`, `#fraud`, `#market abuse`, `#security`

---

<a id="item-5"></a>
## [EU Proposes Browser-Level Privacy to Kill Cookie Banners](https://killthecookiebanner.eu/) ⭐️ 8.0/10

The European Commission has proposed a regulation that would allow users to set their privacy preferences once in the browser, eliminating the need for cookie banners on every website. This could end the widely hated cookie banner experience, improving user experience and accessibility while potentially reducing tracking if properly enforced. The proposal moves cookie rules into the GDPR framework, giving websites more legal bases, but faces pushback from EU member states like Germany and France, as well as Google.

hackernews · rapnie · Jul 26, 11:53 · [Discussion](https://news.ycombinator.com/item?id=49057175)

**Background**: Cookie banners are pop-ups required under the EU's ePrivacy Directive to obtain user consent for tracking cookies. They have been criticized for being annoying, misleading, and often failing to provide genuine informed consent.

<details><summary>References</summary>
<ul>
<li><a href="https://noyb.eu/en/eu-member-states-and-google-suddenly-want-keep-cookie-banners">EU Member States (and Google) suddenly want to keep cookie banners!</a></li>
<li><a href="https://thecapitolforum.com/eu-cookie-banner-cleanup-plan-faces-conflicting-pushback-echoing-tensions-that-tanked-past-efforts/">EU Cookie Banner Cleanup Plan Faces Conflicting Pushback, Echoing Tensions That Tanked Past Efforts - The Capitol Forum</a></li>

</ul>
</details>

**Discussion**: Commenters largely support the proposal, citing annoyance, lack of informed consent, and accessibility issues. Some argue that banners should be banned entirely, while others emphasize the need for strict enforcement and fines for non-compliance.

**Tags**: `#privacy`, `#regulation`, `#web standards`, `#user experience`, `#accessibility`

---

<a id="item-6"></a>
## [OpenAI Agents Python SDK v0.19.0 Adds Programmatic Tool Calling](https://github.com/openai/openai-agents-python/releases/tag/v0.19.0) ⭐️ 7.0/10

OpenAI released v0.19.0 of the openai-agents-python SDK, introducing Programmatic Tool Calling via the new `ProgrammaticToolCallingTool` class, which allows supported models to generate JavaScript for coordinating tools. The release also adds a public `agents.decorators` module with a `@tool` alias and improves configuration flexibility by accepting both typed objects and dictionaries. This feature enables AI agents to write and execute JavaScript for complex tool orchestration, including parallel calls, loops, and conditionals, significantly expanding the capabilities of agentic workflows. The SDK improvements also make it easier for developers to build and configure multi-agent systems, potentially accelerating adoption of AI agents in production. Programmatic Tool Calling is supported only by certain OpenAI Responses models and requires a hosted JavaScript runtime; it supports per-tool `allowed_callers`, structured function-tool outputs, and integrates with streaming, guardrails, and approvals. The release also hardens logging to avoid exposing sensitive payloads and improves compatibility with AnyLLM and LiteLLM providers.

github · seratch · Jul 27, 04:10

**Background**: The OpenAI Agents SDK is a lightweight framework for building multi-agent workflows, supporting OpenAI's Responses and Chat Completions APIs as well as over 100 other LLMs. Tool calling (function calling) allows models to interact with external systems, and Programmatic Tool Calling extends this by letting the model write JavaScript programs that coordinate multiple tool calls in a single request, enabling more dynamic and efficient agent behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling">Programmatic Tool Calling | OpenAI API</a></li>
<li><a href="https://openai.github.io/openai-agents-python/">OpenAI Agents SDK</a></li>
<li><a href="https://github.com/openai/openai-agents-python">GitHub - openai / openai - agents - python : A lightweight, powerful...</a></li>

</ul>
</details>

**Tags**: `#openai`, `#agents-sdk`, `#tool-calling`, `#python`, `#ai-agents`

---

<a id="item-7"></a>
## [PGSimCity Visualizes PostgreSQL Internals Interactively](https://nikolays.github.io/PGSimCity/) ⭐️ 7.0/10

PGSimCity is an interactive visualization tool that animates PostgreSQL's internal architecture, including process management, memory allocation, and query execution flow. It provides a real-time, animated tour of how the database operates under the hood. This tool makes complex database internals accessible to developers and students, lowering the barrier to understanding PostgreSQL's process-based architecture. Community feedback suggests it could become even more valuable if made query-driven and interactive, potentially serving as a teaching aid for database courses. The tool is open-source and available at nikolays.github.io/PGSimCity/. Users report that the automatic tour can be overwhelming with too many simultaneous animations, and some experience blank screens when zooming in on 4K displays.

hackernews · jonbaer · Jul 27, 00:19 · [Discussion](https://news.ycombinator.com/item?id=49063754)

**Background**: PostgreSQL uses a multi-process architecture where a 'postmaster' process forks a new backend process for each client connection. It also employs shared memory and various background processes (e.g., writer, checkpointer) for concurrency and reliability. Understanding this architecture is key to tuning and troubleshooting PostgreSQL performance.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.algomaster.io/p/postgresql-internal-architecture">How PostgreSQL Works: Internal Architecture Explained</a></li>
<li><a href="https://severalnines.com/blog/understanding-postgresql-architecture/">Understanding the PostgreSQL Architecture | Severalnines</a></li>
<li><a href="https://www.postgresql.org/docs/current/spi-memory.html">PostgreSQL: Documentation: 18: 45.3. Memory Management</a></li>

</ul>
</details>

**Discussion**: Commenters praised the tool's educational value but wished for more interactivity, such as entering a custom query and seeing it flow through the system. Some found the automatic tour too noisy, while others on large screens appreciated the level of detail. A few suggested applying the same visualization concept to other domains like Kubernetes.

**Tags**: `#PostgreSQL`, `#database internals`, `#visualization`, `#educational tool`

---

<a id="item-8"></a>
## [NVIDIA's Physical AI Revenue Hits $10B, Eyes $100B](https://news.google.com/rss/articles/CBMiW0FVX3lxTE55VllHTUVsLUR6a3lUSFJ4cGdDZUVFWnNOVUN0bG91N1J0c3E0RUxKdFhzTjFkSDFkbW5BLVZjSkdwbEdJNXBwaFVGVU42bGQ2ZXlQU2luSGNmbGc?oc=5) ⭐️ 7.0/10

NVIDIA CEO Jensen Huang announced that the company's Physical AI business has reached $10 billion in revenue and outlined a path to $100 billion. This milestone signals strong market validation for Physical AI, which powers autonomous systems like robots and self-driving cars, and positions NVIDIA as a dominant player in the next wave of AI-driven physical industries. The Physical AI market is projected to grow from $1.50 billion in 2026 to $15.24 billion by 2032, according to MarketsandMarkets, making NVIDIA's $10 billion figure notably larger than current market estimates.

google_news · finance.biggo.com · Jul 26, 22:09

**Background**: Physical AI refers to AI systems that perceive, reason, and act in the physical world, enabling autonomous machines like robots and self-driving cars. NVIDIA provides hardware (GPUs), simulation platforms (e.g., Omniverse), and AI models to support this ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/generative-physical-ai/">What is Physical AI? | NVIDIA Glossary</a></li>
<li><a href="https://www.marketsandmarkets.com/ResearchInsight/physical-ai-nvidia.asp">NVIDIA is Driving the Next Era of Physical AI Innovation</a></li>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world">NVIDIA and Global Robotics Leaders Take Physical AI to the Real World | NVIDIA Newsroom</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#Physical AI`, `#AI Hardware`, `#Market Growth`, `#Robotics`

---

<a id="item-9"></a>
## [OpenAI Urges White House to Speed Frontier AI Reviews](https://news.google.com/rss/articles/CBMihwFBVV95cUxQZGZJS3IxSXd1ME9Ib0s5LVpmQmxjdjJicG5FelJBeWhpRG9RNUVtZUhKSllNVDVkM2JCcmYxRTdmNkRoYTRTNWg5WFlqaUpFRS1RUk1DVExWRVBtSk9YMUZYMXVnNTlzZUdWV3N5ZVJ3TmpncXkyNlNIeVloeTkzdHM0SDNKd3M?oc=5) ⭐️ 7.0/10

OpenAI is lobbying the White House to accelerate the review process for frontier AI models, pushing for faster regulatory approvals before model release. This move could shape U.S. AI regulation, potentially reducing time-to-market for advanced models while influencing global standards. It highlights the tension between innovation speed and safety oversight. The current voluntary 30-day pre-release review for frontier models was established by a White House executive order. OpenAI's push suggests the company wants even faster reviews, possibly to maintain competitive advantage.

google_news · Unite.AI · Jul 26, 12:57

**Background**: Frontier AI models are the most advanced and capable models, trained on massive datasets to perform a wide variety of tasks. The U.S. government currently relies on voluntary reviews rather than mandatory regulation, unlike the EU's AI Act. OpenAI's lobbying reflects ongoing debates about how to balance innovation with safety.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work - NVIDIA</a></li>
<li><a href="https://carussignal.com/white-house-30-day-frontier-ai-review-explained/">The 30-Day Rule: What the White House's New Frontier - AI Review ...</a></li>

</ul>
</details>

**Tags**: `#AI Policy`, `#OpenAI`, `#Regulation`, `#Frontier Models`

---