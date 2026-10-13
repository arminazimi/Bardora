# Global ecosystem strategy — 2026-10-12

## Purpose

This note turns the current open-source TOEFL iBT® test coaching skill into a staged global ecosystem strategy. It uses first-party sources and is product guidance, not legal advice. The project should obtain qualified trademark, copyright, privacy, consumer-protection, and tax review before operating a paid service internationally.

## Strategic thesis

Keep one **free, fully useful, vendor-neutral skill** as the public source of truth. Monetize the hosted service around it—compute, speech processing, secure sync, longitudinal analytics, collaboration, administration, and support—rather than withholding the basic coaching method. This preserves community trust, keeps adoption friction low, and gives the paid product defensible operational value.

Apache-2.0 permits free, internal, and commercial use subject to its terms, so a paid hosted product can coexist with the open repository; releases still need the license and applicable notices. [Apache Software Foundation licensing FAQ](https://www.apache.org/foundation/license-faq.html)

## Non-negotiable launch gates

1. **Adopt an independent brand before broad promotion.** ETS says its marks and translations/transliterations may not appear in a company, brand, product, domain, social username, website identifier, or advertising keyword. Use the independent brand prominently; use “TOEFL iBT® test” only as compatibility/informational text, with the required generic term, symbol, separation, and non-endorsement notice. Submit proposed public materials to ETS for review when required. [ETS trademark guidelines](https://www.ets.org/legal/trademarks.html)
2. **Ship only original learning content unless written permission is obtained.** ETS says all TOEFL materials are copyright-protected, reproduction requires a license, and ETS does not grant permission to post TOEFL materials on third-party websites. Do not copy or adapt passages, prompts, audio, transcripts, rubrics, answer keys, sample responses, directions, graphics, or recalled test content. Link to official sources and maintain provenance for every shipped item. [ETS TOEFL licensing policy](https://www.ets.org/legal/permissions/licensing.html), [ETS permissions policy](https://www.ets.org/legal/permissions.html)
3. **Never market an “official,” “ETS-approved,” or score-equivalent result.** Label AI feedback and estimated readiness as unofficial, publish uncertainty and known limitations, and reserve high-stakes claims for independently validated evidence.
4. **Decide the under-13 policy before accounts launch.** The lowest-risk initial scope is a general-audience service for users 13+ with a neutral age gate and no personal-data collection before the gate. If the product targets or knowingly collects personal data from children under 13, COPPA can require notice, verifiable parental consent, parent access/deletion controls, security, and limited retention. [FTC COPPA FAQ](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions)
5. **Minimize learner data by design.** Store derived progress signals by default, not raw answers or voice recordings; make audio retention explicit and time-limited; provide export and deletion. GDPR Article 5 requires personal data to be adequate, relevant, and limited to what is necessary. [EU GDPR, Article 5](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679)

## Product and distribution architecture

### Canonical free core

- Maintain one provider-neutral skill directory as the canonical implementation, with an independent name and stable task contracts.
- Conform to the open Agent Skills specification: one `SKILL.md`, valid `name` and `description`, focused `references/`, deterministic `scripts/`, reusable `assets/`, and progressive disclosure. Validate every release with `skills-ref`. [Agent Skills specification](https://agentskills.io/specification)
- Keep network access optional. The core should coach from user-provided or bundled original content without accounts, telemetry, or a hosted backend.
- Version task contracts, learner-state schema, evaluation fixtures, content packs, and platform adapters separately so improvements do not force a monolithic upgrade.

### Multi-platform packaging

- Build release artifacts from the same canonical files: a plain skill archive, platform-specific install instructions, and later an installable plugin. Do not maintain divergent copies by hand.
- Test discovery, activation, feedback boundaries, missing-input behavior, audio handling, and privacy behavior on every supported surface. OpenAI supports versioned skill bundles compatible with the open standard, while Anthropic notes that skills and their sharing scope differ across Claude surfaces; portability therefore needs tested adapters and a compatibility matrix, not a README claim. [OpenAI Skills API guide](https://developers.openai.com/api/docs/guides/tools-skills), [Anthropic Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- For ChatGPT/Codex distribution, package the skill as a plugin only when that reduces installation friction or adds controlled tools; OpenAI’s plugin format can bundle skills now and add an MCP server or UI later without changing the skill’s purpose. [OpenAI plugin architecture](https://developers.openai.com/plugins/concepts/plugins), [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins)

## Becoming a trusted learning authority

1. **Evidence before growth:** publish an original, versioned evaluation set for all 12 task types; run it across supported agents/models; report regressions, not only wins.
2. **Human calibration:** establish a blind review panel of qualified TOEFL educators. Measure agreement, false-positive/false-negative feedback patterns, and learner improvement over repeated attempts. Do not use educator review as a claim of ETS equivalence.
3. **Transparent content pipeline:** require source/provenance metadata, originality checks, pedagogical review, accessibility review, and an expiry/recheck date for every content pack.
4. **Learning outcomes:** track improvement in observable skills and completion of targeted revisions—not vanity metrics or invented score precision. Publish an annual methodology and limitations report.
5. **Global inclusion:** make explanations localizable while preserving English practice content; accept community translations through review; test low-bandwidth, keyboard-only, screen-reader, transcript-only, and no-audio paths.

## Community and governance

Before actively recruiting contributors, add `CODE_OF_CONDUCT.md`, `SUPPORT.md`, `SECURITY.md`, `ACCESSIBILITY.md`, issue/PR templates, maintainer roles, a decision log, and a lightweight governance document. GitHub’s community-health guidance specifically supports contribution guidelines, a code of conduct, support resources, accessibility reporting, licensing, and newcomer labels. [GitHub healthy-contribution guidance](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions)

Use three contribution lanes:

- **Content:** original exercises with provenance, answer rationale, difficulty tags, and review evidence.
- **Pedagogy/evaluation:** rubrics, failure cases, human-review studies, and accessibility audits.
- **Engineering/localization:** validators, adapters, installers, translations, privacy, and hosted services.

Create a public maintainer ladder—contributor, reviewer, module maintainer, steering maintainer—with conflict-of-interest disclosure. Keep roadmap decisions and acceptance criteria public. GitHub Discussions can host learner/educator feedback while Issues remain actionable engineering and content work.

## Sustainable monetization boundary

### Stage A — public-good adoption

- Free repository, installable releases, original starter content, local learner state, and all core coaching workflows.
- If regionally eligible, enable GitHub Sponsors for voluntary one-time and monthly support; GitHub says eligibility depends on residence/legal operation in a supported region, so confirm eligibility before making it a funding dependency. [GitHub Sponsors for contributors](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/about-github-sponsors-for-open-source-contributors), [repository sponsor button](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/displaying-a-sponsor-button-in-your-repository)

### Stage B — optional hosted Pro

Paid value may include managed accounts and sync, more speech-processing minutes, cross-device history, adaptive study plans, original full-length simulations, scheduled practice, richer analytics, priority compute, and support. Preserve a useful anonymous/local path and publish clear quotas before asking for payment.

Start with simple flat monthly/annual tiers and visible usage entitlements. Introduce usage-based billing only where costs genuinely scale, such as speech minutes or model inference, with hard spend caps and warnings; Stripe documents flat-rate, tiered, usage-based, and credit models, and warns that postpaid usage can accumulate significant charges. [Stripe recurring pricing models](https://docs.stripe.com/billing/subscriptions/metered-billing/thresholds)

### Stage C — educators and institutions

Offer classroom cohorts, assignment workflows, consent-aware dashboards, SSO, administrative controls, audit/export, service levels, and an API. Keep individual learner data private from sponsors and advertisers. Institutional contracts must not imply ETS endorsement.

### Stage D — ecosystem

Publish stable extension interfaces for independently reviewed content packs, localizations, analytics exporters, and institution integrations. Use a curated registry with provenance, license, compatibility, safety review, and revocation status. Third-party extensions should never inherit the project’s trust badge automatically.

## Release and security hygiene

- Require pull requests, passing tests, resolved reviews, and designated-owner approval for sensitive files; GitHub rulesets can require reviews, status checks, signed commits, and prevent unsafe direct changes. [GitHub ruleset options](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
- Publish `SECURITY.md`, enable private vulnerability reporting, and use private security advisories for coordinated fixes. Enable dependency graph, Dependabot, code scanning, secret scanning, and push protection as the implementation grows. [GitHub repository security quickstart](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository)
- Tag semantic releases, generate changelogs, freeze evaluation results, and publish checksums. Use immutable GitHub releases for stable artifacts; for executable/plugin bundles, add build provenance attestations and document verification. Attestations prove provenance, not that an artifact is safe. [GitHub releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases), [GitHub artifact attestations](https://docs.github.com/en/actions/concepts/security/artifact-attestations)
- Treat installed skills as software: review every bundled file, script, external fetch, permission, and dependency. Anthropic warns that malicious or compromised skills can misuse tools, access data, or exfiltrate information. [Anthropic skill security considerations](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#security-considerations)

## Recommended roadmap expansion

| Horizon | Outcome | Exit criteria |
|---|---|---|
| 0–3 months | Trustworthy independent v1 | Independent brand; IP/trademark review; human Writing review; public eval baseline; accessibility/security/community files; two-platform compatibility report; signed/tagged release. |
| 3–6 months | Global free adoption | One-command installs; original content-pack pipeline; localization framework; educator council; public documentation site; monthly quality report; community support/discussion workflow. |
| 6–12 months | Hosted beta | Privacy/age/tax/legal review; accountless free mode; opt-in sync; deletion/export; capped audio/inference usage; Pro pilot with transparent pricing; outcome and retention experiments. |
| 12–24 months | Educator and institutional product | Classroom workflows; consent-aware analytics; organization controls; API and SLAs; independent learning-impact study; security audit and incident exercises. |
| 24+ months | Governed ecosystem | Reviewed extension registry; certification criteria for content/reviewers; regional partnerships; transparent grants/sponsorships; durable multi-maintainer governance. |

## Success measures and stop conditions

Track: install-to-first-practice activation; completion and targeted-revision rates; 7/30-day learning retention; improvement on blinded original benchmark tasks; human/AI feedback agreement; accessibility task success; platform regression rate; contributor-review latency; security/privacy incidents; free-to-paid conversion; and paid churn.

Stop or delay monetization if the independent brand is unresolved, protected ETS material is present, score claims lack evidence, deletion/export is incomplete, minors/privacy scope is undefined, platform behavior is untested, or paid benefits would make the free core unusable. Popularity should be a consequence of trustworthy outcomes, not a substitute for them.
