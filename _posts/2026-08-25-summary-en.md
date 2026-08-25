---
layout: default
title: "Horizon Summary: 2026-08-25 (EN)"
date: 2026-08-25
lang: en
---

> From 33 items, 9 important content pieces were selected

---

1. [MS Paint and Photos Embed Invisible GUID Watermarks in AI Images](#item-1) ⭐️ 8.0/10
2. [Interactive Moon Visualization by Ciechanowski](#item-2) ⭐️ 8.0/10
3. [Entire San Francisco Rendered as Explorable 3D Web Game](#item-3) ⭐️ 8.0/10
4. [XMPP Celebrates 25 Years of Digital Independence](#item-4) ⭐️ 8.0/10
5. [IPFS Maintainers Shipyard Winding Down, Project Continues](#item-5) ⭐️ 8.0/10
6. [SQLite Database File Crafted as Executable Linux Binary](#item-6) ⭐️ 8.0/10
7. [OpenAI Releases GPT-5.6 in Kiro with Improved Price-Performance](#item-7) ⭐️ 8.0/10
8. [Claude Code Overtakes GitHub Copilot in Developer Market Share](#item-8) ⭐️ 8.0/10
9. [OpenBMB Releases MathForm 8B for Automated Math Formalization](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [MS Paint and Photos Embed Invisible GUID Watermarks in AI Images](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

Microsoft Paint and Photos now silently embed invisible GUID watermarks into images that have been AI-manipulated, even when using local models. The watermark is applied via a function called ApplyWatermark and cannot be disabled by the user. This raises significant privacy and anonymity concerns, as the unique GUID can be traced back to the user's Microsoft account, potentially exposing personal information. It also highlights a broader trend of invisible watermarking in consumer software, which could impact content creators and privacy advocates. The watermark is embedded even when using local AI models, and in Paint, a watermarking failure causes the image generation to fail, while in Photos, it logs an error but still returns the image. The GUID is server-issued, and the watermarking process is performed by Watermarker.dll.

hackernews · ComputerGuru · Aug 24, 15:28 · [Discussion](https://news.ycombinator.com/item?id=49421158)

**Background**: Digital watermarking is a technique used to embed hidden information into media files to identify ownership or track usage. Invisible watermarks are imperceptible to the human eye but can be extracted by software. Microsoft's implementation uses a GUID (Globally Unique Identifier) to uniquely identify each image, which can be linked to the user's account.

<details><summary>References</summary>
<ul>
<li><a href="https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/">Microsoft Paint and Photos Embed Server-Issued GUIDs as Invisible Watermarks in Locally-Generated Images :: Xusheng Li</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_watermarking">Digital watermarking - Wikipedia</a></li>
<li><a href="https://www.brookings.edu/articles/detecting-ai-fingerprints-a-guide-to-watermarking-and-beyond/">Detecting AI fingerprints: A guide to watermarking and beyond | Brookings</a></li>

</ul>
</details>

**Discussion**: The community is concerned about the privacy implications, with one commenter noting that the invisible watermark could be used to subpoena user data from Microsoft. Another commenter points out that Microsoft has a history of sloppy implementations, citing a previous incident with Copilot watermarks in Azure DevOps commits. Some users are also surprised that MS Paint has evolved beyond a simple pixel editor.

**Tags**: `#privacy`, `#watermarking`, `#Microsoft`, `#AI`, `#security`

---

<a id="item-2"></a>
## [Interactive Moon Visualization by Ciechanowski](https://ciechanow.ski/moon/) ⭐️ 8.0/10

Bartosz Ciechanowski released 'Moon (2024)', an interactive and highly detailed visualization of the Moon, offering multiple perspectives and educational insights. The page showcases advanced web techniques for immersive learning. This visualization exemplifies the future of web-based education, making complex astronomical concepts intuitive and engaging. It sets a standard for interactive content that could influence how educational resources are designed across the web. The visualization includes multiple perspectives, such as a virtual planet view, and is praised for its detail and clarity. It is part of Ciechanowski's series of interactive explanations that combine technical depth with aesthetic appeal.

hackernews · simonebrunozzi · Aug 24, 22:06 · [Discussion](https://news.ycombinator.com/item?id=49426466)

**Background**: Bartosz Ciechanowski is known for creating interactive articles that explain complex topics using custom JavaScript visualizations. His works often cover physics, astronomy, and engineering, making them accessible to a broad audience. This Moon visualization continues that tradition, offering a hands-on way to explore lunar features and motions.

**Discussion**: Community comments express admiration for Ciechanowski's work, with some noting that his style has become a benchmark for interactive web content. There is also discussion about the potential influence of AI-assisted development in making such pages more common, and a suggestion for adding a table of contents for easier navigation.

**Tags**: `#interactive visualization`, `#moon`, `#web development`, `#education`, `#Bartosz Ciechanowski`

---

<a id="item-3"></a>
## [Entire San Francisco Rendered as Explorable 3D Web Game](https://sf.thijs.gg/) ⭐️ 8.0/10

A web-based project at sf.thijs.gg renders the entire city of San Francisco as an explorable 3D video game environment, viewable directly in a browser. The project has gained significant community attention, with 363 points and 122 comments on Hacker News. This project demonstrates the feasibility of creating large-scale, interactive 3D city environments using web technologies, which could inspire new applications in gaming, urban planning, and virtual tourism. It also highlights the potential for community-driven development of realistic city maps for game engines like GTA. The project uses elevation data, building data, and map imagery to construct the 3D environment, and includes features like driving vehicles and collecting coins. Community members have noted that the implementation may be based on reverse-engineered Apple map data, similar to the retroplasma project, and have suggested improvements such as street names, landmarks, and address teleportation.

hackernews · centrosphere · Aug 24, 17:05 · [Discussion](https://news.ycombinator.com/item?id=49422784)

**Background**: Creating 3D city models from real-world data is a complex task that involves processing elevation, building footprints, and textures. Web-based 3D rendering has advanced significantly, allowing interactive experiences directly in browsers. Similar projects, such as a Seattle N64-style map, show a growing interest in recreating real cities in game-like environments.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/San_Francisco_Rush:_Extreme_Racing">San Francisco Rush: Extreme Racing - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Category:Video_games_set_in_San_Francisco">Category:Video games set in San Francisco - Wikipedia</a></li>
<li><a href="https://www.cgtrader.com/3d-models/san-francisco">San francisco 3D Models – Free & Premium Downloads | CGTrader</a></li>

</ul>
</details>

**Discussion**: Community comments express enthusiasm and emotional resonance, with one user who lived in SF for 20 years finding it moving to explore familiar places. Users discuss technical implementation details, such as the use of Apple map data and potential for GTA-style maps, and suggest features like street names and address search. Some also share related projects, like a Seattle N64-style map.

**Tags**: `#3D rendering`, `#San Francisco`, `#web development`, `#interactive maps`, `#gaming`

---

<a id="item-4"></a>
## [XMPP Celebrates 25 Years of Digital Independence](https://gultsch.de/posts/25-years-of-digital-independence/) ⭐️ 8.0/10

Daniel Gultsch published an anniversary retrospective marking 25 years of Jabber/XMPP, emphasizing its role in digital independence and the ongoing community efforts to keep it relevant. This milestone highlights XMPP's enduring relevance as a decentralized messaging standard, offering an alternative to proprietary platforms. It underscores the importance of open standards for digital sovereignty, especially as Europe seeks greater independence. The article reflects on XMPP's history and its community-driven development, noting that it was not created to fit a particular zeitgeist. It also discusses the protocol's adaptability and the ongoing work by projects like Movim and Fluux to modernize the ecosystem.

hackernews · inputmice · Aug 24, 15:51 · [Discussion](https://news.ycombinator.com/item?id=49421536)

**Background**: XMPP (Extensible Messaging and Presence Protocol) is an open standard for real-time messaging and presence, originally developed as Jabber in 1999. It uses a client-server architecture and is known for its decentralization and extensibility, allowing federated servers to interoperate. Over the years, it has been used by major companies like Google and Facebook, though many later moved to proprietary protocols.

<details><summary>References</summary>
<ul>
<li><a href="https://gultsch.de/posts/25-years-of-digital-independence/">Daniel Gultsch | Jabber/ XMPP : 25 Years of Digital Independence</a></li>
<li><a href="https://zeli.app/story/49421536">XMPP at 25: The Open Standard That Refuses to Die... | Zeli</a></li>
<li><a href="https://news.ycombinator.com/item?id=49421536">Jabber/ XMPP : 25 Years of Digital Independence | Hacker News</a></li>

</ul>
</details>

**Discussion**: Community comments express enthusiasm for XMPP's future, citing projects like Movim and Fluux, and lamenting that Matrix did not build on XMPP. Some users share practical use cases, such as using XMPP for telephony bridging or as an agent communication layer, while others question its current adoption compared to Matrix.

**Tags**: `#XMPP`, `#decentralization`, `#protocols`, `#messaging`, `#open-source`

---

<a id="item-5"></a>
## [IPFS Maintainers Shipyard Winding Down, Project Continues](https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/) ⭐️ 8.0/10

The IPFS maintainer team at Shipyard announced they are winding down their centralized maintenance efforts, transitioning to individual grants for IPFS development. This change does not mean the IPFS project itself is shutting down. This shift marks a significant change in how IPFS is maintained, potentially affecting the pace and coordination of development. It highlights the challenges of sustaining open-source infrastructure and may influence community trust and adoption. The announcement clarifies that only the Shipyard maintainer team is sunsetting, not the IPFS project. The transition to individual grants means future IPFS work will be funded on a per-project basis, which could lead to more fragmented but potentially more diverse contributions.

hackernews · iand · Aug 24, 15:48 · [Discussion](https://news.ycombinator.com/item?id=49421489)

**Background**: IPFS (InterPlanetary File System) is a peer-to-peer hypermedia protocol designed to make the web faster, safer, and more open. Shipyard was a team within Protocol Labs that provided centralized maintenance and support for various IPFS implementations and tools. The IPFS ecosystem also relies on a grant platform to fund community-driven development.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ipfs-shipyard">IPFS Shipyard · GitHub</a></li>
<li><a href="https://blog.ipfs.tech/shipyard-hello-world/">IPFS & libp2p Devs Go Independent: Meet Interplanetary Shipyard</a></li>
<li><a href="https://github.com/ipfs/devgrants">GitHub - ipfs/devgrants: The IPFS Grant platform connects funding organizations with builders and researchers in the IPFS community. · GitHub</a></li>

</ul>
</details>

**Discussion**: Community comments clarify that the announcement is about Shipyard, not IPFS, and express sadness over the change. Some suggest alternative projects like Iroh, while others criticize the use of Google Forms for feedback, highlighting a desire for more decentralized solutions.

**Tags**: `#IPFS`, `#decentralization`, `#open source`, `#maintenance`, `#p2p`

---

<a id="item-6"></a>
## [SQLite Database File Crafted as Executable Linux Binary](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/) ⭐️ 8.0/10

Farid Zakaria has demonstrated a technique to create a SQLite database file that can also be executed as a Linux binary by embedding ELF components into SQLite tables and using a custom interpreter called self-exec. The trick leverages the SQLite application ID field set to 'SELF' and the Linux binfmt_misc mechanism to invoke the interpreter. This proof-of-concept could inspire new approaches to software distribution and introspection, where a single file serves dual purposes as both a database and an executable. It highlights the flexibility of SQLite as an application file format and the extensibility of the Linux kernel through binfmt_misc. The SQLite application ID is a 4-byte field at offset 68 in the file, set to 'SELF' to mark the file as a Structured Executable & Linkable Format. The ELF components are stored across multiple SQLite tables according to a schema, and the self-exec interpreter extracts and executes them. Registration with binfmt_misc can be done via a command like 'printf ... > /proc/sys/fs/binfmt_misc/register'.

rss · Simon Willison · Aug 24, 11:38

**Background**: SQLite is a popular embedded database that stores data in a single file, and its file format includes an application ID field for identifying the application that created the file. ELF is the standard executable format on Linux, containing headers, sections, and segments that define how the program should be loaded and executed. binfmt_misc is a Linux kernel feature that allows custom binary formats to be recognized and executed via an interpreter, typically used for emulation or scripting languages.

<details><summary>References</summary>
<ul>
<li><a href="https://stackoverflow.com/questions/35557487/where-can-i-register-a-sqlite-application-id">registration - Where can I register a sqlite application ID? - Stack Overflow</a></li>
<li><a href="https://en.wikipedia.org/wiki/Executable_and_Linkable_Format">Executable and Linkable Format - Wikipedia</a></li>
<li><a href="https://docs.kernel.org/admin-guide/binfmt-misc.html">Kernel Support for miscellaneous Binary Formats (binfmt_misc) — The Linux Kernel documentation</a></li>

</ul>
</details>

**Tags**: `#SQLite`, `#ELF`, `#Linux`, `#executable`, `#binfmt_misc`

---

<a id="item-7"></a>
## [OpenAI Releases GPT-5.6 in Kiro with Improved Price-Performance](https://openai.com/index/gpt-5-6-in-kiro) ⭐️ 8.0/10

OpenAI has released GPT-5.6, now available in the Kiro agentic IDE, offering developers improved price-performance for planning, building, reviewing, and testing software. The model comes in three variants—Sol, Terra, and Luna—with discounted pricing through at least November 21, 2026. This release strengthens OpenAI's position in the competitive AI coding assistant market, directly challenging offerings from Anthropic and other providers. The improved price-performance could lower barriers for developers adopting AI-assisted development, potentially accelerating the shift toward agentic engineering. The pricing schedule shows gpt-5.6-sol at $4.00 input and $20.00 output per million tokens, with Terra and Luna at lower price points. The announcement includes a 20% discount on input and 33% on output through at least November 21, 2026, and Kiro is an agentic IDE that supports spec-driven development and parallel agents.

rss · OpenAI News · Aug 24, 12:00

**Background**: Kiro is an agentic IDE introduced by AWS that goes beyond simple AI coding assistance, enabling autonomous, goal-driven actions. GPT-5.6 is OpenAI's latest model family, designed to deliver more useful work per token, with variants optimized for different performance and cost needs.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-6-in-kiro/">Advancing price - performance for developers with GPT ‑ 5 . 6 in... | OpenAI</a></li>
<li><a href="https://github.com/kirodotdev/Kiro">GitHub - kirodotdev/Kiro: Kiro is an agentic IDE that works alongside you from prototype to production. · GitHub</a></li>
<li><a href="https://artificialanalysis.ai/models/gpt-5-6-sol">GPT - 5 . 6 Sol (max) - Intelligence, Performance & Price Analysis</a></li>

</ul>
</details>

**Discussion**: Community comments express enthusiasm for the price war, with some praising the affordability and open-source models. One user notes the 50% off at OpenRouter, bringing costs down further, while another shares detailed opinions on Sol's performance in complex tasks, suggesting it may struggle with long, multi-step projects compared to alternatives like Fable.

**Tags**: `#OpenAI`, `#GPT-5.6`, `#AI model`, `#developer tools`, `#price-performance`

---

<a id="item-8"></a>
## [Claude Code Overtakes GitHub Copilot in Developer Market Share](https://news.google.com/rss/articles/CBMif0FVX3lxTE52bmFnekZfN2pVSHd5RnU2RmFXbW9MeDNVVWRENWhmend5VHdCU3hjUmR2VlEtbl9ETEItam8tZnFyR05iUGQzc3RhQXRMS1FZRXVVX0ZPWHF0cDNBVHo2YzA0WjFfZ3I1NDZRTXZYQl9VaGFGdm11YTYyZUVGMzg?oc=5) ⭐️ 8.0/10

A recent survey reveals that 90% of professional developers now use AI coding agents at least once a week, and Anthropic's Claude Code has overtaken GitHub Copilot to become the leading tool, holding nearly double the market share. This marks a significant shift in the AI coding tools landscape, indicating that developers increasingly prefer agentic tools that can autonomously plan and execute tasks over traditional code assistants. It also highlights the rapid adoption of AI in software development, which could reshape developer workflows and productivity. The survey specifically highlights Claude Code's rise to the top spot with nearly double the market share of GitHub Copilot. This suggests that while GitHub Copilot remains popular, developers are increasingly adopting more advanced agentic tools that offer deeper codebase understanding and autonomous execution.

google_news · GIGAZINE · Aug 24, 01:52

**Background**: AI coding agents are systems that can plan multi-step tasks, write code, execute it, and observe results without step-by-step human guidance. Claude Code, developed by Anthropic, is an agentic coding tool that understands codebases, edits files, and runs commands to help developers ship faster. GitHub Copilot, on the other hand, is a widely used AI pair programmer that suggests code snippets in the editor. The shift in market share reflects a growing preference for tools that can handle more complex, autonomous tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/resources/articles/what-are-ai-agents">What are AI agents? · GitHub</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-are-ai-coding-agents">What Is an AI Coding Agent? How They Work and When to Use Them | MindStudio</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**Tags**: `#AI coding agents`, `#Claude Code`, `#GitHub Copilot`, `#developer tools`, `#market share`

---

<a id="item-9"></a>
## [OpenBMB Releases MathForm 8B for Automated Math Formalization](https://news.google.com/rss/articles/CBMiSkFVX3lxTE5NNG4wWC1EbVNYM3RKM2V0UGZwakJhVm5ZY05BMDNsWEdEQVJaZk1McFh2bDZTVmR6S1dQSFJNOF9XNHNvSy14TEFR?oc=5) ⭐️ 8.0/10

OpenBMB has open-sourced MathForm-8B, an 8-billion-parameter model that translates natural-language mathematical statements into Lean 4 formal proofs. The model, along with the FormalVerse dataset of about 367,000 verified examples, is released under the Apache 2.0 license. This open-source release democratizes access to advanced autoformalization technology, previously dominated by tech giants, and could accelerate research in formal verification and AI-assisted mathematics. It also provides a strong baseline for the community to build upon, potentially improving theorem proving and math education tools. MathForm-8B is an 8B causal language model in BF16 with a chat template, and it achieves the strongest overall performance among specialized autoformalizers on six benchmarks despite its smaller size. The accompanying FormalVerse dataset contains roughly 367,000 verified Lean 4 examples, and the model is released under the Apache 2.0 license.

google_news · AIBase · Aug 24, 04:14

**Background**: Automated formalization of mathematics involves translating informal mathematical statements into formal languages like Lean 4, which can be verified by proof assistants. This field has grown rapidly with the rise of deep learning, and models like MathForm-8B aim to automate this translation process, making formal verification more accessible.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/openbmb/MathForm-8B">openbmb/ MathForm - 8 B · Hugging Face</a></li>
<li><a href="https://www.orcarouter.ai/blog/what-is-mathform-8b">What Is MathForm - 8 B ? OpenBMB's Quiet Lean 4 Autoformalizer</a></li>
<li><a href="https://arxiv.org/html/2608.14221">MathForm : Scaling Mathematical Autoformalization with Knowledge...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#formalization`, `#mathematics`, `#open-source`, `#LLM`

---