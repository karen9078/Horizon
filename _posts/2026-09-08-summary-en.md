---
layout: default
title: "Horizon Summary: 2026-09-08 (EN)"
date: 2026-09-08
lang: en
---

> From 25 items, 9 important content pieces were selected

---

1. [OpenAI Unveils GPT-6 Astra, Its Most Capable Model Yet](#item-1) ⭐️ 9.0/10
2. [Factoring 90s CA RSA Keys with a Consumer GPU](#item-2) ⭐️ 8.0/10
3. [Broadcom's VDDK Removal Complicates VMware Migrations](#item-3) ⭐️ 8.0/10
4. [Google TPU Inference Externalization Accelerates with InferenceX](#item-4) ⭐️ 8.0/10
5. [Urgent Call: One Year to Fix Security Before AI Exploits It](#item-5) ⭐️ 7.0/10
6. [TALA, D2's Advanced Layout Engine, Goes Open Source](#item-6) ⭐️ 7.0/10
7. [Abusive crawlers overwhelm git.kernel.org](#item-7) ⭐️ 7.0/10
8. [OpenAI Chief Scientist Advocates for Defensive AI, Warns Against Reckless Racing](#item-8) ⭐️ 7.0/10
9. [Latent Space Launches AEO Tracker for Frontier Model Choices](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI Unveils GPT-6 Astra, Its Most Capable Model Yet](https://news.google.com/rss/articles/CBMiTkFVX3lxTE11QUxBUVJLdC1jSmtJbmcxQzg4Qm9yUlNPS3JEMEVBanIyY1FRT2k2R0hBTlNnX2VqcWpTSDJUMDV0TjBJN1VGamlrZzVPZw?oc=5) ⭐️ 9.0/10

OpenAI has announced GPT-6 Astra, a new generation of its flagship language model, which is rolling out today to a limited set of organizations and will become available to all ChatGPT Plus, Pro, Business, and Enterprise users, as well as via the OpenAI API, Microsoft Azure, and AWS Bedrock in the coming days. This release marks the first model to reach the Critical level of cybersecurity capability under OpenAI's Preparedness Framework. GPT-6 Astra represents a significant leap in AI capability, particularly in complex reasoning, coding, computer use, and research, which could accelerate adoption across industries and redefine what is possible with AI assistants. Its Critical cybersecurity rating also signals a new era where AI systems possess advanced defensive and offensive capabilities, raising important considerations for safety and governance. GPT-6 Astra is included in existing subscription allowances, with options to purchase additional credits for extra usage. According to a GIGAZINE report, it scored 67 points in AI coding performance, demonstrating outstanding token efficiency, but still fell short of Fable 5.1.

google_news · OpenAI · Sep 8, 06:32

**Background**: GPT-6 Astra is the latest iteration in OpenAI's GPT series, building on previous models like GPT-4 and GPT-5. The model is designed for end-to-end work, handling complex tasks that require deep reasoning and multi-step execution. OpenAI's Preparedness Framework categorizes models based on their capabilities in areas like cybersecurity, and reaching the Critical level indicates a high degree of proficiency that requires careful deployment and monitoring.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>
<li><a href="https://deploymentsafety.openai.com/gpt-6-astra">GPT-6 Astra System Card - Deployment Safety Hub - OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-6-astra">GPT-6 Astra Model | OpenAI API</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-6`, `#AI`, `#language model`, `#announcement`

---

<a id="item-2"></a>
## [Factoring 90s CA RSA Keys with a Consumer GPU](https://mcpherrin.ca/2026/09/07/rsa.html) ⭐️ 8.0/10

An article describes how the author successfully factored the RSA keys of a Certificate Authority from the 1990s using a consumer GPU, taking about two days. This demonstrates the practical cracking of 512-bit RSA keys with modern hardware. This highlights the historical weakness of short RSA keys and raises concerns about retroactive decryption of past encrypted communications. It underscores the importance of using sufficiently long keys and the potential privacy risks from recorded encrypted data. The author targeted a 512-bit RSA key from a 90s CA, using a consumer GPU to factor it in about two days. The article also mentions a custom TLS implementation needed to interact with the target client, Netscape Communicator 4.51, due to Go's crypto/tls dropping SSLv3 support.

hackernews · ahlCVA · Sep 8, 01:16 · [Discussion](https://news.ycombinator.com/item?id=49604637)

**Background**: RSA encryption relies on the difficulty of factoring the product of two large prime numbers. In the 1990s, 512-bit keys were common but are now considered weak; modern GPUs can factor them quickly. Certificate Authorities (CAs) issue digital certificates that vouch for the identity of websites, and their private keys are crucial for trust in HTTPS.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RSA_Factoring_Challenge">RSA Factoring Challenge - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/RSA_cryptosystem">RSA cryptosystem - Wikipedia</a></li>
<li><a href="https://querychart.io/visual-explanations/how-https-works">How HTTPS Works — the TLS handshake explained — QueryChart</a></li>

</ul>
</details>

**Discussion**: Community comments express a mix of fascination and concern. Some note the ease of cracking 512-bit keys and worry about governments recording encrypted traffic for future decryption. Others criticize the use of LLM-generated content without thorough verification, and one commenter asks how long people in the 90s expected such cracking to become feasible.

**Tags**: `#RSA`, `#cryptography`, `#security`, `#history`, `#GPU cracking`

---

<a id="item-3"></a>
## [Broadcom's VDDK Removal Complicates VMware Migrations](https://www.virtualizationhowto.com/2026/09/leaving-vmware-just-got-harder-after-broadcom-pulled-vddk-downloads/) ⭐️ 8.0/10

Broadcom has removed public downloads of the VMware Virtual Disk Development Kit (VDDK), a critical tool for migrating virtual machines away from VMware. This change, reported in September 2026, affects migration paths that rely on VDDK for efficient disk access. This move increases vendor lock-in for VMware customers, making it harder and more costly to migrate to alternative platforms like KVM or Proxmox. It signals Broadcom's strategy to extract maximum value from VMware, potentially accelerating customer churn and sparking community backlash. VDDK is a collection of C/C++ libraries and utilities that enable fast disk reads during migration; without it, transfers fall back to slower paths, and for vSAN-backed VMs, VDDK is mandatory. The VDDK cannot be redistributed, so third-party tools that depend on it are also affected.

hackernews · josephcsible · Sep 7, 20:32 · [Discussion](https://news.ycombinator.com/item?id=49602699)

**Background**: VMware has long been a dominant virtualization platform, but after Broadcom acquired it, the company has made controversial changes to licensing and support. VDDK is essential for many migration tools, such as those used to move VMs to KVM or Proxmox, because it provides efficient access to virtual disk data. Without public access, migration becomes significantly more complex, especially for enterprise environments.

<details><summary>References</summary>
<ul>
<li><a href="https://platform9.com/blog/vddk-no-longer-available/">Broadcom Cut Public Access of Virtual Disk Development Kit ...</a></li>
<li><a href="https://aenix.io/migration/vmware/">VMware migration — exit VCF without breaking the application – Ænix</a></li>
<li><a href="https://dev.to/ptp2308/how-to-vm-migrate-from-vmware-to-kvm-key-tips-and-pitfalls-522c">How to vm migrate from vmware to kvm — key tips... - DEV Community</a></li>

</ul>
</details>

**Discussion**: Community comments express sadness and frustration over Broadcom's approach, with former VMware engineers lamenting the decline of innovation. Some users share practical migration experiences, noting that Proxmox migrations were surprisingly painless, while others advocate for moving to KVM and investing in internal skills to avoid vendor lock-in.

**Tags**: `#VMware`, `#Broadcom`, `#VDDK`, `#virtualization`, `#migration`

---

<a id="item-4"></a>
## [Google TPU Inference Externalization Accelerates with InferenceX](https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam) ⭐️ 8.0/10

SemiAnalysis published the first third-party inference results for Google's TPUv7 Ironwood on InferenceX Official Preview, showing up to 50% better performance per dollar compared to NVIDIA B200/B300 in apples-to-apples tests. This marks a significant step in Google's externalization of its TPU inference stack. This development challenges NVIDIA's CUDA dominance in AI inference by offering a competitive alternative with better cost efficiency. As Google externalizes its TPU stack, customers gain more choices, potentially reshaping the AI hardware landscape and reducing the CUDA moat. Ironwood (TPUv7) is the first generation where Google competes for external inference workloads with chips that can be purchased outright or rented via its cloud. The advantage extends across much of the Pareto curve, and the analysis examines both Google's internal TCO and the external TCO for customers.

rss · Semianalysis · Sep 7, 20:00

**Background**: TPUs (Tensor Processing Units) are Google's custom application-specific integrated circuits (ASICs) designed to accelerate machine learning workloads, particularly neural network inference and training. InferenceX appears to be a platform or program through which Google offers its TPU inference capabilities externally, allowing third parties to benchmark and use them. Historically, TPUs were primarily used internally by Google, but with Ironwood, Google is actively competing for external inference workloads against NVIDIA GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam">TPU Inference Externalization Full Steam Ahead - InferenceX</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tensor_Processing_Unit">Tensor Processing Unit - Wikipedia</a></li>
<li><a href="https://www.servethehome.com/googles-tpuv8s-for-training-and-inference-at-hot-chips-2026/">Google's TPUv 8 s for Training and Inference at Hot... - ServeTheHome</a></li>

</ul>
</details>

**Tags**: `#TPU`, `#AI inference`, `#hardware`, `#NVIDIA`, `#CUDA`

---

<a id="item-5"></a>
## [Urgent Call: One Year to Fix Security Before AI Exploits It](https://jyn.dev/a-year-to-fix-security/) ⭐️ 7.0/10

The author argues that we have only one year to fix widespread software security issues before AI makes exploitation trivial, urging a collective effort to secure software. The article has sparked significant discussion, with 105 points and 63 comments. This matters because AI models are becoming increasingly adept at identifying vulnerabilities, potentially lowering the barrier for cyberattacks. If the security community fails to act, we may face a surge in automated exploits that outpace traditional defenses. The article references Apple's upcoming M5 Mac Studio with 256GB unified memory as an example of hardware that could run LLMs locally, though commenters note that even such hardware would not run code in 3 seconds as the author implies. The discussion highlights that cost and scale remain limiting factors for AI-driven hacking campaigns.

hackernews · saikatsg · Sep 8, 04:48 · [Discussion](https://news.ycombinator.com/item?id=49605691)

**Background**: Large Language Models (LLMs) are AI systems trained on vast text data, capable of understanding and generating code, which can be used to identify security vulnerabilities. The article suggests that as LLMs improve, they could automate the discovery and exploitation of software flaws, making it easier for attackers. The urgency stems from the rapid pace of AI advancement, which may outstrip the security community's ability to patch vulnerabilities.

**Discussion**: Commenters generally agree with the urgency, with some saying we have even less than a year. They debate the feasibility of fixing security, noting historical neglect due to cost, and suggest simplifying software stacks. Some push back on the author's claims about LLM performance, pointing out that running LLMs locally is slower than implied.

**Tags**: `#security`, `#AI`, `#LLM`, `#vulnerabilities`, `#software engineering`

---

<a id="item-6"></a>
## [TALA, D2's Advanced Layout Engine, Goes Open Source](https://d2lang.com/blog/tala-is-open-source/) ⭐️ 7.0/10

TALA, the proprietary layout engine developed by Terrastruct for D2 diagrams, has been open-sourced. The source code is now available on GitHub, and users can specify TALA as the layout engine by setting the environment variable D2_LAYOUT. This move makes a high-quality layout engine accessible to the broader diagramming community, potentially improving the default experience for D2 users and enabling community contributions to its development. It also signals a shift in Terrastruct's business model, as TALA was previously a paid product. TALA is designed specifically for software architecture diagrams and is a separate install from D2 to maintain a clear distinction between the free and open-source D2 and the previously proprietary TALA. The open-source release includes the full source code, allowing users to build and integrate it themselves.

hackernews · alixanderwang · Sep 7, 23:37 · [Discussion](https://news.ycombinator.com/item?id=49604150)

**Background**: D2 is an open-source declarative diagramming language that allows users to define diagrams in text. TALA is a layout engine that automatically positions nodes and edges in a diagram, and it was previously a proprietary product offered by Terrastruct, the company behind D2. Layout engines like TALA, ELK, and Graphviz are used to compute the visual arrangement of diagrams, which can significantly affect readability and aesthetics.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/terrastruct/TALA">GitHub - terrastruct/TALA: A diagram layout engine designed specifically for software architecture diagrams · GitHub</a></li>
<li><a href="https://d2lang.com/tour/tala/">TALA | D2 Documentation</a></li>
<li><a href="https://terrastruct.com/tala/">TALA | Terrastruct's AutoLayout Approach</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some praise TALA's improved layouts over default D2 and ELK, while others point out specific cases where TALA's output is worse, such as the Go queue example. There are also concerns about the website's mobile compatibility, and questions about whether TALA could be integrated into Graphviz.

**Tags**: `#open-source`, `#diagramming`, `#layout-engine`, `#D2`, `#visualization`

---

<a id="item-7"></a>
## [Abusive crawlers overwhelm git.kernel.org](https://simonwillison.net/2026/Sep/7/creepy-crawlies/) ⭐️ 7.0/10

Konstantin Ryabitsev reported that on git.kernel.org, rendering commits for scrapers consumes more CPU than all legitimate access combined, with 14 CPU cores across 5 geo-distributed nodes dedicated solely to this task. This highlights the growing problem of abusive web crawlers, especially AI training scrapers, which waste significant server resources and increase operational costs for open-source infrastructure. It affects maintainers and users of public repositories, potentially degrading service quality for legitimate users. The report specifically mentions that rendering git commits as HTML for scrapers is the primary CPU drain, exceeding even git clones. This is part of a broader trend where AI crawlers impose heavy loads on web servers, as discussed in various analyses.

rss · Simon Willison · Sep 7, 23:08

**Background**: git.kernel.org is the official Git repository for the Linux kernel, providing access to the source code via git clone and web interfaces. Web crawlers, including those used by search engines and AI companies, automatically fetch pages, but abusive ones can overwhelm servers by requesting resource-intensive pages like rendered commit views.

<details><summary>References</summary>
<ul>
<li><a href="https://www.amicited.com/blog/ai-crawler-impact-server-resources/">AI Crawler Impact on Server Resources : What to Expect | Am I Cited</a></li>
<li><a href="https://fusionchat.ai/news/rise-of-ai-crawlers-impact-on-web-server-resources">Rise of AI Crawlers : Impact on Web Server Resources - Fusion Chat</a></li>
<li><a href="https://www.mayrhofer.eu.org/post/defenses-against-abusive-ai-scrapers/">Defenses against abusive AI scrapers | René Mayrhofer</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion likely reflects concerns about the impact of AI crawlers on open-source infrastructure, with some suggesting mitigation strategies like blocking or rate-limiting abusive bots. The sentiment is generally sympathetic to maintainers and critical of unchecked scraping.

**Tags**: `#web crawling`, `#open source`, `#infrastructure`, `#Linux kernel`, `#resource management`

---

<a id="item-8"></a>
## [OpenAI Chief Scientist Advocates for Defensive AI, Warns Against Reckless Racing](https://simonwillison.net/2026/Sep/7/jakub-pachocki/) ⭐️ 7.0/10

OpenAI Chief Scientist Jakub Pachocki publicly argued that building powerful, aligned AI for defensive purposes is essential, while cautioning that the urgency of defense must not justify reckless AI development. This statement reflects strategic thinking from a top AI lab leader, potentially shaping industry debates on AI safety and policy. It underscores the dual-use nature of AI and the need for balanced development. Pachocki's remarks come from an OpenAI blog post titled 'An Alien Mind,' specifically the section on scalable defense. He emphasized that defensive AI will be a primary focus of OpenAI's deployment efforts, including securing infrastructure and protecting against rogue agents in real time.

rss · Simon Willison · Sep 7, 22:26

**Background**: AI alignment aims to steer AI systems toward intended goals and ethical principles. OpenAI has been exploring defensive AI measures, such as securing infrastructure and defending against prompt injection attacks, as part of broader safety efforts.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment - Wikipedia</a></li>
<li><a href="https://www.analyticsvidhya.com/blog/2024/05/openai-security-measures/">6 Latest OpenAI Security Measures for Advanced AI Infrastructure</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#OpenAI`, `#AI ethics`, `#AI policy`

---

<a id="item-9"></a>
## [Latent Space Launches AEO Tracker for Frontier Model Choices](https://www.latent.space/p/aeo) ⭐️ 7.0/10

Latent Space has introduced a new project, the Frontier AEO Tracker, which tracks AEO trends and the choices made by frontier AI models, aiming to provide insights for founders and developer experience leaders. This tracker addresses a trending and practical topic (AEO) that is highly relevant for AI/ML practitioners and companies looking to optimize their visibility in AI-driven search and answers. It could help shape strategies for developer experience and product positioning in an evolving AI landscape. The article is the first Astra project from Latent Space, focusing on AEO trends, a top-asked topic from founders and DX leaders. The tracker aims to document which frontier models are chosen and what can be done about it, though specific details on methodology or data sources are not yet provided.

rss · Latent Space · Sep 7, 21:32

**Background**: AEO, or Answer Engine Optimization, is an emerging practice focused on optimizing content to be featured in AI-generated answers, such as those from ChatGPT or Google's AI Overviews. It differs from traditional SEO, which targets search engine rankings. As AI assistants become more prevalent, AEO is gaining attention from businesses seeking to maintain visibility. The term 'Astra' in the article likely refers to a project name within Latent Space, not Google's Project Astra, which is a separate AI assistant research prototype.

<details><summary>References</summary>
<ul>
<li><a href="https://rankandrevenue.com/aeo-ai-search-optimization">AEO & AI Optimization | Boost Rankings & Revenue Now — Rank...</a></li>
<li><a href="https://www.loudface.co/blog/best-aeo-agencies">Best GEO, AEO & AI Search Agencies 2026 | LoudFace</a></li>
<li><a href="https://deepmind.google/models/project-astra/">Project Astra — Google DeepMind</a></li>

</ul>
</details>

**Tags**: `#AEO`, `#AI`, `#frontier models`, `#developer experience`, `#trends`

---