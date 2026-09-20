---
layout: default
title: "Horizon Summary: 2026-09-20 (EN)"
date: 2026-09-20
lang: en
---

> From 20 items, 6 important content pieces were selected

---

1. [RSA-896 Factored via Claude-Orchestrated GPU Port of CADO-NFS](#item-1) ⭐️ 8.0/10
2. [OpenAI launches GPT-Live-1 in the API for natural voice](#item-2) ⭐️ 8.0/10
3. [OONI censorship measurement tool sparks Hacker News debate on scope and bias](#item-3) ⭐️ 7.0/10
4. [Brood War Bench: New Benchmark for StarCraft AI](#item-4) ⭐️ 7.0/10
5. [AI-generated posters don't have to be horrible](#item-5) ⭐️ 7.0/10
6. [Non-Autoregressive RL Decision Model Sparks Debate on Novelty vs. Marketing](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [RSA-896 Factored via Claude-Orchestrated GPU Port of CADO-NFS](https://saweis.net/posts/rsa-896.html) ⭐️ 8.0/10

A user had Claude port CADO-NFS to run on GPUs and then orchestrated a fleet of up to 2048 GPUs to factor RSA-896, a 270-digit (896-bit) number from the RSA Factoring Challenge. The run consumed roughly 30 GPU-years over about 10 days using scavenged idle capacity. This is a notable cryptographic milestone because RSA-896 had remained unfactored since the challenge was created in 1991, and it demonstrates that GPU-accelerated number field sieve implementations can now tackle sizes previously considered out of reach. It also highlights how AI-assisted code porting and orchestration can lower the engineering barrier to large-scale distributed computation. The factoring used CADO-NFS, the reference C/C++ implementation of the Number Field Sieve, ported to GPUs and run on scavenged idle capacity with a maximum of 2048 GPUs. The effort took about 30 GPU-years over 10 days, and the user noted that credit belongs to the people who built the number field sieve and CADO-NFS over decades.

hackernews · madars · Sep 20, 02:19 · [Discussion](https://news.ycombinator.com/item?id=49771966)

**Background**: The general number field sieve is the most efficient classical algorithm known for factoring integers larger than 10^100, and CADO-NFS is a complete open-source implementation of it. RSA numbers are semiprimes published by RSA Laboratories in 1991 as a factoring challenge to gauge the practical difficulty of breaking RSA-based cryptography. Factoring a 896-bit RSA modulus does not directly break RSA-1024 or larger keys, but it provides a data point on the advancing frontier of factoring capability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/General_number_field_sieve">General number field sieve - Wikipedia</a></li>
<li><a href="https://github.com/cado-nfs/cado-nfs">cado - nfs / cado - nfs : Cado - NFS , An Implementation of the Number ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/RSA_numbers">RSA numbers - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters noted the economics of using already-paid-for idle GPU capacity for math puzzles, with one arguing it would be more financially sensible to mine crypto and another calling it bearish for data center rollouts if spare compute is used for puzzles instead of training LLMs. The overall sentiment was a mix of appreciation for the achievement and pragmatic observations about compute economics.

**Tags**: `#cryptography`, `#RSA`, `#GPU computing`, `#number field sieve`, `#distributed computing`

---

<a id="item-2"></a>
## [OpenAI launches GPT-Live-1 in the API for natural voice](https://news.google.com/rss/articles/CBMic0FVX3lxTFBRNXJSTHl4WmdBNnM2dnFMVXo3UE1CZFkzTUtzUlFQNXV2dnc1alNkaW1icHZDOGNUQlJjUFdMMDlWOVQ3Q0s4MzE1S0xOaVBSS3RubkNvUjkwampKcjdpckZIQTF6X1E3Q2k1dzJsTl9UZ0U?oc=5) ⭐️ 8.0/10

OpenAI has introduced GPT-Live-1 in its API, bringing natural, full-duplex voice conversations to developers along with stronger instruction following, custom voices, and telephony support. The model was previously rolled out to ChatGPT users as GPT-Live-1 and GPT-Live-1 mini before becoming available to API developers. This gives developers a first-class way to add conversational voice to their products without building speech pipelines from scratch, which could accelerate voice agents across customer support, telephony, and assistants. It also intensifies competition in the realtime voice AI space, where OpenAI is positioning GPT-Live as a core interface layer for applications. GPT-Live-1 supports full-duplex conversation, meaning users and the model can speak and listen simultaneously, and it offers custom voices and telephony support. Developers can keep their existing text workflows and tools, then add GPT-Live as the voice interface using either client delegation or responses delegation modes.

google_news · OpenAI · Sep 20, 03:00

**Background**: Voice AI in the OpenAI API has evolved from separate transcription, translation, and speech-generation endpoints toward unified conversational agents. Full-duplex means the model can handle overlapping speech and interruptions like a human phone call, rather than the turn-taking of older voice assistants. GPT-Live is OpenAI's family of realtime voice models, and GPT-Live-1 is the version now exposed through the API for developers.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-live-1-in-the-api/">Build more natural voice experiences with GPT‑Live‑1 in the API | OpenAI</a></li>
<li><a href="https://openai.com/index/introducing-gpt-live/">Introducing GPT-Live | OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/voice-agents">Voice agents | OpenAI API</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#voice AI`, `#API`, `#GPT`, `#developer tools`

---

<a id="item-3"></a>
## [OONI censorship measurement tool sparks Hacker News debate on scope and bias](https://ooni.org/install) ⭐️ 7.0/10

OONI's internet censorship measurement tool (ooni.org/install) was discussed on Hacker News, where the thread reached 141 points and 86 comments. Commenters highlighted OONI Probe's focus on network-level blocking while debating its limitations regarding platform-level censorship and potential geographic biases. OONI is one of the few open-source, community-driven projects providing public data on internet censorship worldwide, so debates about its methodology directly affect how researchers, journalists, and policymakers interpret global censorship trends. The discussion also surfaces a broader question about whether network-level measurement adequately captures the growing role of platform-level content moderation. OONI Probe is a network measurement tool that detects blocked websites and apps by testing IP reachability, and its data is published openly via OONI Explorer with over a billion measurements. A key criticism raised is that the probe scans domains frequently blocked in authoritarian countries but not those blocked in democracies, such as Anna's Archive, potentially skewing the global picture.

hackernews · Bluestein · Sep 19, 20:00 · [Discussion](https://news.ycombinator.com/item?id=49769676)

**Background**: OONI, the Open Observatory of Network Interference, is a non-profit free software project founded in 2012 that measures internet censorship, surveillance, and network interference. Its OONI Probe app runs a series of network measurements to detect blocked websites, apps, and tools, and the resulting data is published openly through OONI Explorer. The project operates at the network layer, examining IP reachability rather than content moderation decisions made by platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OONI">OONI - Wikipedia</a></li>
<li><a href="https://ooni.org/">OONI: Open Observatory of Network Interference | OONI</a></li>
<li><a href="https://explorer.ooni.org/">OONI Explorer - Open Data on Internet Censorship Worldwide</a></li>

</ul>
</details>

**Discussion**: Commenters raised several concerns: one noted a bias problem because the probe scans domains blocked in dictatorships but not those blocked in democracies like Anna's Archive; another argued most censorship happens within platforms (e.g., Reddit mods, Twitter's NYPost incident) and is missed entirely. A counterpoint emphasized that OONI is not designed to measure layers 4-7 of the OSI model but focuses on IP reachability and layer 3, and one user noted RIPE Atlas has thousands of endpoints that can ping/fetch.

**Tags**: `#internet-censorship`, `#network-measurement`, `#privacy`, `#ooni`, `#hacker-news`

---

<a id="item-4"></a>
## [Brood War Bench: New Benchmark for StarCraft AI](https://bw.swerdlow.dev/report) ⭐️ 7.0/10

A new benchmark called Brood War Bench has been released for evaluating AI agents in StarCraft: Brood War, as detailed on its report page at bw.swerdlow.dev/report. The project has sparked a vibrant community discussion with 227 points and 98 comments on Hacker News. This benchmark provides a standardized way to measure progress in game AI, particularly for real-time strategy games that require long-term planning and complex decision-making. It could accelerate research in reinforcement learning and multi-agent systems by offering a challenging, well-defined testbed. The benchmark focuses on StarCraft: Brood War, a classic RTS known for its difficulty and partial observability, and likely builds on existing APIs like BWAPI. It may include tasks that test macromanagement, micromanagement, and strategic adaptation, though specific metrics and baselines are not detailed in the provided content.

hackernews · benswerd · Sep 19, 14:44 · [Discussion](https://news.ycombinator.com/item?id=49766966)

**Background**: StarCraft: Brood War, released in 1998, has long been a challenging domain for AI research due to its real-time nature, large action space, and imperfect information. Previous efforts include the Student StarCraft AI Tournament (SSCAIT) from 2011 to 2022 and DeepMind's work on StarCraft II, which advanced reinforcement learning techniques. Benchmarks like this help compare different AI approaches, from rule-based systems to deep learning.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/StarCraft:_Brood_War">StarCraft : Brood War - Wikipedia</a></li>
<li><a href="https://liquipedia.net/starcraft/SSCAIT">SSCAIT - Liquipedia StarCraft Brood War Wiki</a></li>
<li><a href="https://arxiv.org/html/2506.10384v1">NeuroPAL: Punctuated Anytime Learning with Neuroevolution for Macromanagement in Starcraft: Brood War</a></li>

</ul>
</details>

**Discussion**: Community comments reflect nostalgia for early StarCraft cybercafe culture, historical context about the 2010 UC Santa Cruz Brood War AI tournament, and creative ideas like using machine learning to upscale old match videos to Remastered quality. One commenter humorously analogizes AI agent architectures to StarCraft factions (Protoss, Terran, Zerg), showing the game's enduring influence on AI thinking.

**Tags**: `#StarCraft`, `#AI`, `#Benchmark`, `#Reinforcement Learning`, `#Game AI`

---

<a id="item-5"></a>
## [AI-generated posters don't have to be horrible](https://john.hartnup.uk/2026/06/07/ai-event-posters.html) ⭐️ 7.0/10

A blog post on john.hartnup.uk argues that AI-generated event posters can be acceptable, pushing back against the common assumption that AI design output is inherently bad. The post sparked a large Hacker News discussion with 1,533 points and 819 comments debating AI's role in graphic design. The debate touches on a growing real-world question: as generative AI tools become widely available for poster and graphic design, whether their output is 'good enough' affects freelance designers, event organizers, and the broader creative industry. The strong community engagement shows this is a live tension between cost, effort, and creative quality. Commenters noted that even the article's 'better' examples still read as AI-generated to trained eyes, citing telltale errors like a deformed wireframe sphere in a 90s drum-and-bass flyer style poster. Others argued that AI models struggle to move beyond surface-level, stereotypical associations—such as pairing 'Japanese Minimal Poster' with sakura and a stylized Japanese flag.

hackernews · ereiamjh · Sep 19, 09:20 · [Discussion](https://news.ycombinator.com/item?id=49764791)

**Background**: Generative AI tools such as Recraft, Design.com, and Leonardo.ai can now produce posters and graphic designs from simple text prompts, making design accessible to people without formal training. However, critics point out that AI systems replicate patterns rather than understand emotion or context, often producing generic or subtly flawed results. This has fueled an ongoing debate about whether AI can match human designers, especially for creative, culturally nuanced work.

<details><summary>References</summary>
<ul>
<li><a href="https://recraft-client.vercel.app/generate/posters">AI Poster Maker — Design Posters with AI | Recraft</a></li>
<li><a href="https://www.leonardo.ai/ai-graphic-design">AI Graphic Design Generator</a></li>
<li><a href="https://www.wingmatestudio.com/blog-posts/when-pixel-perfect-isnt-enough-the-limitations-of-ai-in-graphic-design">Why AI-Generated Designs Feel ‘Off’ (And How to Fix It)</a></li>

</ul>
</details>

**Discussion**: Commenters were divided: some argued that AI output is still worse than a skilled human designer, while others countered that the average budget freelance designer on platforms like Fiverr often produces worse results than AI. A recurring theme was that the default AI style signals low effort, and that AI's reliance on banal, stereotypical associations makes its creative output feel hollow.

**Tags**: `#AI`, `#Design`, `#Generative AI`, `#Creativity`, `#Hacker News`

---

<a id="item-6"></a>
## [Non-Autoregressive RL Decision Model Sparks Debate on Novelty vs. Marketing](https://laya.convaiinnovations.com/) ⭐️ 7.0/10

A Hacker News discussion about a non-autoregressive decision model built with reinforcement learning drew 1182 points and 288 comments, with commenters debating whether the approach is technically novel or essentially BERT with more data. The author claims a frontier lab later called the concept a 'breakthrough,' while critics argue the real differentiator is branding and marketing rather than technical substance. The debate highlights a recurring tension in the AI ecosystem: whether technical merit alone can win adoption, or whether clear branding and packaging are equally essential for research to become a product. It also raises questions about how much credit original researchers receive when a well-funded lab or startup popularizes their ideas. Commenters noted that the model is faster and cheaper than LLM-based classifiers like Gemini 2.5 Flash Lite and offers consistent one-shot classification, but one NLP veteran described it as 'just BERT with more data' rather than a breakthrough. The author's own marketing was limited to a single Reddit post titled 'Predicting sales conversion probability from conversations using pure Reinforcement Learning,' which many found hard to parse.

hackernews · nandakishor_ml · Sep 19, 10:46 · [Discussion](https://news.ycombinator.com/item?id=49765348)

**Background**: Non-autoregressive models generate outputs in parallel rather than token-by-token, which can make inference much faster than autoregressive LLMs like GPT. Reinforcement learning trains a model through reward signals rather than labeled examples, and here it is used to produce calibrated probability estimates for decision tasks such as classifying sales conversations. The comparison point in the discussion, Jev, is a well-branded commercial classifier product that some commenters see as repackaging similar ideas with stronger marketing.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49765348">I built non - autoregressive decision models with RL... | Hacker News</a></li>
<li><a href="https://dev.to/nandakishor_m_6cc0adfde9f/i-built-non-autoregressive-decision-models-a-year-ago-then-a-frontier-lab-called-it-a-18me">I Built Non - Autoregressive Decision Models ... - DEV Community</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/difference-between-autoregressive-and-non-autoregressive-models/">Difference Between Autoregressive And Non-Autoregressive Models - GeeksforGeeks</a></li>

</ul>
</details>

**Discussion**: Sentiment was mixed: some argued marketing and branding matter as much as the product and praised Jev's clear messaging, while others criticized Jev's launch language as sounding like a parody or con. A recurring technical critique was that the approach is essentially BERT with more data, and one commenter suggested the author's academic-style release of papers and weights, rather than a product, is part of why the work was overlooked.

**Tags**: `#reinforcement-learning`, `#non-autoregressive-models`, `#machine-learning`, `#hacker-news`, `#startup-marketing`

---