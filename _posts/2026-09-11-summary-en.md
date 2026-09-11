---
layout: default
title: "Horizon Summary: 2026-09-11 (EN)"
date: 2026-09-11
lang: en
---

> From 38 items, 14 important content pieces were selected

---

1. [OpenAI Unveils GPT-6 Astra, Its Most Intelligent and Aligned Model Yet](#item-1) ⭐️ 9.0/10
2. [Shopify migrates its mobile app from React Native back to native Swift and Kotlin](#item-2) ⭐️ 8.0/10
3. [OpenAI Launches Agents API with Self-Hosted Sandbox Option](#item-3) ⭐️ 8.0/10
4. [Mathematicians question whether OpenAI can be trusted with unpublished ideas](#item-4) ⭐️ 8.0/10
5. [Forgejo 16.0.4 Patches Critical RCE in Template Repositories](#item-5) ⭐️ 8.0/10
6. [Microsoft Designates Rust as a Tier-1 Language](#item-6) ⭐️ 8.0/10
7. [trynix.dev boots any Nix package in the browser via qemu-wasm](#item-7) ⭐️ 8.0/10
8. [Shopify Returns to Native Mobile, Citing AI Coding Agents](#item-8) ⭐️ 8.0/10
9. [OpenAI Launches ChatGPT for Financial Services with GPT-6 Astra](#item-9) ⭐️ 8.0/10
10. [Datasette 1.0a39 and 0.65.4 Patch AI-Found Security Flaws](#item-10) ⭐️ 7.0/10
11. [Researcher Uses Codex and ChatGPT to Mine Genomes for Antimicrobials](#item-11) ⭐️ 7.0/10
12. [OpenAI launches Data agent in ChatGPT Work for enterprise analytics](#item-12) ⭐️ 7.0/10
13. [OpenAI and GSA Offer Free ChatGPT Licenses to U.S. Governments](#item-13) ⭐️ 7.0/10
14. [OpenAI launches GPT-Live-1 voice model in its API](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI Unveils GPT-6 Astra, Its Most Intelligent and Aligned Model Yet](https://news.google.com/rss/articles/CBMiTkFVX3lxTE11QUxBUVJLdC1jSmtJbmcxQzg4Qm9yUlNPS3JEMEVBanIyY1FRT2k2R0hBTlNnX2VqcWpTSDJUMDV0TjBJN1VGamlrZzVPZw?oc=5) ⭐️ 9.0/10

OpenAI announced GPT-6 Astra, described as its most intelligent and aligned model yet, with state-of-the-art capabilities in computer use, coding, cybersecurity, and science. The model was initially released to approved users on September 3, 2026, with general availability the following day, and is now available in ChatGPT Work, Codex, and the API. OpenAI calls Astra a "generational leap" for cybersecurity, professional work, software engineering, and science, with president Greg Brockman claiming it could eventually be seen as the arrival of artificial general intelligence (AGI). This positions GPT-6 Astra as a potential industry-changing release that could reshape how teams approach demanding professional and technical work. Astra is positioned as state-of-the-art across computer use, browsing, professional work, software engineering, cybersecurity, and science, and OpenAI frames it as its most aligned model to date. The rollout began with approved users on September 3, 2026, followed by general availability on September 4, 2026, across ChatGPT Work, Codex, and the API.

google_news · openai.com · Sep 11, 06:36

**Background**: GPT-6 Astra is a large language model (LLM) developed by OpenAI, the American AI firm behind the GPT series and ChatGPT. OpenAI has previously defined AGI as "an automated system that can perform all economically valuable work as well as or better than humans," a benchmark that Brockman suggests Astra could eventually be associated with. The model's launch follows OpenAI's pattern of releasing increasingly capable models into both consumer products and developer APIs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra - Wikipedia</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>
<li><a href="https://openai.com/index/gpt-6-astra-next-generation-work/">GPT-6 Astra: The next generation in intelligence for work | OpenAI</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-6`, `#LLM`, `#AI`, `#announcement`

---

<a id="item-2"></a>
## [Shopify migrates its mobile app from React Native back to native Swift and Kotlin](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify announced on its engineering blog that it is migrating its mobile app away from React Native and back to fully native Swift (iOS) and Kotlin (Android) codebases. The post, titled 'Back to Native', triggered a large Hacker News discussion with 973 points and 655 comments. Shopify is one of the largest consumer-facing apps to abandon a cross-platform framework in favor of native development, making it a significant industry signal about the trade-offs of React Native at scale. The move could influence how other large engineering organizations weigh cross-platform efficiency against native performance and platform fidelity. The migration means maintaining two separate codebases in Swift and Kotlin instead of one shared JavaScript/React Native codebase, trading development efficiency for closer-to-the-metal performance and platform-specific capabilities. Community commenters noted that LLM-assisted tooling can now automate much of the porting work, with one developer reporting a similar migration completed largely overnight using Codex and Maestro.

hackernews · fnthawar2 · Sep 10, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49643982)

**Background**: React Native is an open-source framework, maintained by Meta, that lets developers write one JavaScript/TypeScript codebase that renders on both iOS and Android, saving significant engineering effort. Native development instead uses Apple's Swift for iOS and Google's Kotlin for Android, giving apps direct access to platform APIs and typically better performance, but requiring separate teams and code for each platform. Many large apps have debated this trade-off, and Shopify's reversal is notable because the company had previously been a prominent React Native adopter.

<details><summary>References</summary>
<ul>
<li><a href="https://reactnative.dev/">React Native</a></li>
<li><a href="https://www.developers.dev/tech-talk/kotlin-vs-swift-which-is-best-for-app-development.html">Kotlin vs Swift : Which is Best for Native App Development ?</a></li>
<li><a href="https://techrev.us/blog/swift-vs-kotlin-for-native-app-development/">Swift vs Kotlin : Native App Development Compared... - TechRev-Blog</a></li>

</ul>
</details>

**Discussion**: Commenters were sharply divided: some iOS engineers felt validated in their long-running argument against shared codebases, while others questioned Shopify's engineering scale, noting it employs roughly 3,000 engineers for what some consider a relatively simple app. Several developers shared that LLM-assisted rewrites made similar React Native-to-native migrations surprisingly fast, and at least one questioned why Kotlin was needed at all if Swift was already being adopted.

**Tags**: `#React Native`, `#Mobile Development`, `#Swift`, `#Kotlin`, `#Cross-Platform`

---

<a id="item-3"></a>
## [OpenAI Launches Agents API with Self-Hosted Sandbox Option](https://developers.openai.com/api/docs/guides/agents-api/overview) ⭐️ 8.0/10

OpenAI has released an Agents API that lets developers build and deploy production-ready agentic applications in a single API call by specifying the task, model, tools, and environment. The API runs the Codex harness and manages the underlying agent infrastructure, with an optional self-hosted sandbox for tool execution. This is a platform-level move that positions OpenAI as the default infrastructure provider for agentic applications, potentially reshaping how developers build AI agents and intensifying competition with Anthropic's managed agents offering. It also raises significant questions about vendor lock-in, abstraction design, and the blurring line between raw LLM endpoints and full agent harnesses. The API is built around four concepts: Agent (model, instructions, tools, MCP servers), Environment (optional sandbox or computer for files, skills, and commands), Session (durable agent instance), and Events/items (inputs and outputs). It includes automatic context compaction, multi-agent orchestration, programmatic tool calling, and MCP support, with OpenAI hosting and maintaining the harness by default.

hackernews · aquir · Sep 10, 19:43 · [Discussion](https://news.ycombinator.com/item?id=49649213)

**Background**: Agentic applications are software programs built on autonomous agent infrastructure that use AI agents to interpret and execute complex tasks. Building an agent harness — the orchestration layer that manages tools, state, and execution — is a deep rabbit hole, and OpenAI's Agents API aims to abstract that away. Self-hosted sandboxes let developers keep tool execution and sensitive data in their own infrastructure while the vendor manages orchestration.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/agents-api/overview">Agents API | OpenAI API</a></li>
<li><a href="https://openai.com/index/introducing-the-agents-api/">Introducing the Agents API | OpenAI</a></li>
<li><a href="https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes">Self-hosted sandboxes - Claude Platform Docs</a></li>

</ul>
</details>

**Discussion**: Commenters broadly agree the abstraction is still unsettled, with some praising the self-hosted sandbox option as easing provider transitions and others criticizing it as vendor lock-in. A recurring theme is that the distinction between LLM endpoints and agent harnesses is becoming meaningless, and that developers may not need to lock themselves in if they can run their own VMs.

**Tags**: `#OpenAI`, `#Agents API`, `#LLM`, `#Developer Tools`, `#Vendor Lock-in`

---

<a id="item-4"></a>
## [Mathematicians question whether OpenAI can be trusted with unpublished ideas](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

A discussion on Mathstodon, amplified by a Hacker News thread with 773 points and 716 comments, raises concerns about whether mathematicians can trust OpenAI with unpublished ideas after a researcher alleged that collaborative chats may have influenced OpenAI's own published results without attribution. The episode highlights a growing tension between AI labs' data-hungry training pipelines and the norms of academic attribution, potentially deterring researchers from collaborating with frontier models and prompting calls for clearer consent and credit standards. Critics point to OpenAI's practice of using user conversations to improve models and to the timing of a 300-billion-output-token generation from a model still in training, while defenders argue that reinforcement learning on verifiable math could independently discover techniques unrelated to any specific chat.

hackernews · pred_ · Sep 10, 06:49 · [Discussion](https://news.ycombinator.com/item?id=49639408)

**Background**: Large language models are typically trained on massive text corpora, and OpenAI's terms allow certain user interactions to be used to improve model performance. In parallel, AI systems are increasingly used as research assistants in mathematics, where priority and attribution are central to academic credit. This case sits at the intersection of those two trends, raising questions about whether ideas shared in private chats can later surface in a lab's own publications.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/policies/usage-policies/">Usage policies - OpenAI</a></li>
<li><a href="https://help.openai.com/en/articles/5722486-api-data-usage-policies">How your data is used to improve model performance | OpenAI ...</a></li>
<li><a href="https://langd0n.com/blog/rethinking-ai-attribution-from-classroom-rules-to-industry-standards/">Rethinking AI Attribution : From Classroom Rules to Industry Standards</a></li>

</ul>
</details>

**Discussion**: Commenters broadly agree that if OpenAI were a human collaborator, publishing results from shared ideas without attribution would be unethical, though some argue both things can be true: chats may sharpen a model's intuition while reinforcement learning independently discovers superhuman techniques. Others suspect 'parallel construction' in the timing of the 300-billion-token generation, and several note that researchers using models on open problems are effectively feeding fresh training data.

**Tags**: `#AI ethics`, `#OpenAI`, `#research integrity`, `#mathematics`, `#attribution`

---

<a id="item-5"></a>
## [Forgejo 16.0.4 Patches Critical RCE in Template Repositories](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md) ⭐️ 8.0/10

Forgejo released versions 16.0.4 and 15.0.8 to fix a critical remote code execution vulnerability (CVE-2026-89094) affecting all versions before 16.0.4, where template expansion on files in .forgejo/template is mishandled during repository initialization from a template repository. This is a critical RCE in a widely used self-hosted Git service, meaning any instance running an unpatched version could be compromised by an attacker who can create or supply a crafted template repository, potentially leading to full server takeover. The flaw occurs because Forgejo clones a template repository, removes the .git folder, performs variable template expansion on files listed in .forgejo/template, and then initializes a new git repository; the mishandling of that expansion allows arbitrary code execution. The fix is included in 16.0.4 and 15.0.8, and the vulnerability has been assigned CVE-2026-89094.

hackernews · weierstass · Sep 10, 15:57 · [Discussion](https://news.ycombinator.com/item?id=49645907)

**Background**: Forgejo is a community-driven fork of Gitea, a lightweight self-hosted Git service similar to GitHub. Template repositories let users quickly scaffold new projects by copying a predefined repository structure and substituting variables. Because this process runs server-side during repository creation, improper handling of template expansion can let an attacker inject and execute code on the server.

<details><summary>References</summary>
<ul>
<li><a href="https://www.rapid7.com/db/vulnerabilities/cve-2026-89094/">CVE-2026-89094: Forgejo : Forgejo ... | Rapid7 Vulnerability Database</a></li>
<li><a href="https://lwn.net/Articles/1093671/">Forgejo 16.0.4 and 15.0.8 address critical security ...</a></li>
<li><a href="https://github.com/advisories/GHSA-q873-4w8p-m645">Forgejo before 16.0.4 allows remote code execution via a...</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted that Gitea is protected against both issues, noted that the release notes were initially unreadable due to Codeberg rate limits, and debated whether Forgejo's policy of disallowing LLM contributions puts it at a disadvantage since attackers may still use AI to find vulnerabilities.

**Tags**: `#security`, `#vulnerability`, `#forgejo`, `#git`, `#rce`

---

<a id="item-6"></a>
## [Microsoft Designates Rust as a Tier-1 Language](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 8.0/10

Microsoft has officially designated Rust as a Tier-1 language, placing it alongside C++, C#, and TypeScript as one of the company's best-supported canonical languages. The announcement, shared via a Rust Foundation guest post, means internal teams now have a paved path from local development to production for Rust, including secure toolchain builds, developer tooling, quality workflows, and compliance with Microsoft's Security Development Lifecycle (SDL) requirements. This is a major industry milestone that signals Rust's transition from a fast-moving newcomer to a mature, mainstream systems programming language backed by long-term corporate support. It also means all major OS vendors with a stake in C and C++ tooling have now diversified their systems-language options for greenfield development, which could accelerate Rust adoption across the wider software ecosystem. Tier-1 status at Microsoft is an engineering designation that gives internal teams a supported path from local development to production, including secure toolchain builds, productive developer tooling, quality workflows, deep platform integration, and SDL compliance. Notably, C++ still dominates Microsoft's codebase after decades of development, and the announcement also brings public news about the long-rumored MSVC integration for Rust.

hackernews · mmastrac · Sep 10, 13:39 · [Discussion](https://news.ycombinator.com/item?id=49643546)

**Background**: Rust is a systems programming language focused on memory safety and performance, originally created at Mozilla and now stewarded by the independent Rust Foundation. Microsoft has been investing in Rust for years, particularly for security-sensitive components, because Rust's ownership model prevents many memory-safety bugs that plague C and C++. A "Tier-1 language" at Microsoft is not just a preference but a formal engineering status: it means the language receives first-class tooling, secure build infrastructure, and compliance support comparable to the company's other canonical languages.

<details><summary>References</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier-1 Language at Microsoft</a></li>
<li><a href="https://www.theregister.com/devops/2026/09/11/microsoft-annoints-rust-as-a-tier-1-internal-language/5295732">Microsoft annoints Rust as a 'Tier 1' internal language</a></li>
<li><a href="https://news.ycombinator.com/item?id=49643546">Rust Is Tier - 1 Language at Microsoft | Hacker News</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters largely viewed the news as significant, with one noting that all major OS vendors with C/C++ tooling roles have now diversified their systems-language options, and another arguing it shows Rust is no longer a "fledgling" language but a mature competitor to C++ and C#. Several commenters were skeptical about automatically converting large legacy C++ codebases to Rust, calling it an AGI-level "Millennium problem," though some suggested converting even 50% of code automatically would be a great outcome. Others highlighted that this year's RustConf focused on C++/Python/JavaScript interop rather than "rewrite it in Rust," reflecting Rust's shift toward ecosystem integration.

**Tags**: `#Rust`, `#Microsoft`, `#Programming Languages`, `#Software Engineering`, `#Industry News`

---

<a id="item-7"></a>
## [trynix.dev boots any Nix package in the browser via qemu-wasm](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 8.0/10

Farid Zakaria launched trynix.dev, a project he calls his "magnum opus" of Nix work, which uses qemu-wasm to run an x86_64 Linux virtual machine entirely inside the browser and boot any Nix package from the past 13 years. Packages are URL-addressable, so visiting a link such as https://trynix.dev/?pkg=python3%403.6.2 and clicking "Load" opens an interactive shell running Python 3.6.2 from 2017. He also released trynix-preview, a GitHub Action that comments a link on a pull request so reviewers can boot that PR's build in the browser with no servers involved. This makes reproducible software environments instantly shareable as plain URLs, which is significant for software archaeology, debugging old builds, and reviewing pull requests by actually booting them rather than reasoning about them statically. Because everything runs client-side in WebAssembly, it lowers the barrier to reproducing historical environments without installing Nix, QEMU, or any server infrastructure. The VM is powered by ktock/qemu-wasm, which translates QEMU translation blocks into WebAssembly modules and uses browser APIs like WebAssembly.Module and WebAssembly.Instance to execute them, since Wasm cannot transfer control to generated code in memory. The project covers Nix packages from the past 13 years and is URL-addressable, though running a full VM in the browser implies performance and resource constraints compared with native execution.

rss · Simon Willison · Sep 10, 23:44

**Background**: Nix is a purely functional package manager that builds every package in isolation with its exact dependencies specified, which makes builds reproducible and allows multiple versions of the same software to coexist. WebAssembly is a memory-safe, sandboxed low-level virtual machine format originally designed for near-native code execution in the browser, and it has since been used to run full Linux environments such as WebVM. qemu-wasm applies this by porting the QEMU emulator to WebAssembly, so a complete x86_64 Linux system can boot inside a browser tab.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ktock/qemu-wasm">GitHub - ktock/qemu-wasm: QEMU on browser · GitHub</a></li>
<li><a href="https://reproducible.nixos.org/">NixOS Reproducible Builds</a></li>
<li><a href="https://webassembly.org/">WebAssembly</a></li>

</ul>
</details>

**Tags**: `#Nix`, `#WebAssembly`, `#qemu`, `#reproducibility`, `#browser`

---

<a id="item-8"></a>
## [Shopify Returns to Native Mobile, Citing AI Coding Agents](https://simonwillison.net/2026/Sep/10/shopify-react-native/) ⭐️ 8.0/10

Shopify announced it is moving its mobile apps away from React Native and back to separate Swift (iOS) and Kotlin (Android) codebases, reversing its 2020 decision to consolidate on React Native. The company says AI coding agents can now handle enough implementation, translation, testing, and review work that maintaining two native platforms is no longer the deciding cost factor. This is a high-profile reversal from one of React Native's most visible enterprise adopters, and it signals that AI coding agents may be shifting the long-standing economics of cross-platform versus native development. If the reasoning holds, other large engineering organizations could reconsider their own cross-platform strategies. Shopify maintains three significant React Native libraries: react-native-skia, flash-list, and restyle; the first two are being handed to new maintainers, while restyle will be archived at the end of 2026 because it has a smaller user base. The company still credits React Native as a great platform during the six years it was used.

rss · Simon Willison · Sep 10, 21:11

**Background**: React Native is an open-source UI framework from Meta that lets developers build apps for both iOS and Android from a single JavaScript/React codebase. Native development instead requires separate codebases in Swift, Apple's language for iOS, and Kotlin, Google's preferred language for Android, which historically doubles the work of shipping features. Shopify originally switched to React Native in 2020 to avoid building the same features twice and to let developers work across the stack.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/React_Native">React Native - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Swift_(programming_language)">Swift (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kotlin_programming_language">Kotlin programming language</a></li>

</ul>
</details>

**Tags**: `#React Native`, `#Mobile Development`, `#AI Coding Agents`, `#Shopify`, `#Native Apps`

---

<a id="item-9"></a>
## [OpenAI Launches ChatGPT for Financial Services with GPT-6 Astra](https://openai.com/index/introducing-chatgpt-financial-services) ⭐️ 8.0/10

OpenAI introduced ChatGPT for Financial Services, a tailored ChatGPT Work experience that combines built-in financial data with the GPT-6 Astra model to help teams produce research, financial models, and customized client materials. The offering builds on ChatGPT Enterprise's security features, including SAML SSO, SCIM provisioning, and role-based access controls. This marks OpenAI's first major industry-specific vertical product for finance, a high-stakes sector where accuracy, data provenance, and compliance are critical. It could accelerate enterprise AI adoption across investment research, banking, and advisory workflows, pressuring competitors to offer similar domain-tuned offerings. The product includes datasets from Daloopa, PitchBook, and LSEG News covering earnings transcripts, financial statements, company fundamentals, and private companies. By default, a firm's business data is not used to train OpenAI's models, and data is encrypted at rest and in transit with configurable workspace retention.

rss · OpenAI News · Sep 10, 07:00

**Background**: ChatGPT is OpenAI's generative AI chatbot, originally released in November 2022, built on large language models. GPT-6 Astra is OpenAI's flagship model designed for complex reasoning, coding, computer use, and long multi-step professional workflows. Financial services firms have increasingly adopted such tools for research and due diligence, but specialized data integration and enterprise controls have been missing until now.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-financial-services/">Introducing ChatGPT for Financial Services | OpenAI</a></li>
<li><a href="https://www.unite.ai/openai-launches-chatgpt-for-financial-services-with-built-in-data/">OpenAI Launches ChatGPT for Financial Services With Built - In Data</a></li>
<li><a href="https://en.ain.ua/2026/09/04/openai-released-gpt-6-astra/">GPT - 6 Astra from OpenAI. What can the new AI model do?</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#ChatGPT`, `#Financial Services`, `#GPT-6`, `#Enterprise AI`

---

<a id="item-10"></a>
## [Datasette 1.0a39 and 0.65.4 Patch AI-Found Security Flaws](https://simonwillison.net/2026/Sep/11/datasette-security/) ⭐️ 7.0/10

Datasette released two security patch versions, 1.0a39 for the alpha series and 0.65.4 for the stable 0.65.x family, after an extensive audit conducted with Claude Fable 5.1, GPT-5.6, and GPT-6 Astra uncovered very subtle vulnerabilities. The audit followed issues reported by Sevban Dönmez, and Simon Willison and Alex Garcia spent nearly a week collaborating on and reviewing the fixes. Anyone running a Datasette instance on the public web, especially one that mixes public and private tables, should apply these patches immediately because the flaws could let users reach data they should not access. The release also signals that security audits by frontier AI models are becoming a standard part of open-source development workflows. The fixes target subtle bugs affecting instances that mix public and private tables, and the work was split so that one person wrote automated tests exposing each issue while the other implemented the fix, ensuring two humans plus multiple coding agents reviewed every change. Willison said security audits by frontier models will be incorporated into all future Datasette development work.

rss · Simon Willison · Sep 11, 03:27

**Background**: Datasette is an open-source tool for exploring, browsing, and publishing data, often used to serve SQLite databases on the web. Its permission system lets administrators mark some tables as public and others as private within the same database, a configuration that has been the source of previous SQL injection issues, including one fixed in 0.65.3 and 1.0a38 in August 2026. This new release continues that security hardening effort with additional fixes found through AI-assisted auditing.

<details><summary>References</summary>
<ul>
<li><a href="https://releaseport.com/r/simonw-datasette/0-65-3">Datasette 0.65.3 release notes — security patches & CVE fixes</a></li>
<li><a href="https://jasonvsthenoise.com/repowatch/2026-08-07-datasette-private-table-sql-injection/">Datasette closes a SQL injection path into private tables</a></li>
<li><a href="https://spbavarva.github.io/0day.digest/posts/datasette-sql-injection-fix/">Datasette SQL Injection Fix (1.0a38) | 0day.digest</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#security`, `#open-source`, `#vulnerability`, `#release`

---

<a id="item-11"></a>
## [Researcher Uses Codex and ChatGPT to Mine Genomes for Antimicrobials](https://openai.com/index/using-codex-chatgpt-to-search-for-new-antimicrobials) ⭐️ 7.0/10

César de la Fuente's lab is using OpenAI's Codex and ChatGPT to search both living and extinct genomes for new antimicrobial candidates to fight drug-resistant infections. The work is highlighted in an OpenAI case study describing how the lab applies AI coding and language tools to genomic data mining. Antimicrobial resistance is a growing global health threat, and traditional antibiotic discovery has largely stalled, so using AI to mine vast genomic datasets could dramatically accelerate the identification of new drug candidates. This case study illustrates how general-purpose AI tools like Codex and ChatGPT are moving from software tasks into real scientific discovery workflows. The approach combines genome mining — computationally scanning DNA sequences for genes that may encode antimicrobial compounds — with AI models that help write and run the analysis code. The OpenAI write-up is a promotional case study rather than a peer-reviewed technical paper, so specific hit rates, molecule counts, and validation results are not detailed.

rss · OpenAI News · Sep 10, 16:00

**Background**: Antimicrobial peptides (AMPs) are short protein-like molecules that can kill bacteria and other microbes, and they are seen as promising alternatives to conventional antibiotics. Machine learning has already been used to predict AMPs across the global microbiome — one 2024 study cataloged over 860,000 candidate peptides — and genome mining extends this idea to ancient or extinct DNA. Codex is OpenAI's code-generation model, originally derived from GPT-3 and now part of its agentic coding tools, while ChatGPT is its general conversational assistant.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cell.com/cell/fulltext/S0092-8674(24)00522-1">Discovery of antimicrobial peptides in the global microbiome ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(language_model)">OpenAI Codex (language model) - Wikipedia</a></li>
<li><a href="https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2019.02518/full">Frontiers | Diversity, Ecology, and Prevalence of Antimicrobials in...</a></li>

</ul>
</details>

**Tags**: `#AI for science`, `#drug discovery`, `#antimicrobial resistance`, `#genomics`, `#OpenAI`

---

<a id="item-12"></a>
## [OpenAI launches Data agent in ChatGPT Work for enterprise analytics](https://openai.com/index/put-data-to-work) ⭐️ 7.0/10

OpenAI announced a new Data agent inside ChatGPT Work that lets users connect their company data and build interactive dashboards using natural language. According to OpenAI's help documentation, the Data plugin can use connected company data and business context to analyze what changed, explain findings, and generate dashboards and reports that users can refine and publish through follow-up questions. This move pushes ChatGPT deeper into enterprise data analysis workflows, where it will compete with established BI tools and AI analytics platforms. If it works reliably, it could let non-technical employees query company data and build dashboards without SQL or dedicated BI expertise, potentially reshaping how businesses handle internal reporting. The Data agent works within ChatGPT Work and Codex, using connected company data and business context to answer questions and produce dashboards, with results refined and validated through conversational follow-ups. OpenAI's own in-house data agent reportedly uses GPT-5, Codex, and memory to reason over large datasets, though the public announcement itself is brief and lacks technical specifics such as supported data sources or pricing.

rss · OpenAI News · Sep 10, 15:00

**Background**: ChatGPT Work is OpenAI's offering aimed at business and enterprise users, extending the consumer ChatGPT product with workplace-focused capabilities. A 'data agent' refers to an AI system that can autonomously connect to data sources, run queries such as read-only SQL against a warehouse, and produce analyses or visualizations. Enterprise data analysis has become a major battleground for AI vendors, as companies look to automate reporting and extract insights from growing volumes of internal data.

<details><summary>References</summary>
<ul>
<li><a href="https://help.openai.com/en/articles/20001518">Using the Data plugin in ChatGPT Work and Codex</a></li>
<li><a href="https://www.xda-developers.com/openai-chatgpt-data-agent-announcement/">OpenAI reveals its new Data agent for ChatGPT Work to make ...</a></li>
<li><a href="https://openai.com/index/inside-our-in-house-data-agent/">Inside OpenAI’s in-house data agent</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#ChatGPT`, `#enterprise AI`, `#data analysis`, `#product announcement`

---

<a id="item-13"></a>
## [OpenAI and GSA Offer Free ChatGPT Licenses to U.S. Governments](https://openai.com/index/expanding-ai-access-us-government) ⭐️ 7.0/10

OpenAI announced a partnership with the U.S. General Services Administration (GSA) to offer eligible federal, state, local, and tribal government agencies $0 license fees, a 50% discount on usage, and expanded cyber defense support. This significantly lowers the cost barrier for public sector AI adoption across all levels of U.S. government, potentially accelerating the integration of AI tools into government workflows while strengthening cybersecurity defenses. The offer includes $0 license fees, 50% off usage costs, and enhanced cyber defense support, though specific eligibility criteria and the exact scope of cyber defense assistance were not detailed in the announcement.

rss · OpenAI News · Sep 10, 07:00

**Background**: The GSA is an independent U.S. government agency established in 1949 that manages basic functioning of federal agencies, including procurement and technology services. OpenAI's ChatGPT is a widely used AI chatbot, and governments have been increasingly evaluating AI tools for efficiency and cybersecurity, with some countries like Japan also considering similar adoption.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/General_Services_Administration">General Services Administration - Wikipedia</a></li>
<li><a href="https://www.gsa.gov/">Home | GSA</a></li>
<li><a href="https://www.viennatimes.com/technology/japan-considers-openai-chatgpt-government-cybersecurity/">Japan Considers Using OpenAI ’s ChatGPT for Government</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#government`, `#AI access`, `#cybersecurity`, `#public sector`

---

<a id="item-14"></a>
## [OpenAI launches GPT-Live-1 voice model in its API](https://news.google.com/rss/articles/CBMia0FVX3lxTE5iOG1jX2MydURESEhHYXluWGN1UXVoWTRPWEcxZmRaZkZNcnBTQ1VEazZ6V2dhSlFCdl9GX1lzWkZkVEo1LWtmc1lNOTRJVlJRTkRVN2gzLVFyUmtNeTViZlpnRVRyS1NOb3lB?oc=5) ⭐️ 7.0/10

OpenAI has introduced GPT-Live-1 in its API, a new model that brings natural, full-duplex voice conversations to developers building voice applications. According to OpenAI, it offers stronger instruction following, support for custom voices, and telephony integration. This release makes advanced conversational voice AI directly accessible to developers through a standard API, which could accelerate innovation in voice assistants, customer service bots, and accessibility tools. It also positions OpenAI against specialized voice AI providers like ElevenLabs and Google Cloud's text-to-speech services. GPT-Live-1 supports full-duplex conversations, meaning users and the AI can speak and listen simultaneously, similar to a natural phone call. It also adds telephony support, enabling integration with phone systems, and allows developers to use custom voices for their applications.

google_news · openai.com · Sep 10, 17:05

**Background**: Full-duplex voice means the AI can listen and speak at the same time, unlike traditional turn-based voice assistants that wait for the user to finish. OpenAI's API lets developers integrate AI models into their own apps and services, and this new voice model is part of a broader trend of making voice interfaces more natural and human-like. Competing services like Google Cloud Text-to-Speech and ElevenLabs also focus on lifelike AI voices, but GPT-Live-1 emphasizes real-time, conversational interaction.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-live-1-in-the-api/">Build more natural voice experiences with GPT‑Live‑1 in the... | OpenAI</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#voice AI`, `#API`, `#natural language processing`, `#developer tools`

---