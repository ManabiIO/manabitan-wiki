# Manabitan documentation audit

Source baseline: wiki `dab60309bae27be9d64f506f2e431d9de146003d`; extension `d3fc6795ccce4ba9b293c336898f3dcb32338128`. This records source changes, not a claim that production was deployed or every browser/package was tested.

## Addressed in this documentation change

- Canonical `/manabitan/` root, prefix-aware navigation, PDF links, logo, social cards, favicon, and a true documentation edit destination.
- Removal of Pages/Workers deployment configuration; Manabi owns conditional static publication through its existing Nginx service.
- Separate user-facing “Why use Manabitan?” material from the project-governance explanation of why Manabitan is a fork. The homepage leads with product improvements and keeps the fork/upstream explanation as a separate section.
- Direct fork explanation, independent maintenance, precise maintainer guidance/release-preparation wording, migration responsibility, open-source lineage, and measured-versus-expected performance distinction.
- Separate Yomitan migration guide, retained Yomichan helper history, and no promise of Dexie JSON / SQLite backup interchange.
- Actual backup format and retained legacy filename prefix; settings, source dictionary packages, and whole-database backups are distinct. Original packages remain the recovery path until version-specific restore coverage is established.
- Explicit unpacked/signed/temporary installation distinctions, no invented stable channel or marketplace listing, and a qualified mobile/device matrix.
- MDX, dictionary management and schedules, built-in themes, recall blur, and current controls documented with build-specific limits.
- Corrected the earlier “Anki note-type installation” wording. Manabitan does not install Kiku, Lapis, Senren, or Crop Theft Vocab. It recognizes an existing selected Anki model and automatically maps its fields. Explicit presets cover Kiku, Lapis, Senren/`Senren 洗練`, and Crop Theft Vocab, while other models receive best-effort alias/name mapping and preservation of same-named existing fields where possible.
- Real third-party names restored. TTS points to upstream #864. MeCab and Forvo remain documented with their real upstream tools and the Manabitan-specific compatibility steps/status instead of being deleted.
- Storage troubleshooting no longer assumes IndexedDB only or recommends destructive reset before backups.
- Privacy describes network requests, optional integrations, normal network metadata, diagnostics, alarms, Chromium offscreen permission, and the external media shown by the wiki itself.
- Support goes to the Manabi Discord while Issues are disabled. The wiki has its own contribution instructions.
- Useful screenshots and videos are retained as workflow examples. The page clearly labels that some were inherited from Yomitan documentation or show earlier UI instead of pretending they capture the exact current release. The site uses system fonts and no remote Google Font. The YouTube demonstration uses `youtube-nocookie.com` and lazy loading; the GitHub-hosted Anki example is retained with controls.
- The PDF introduction is generated from reviewable plaintext with Manabitan metadata. The vendor viewer is preserved; preparation changes only its title/favicon and sample document. Updates require an explicit version and checksum, and retain included licenses/notices.
- Strict MkDocs CI plus rendered HTML/CSS/anchor/search/sitemap checks under the real prefix; direct dependency pins, monthly dependency PRs, and separate external-link checks.

## Qualification that still requires outside access or a released build

- Merge the wiki changes before Manabi's workflow resolves them; configure the documented SSH host/user/known-host credentials and writable static parent directory. Verify the public route after the one-time Nginx/HAProxy update. Remove or repoint any external Cloudflare Worker/Pages rule that intercepts the path before the origin. Source changes cannot change that dashboard rule.
- Update both repositories' About homepage/description in GitHub administration. The connector used for this work does not provide that settings mutation. Keep Issues disabled with the documented Discord route, or enable them deliberately and then change the links.
- Confirm the release artifacts, signing, restart persistence, and update feed before advertising a persistent Firefox channel or platform support. Test mobile browsers and e-readers on their actual devices.
- Qualify old/new settings imports, full collection restoration including external resources, custom CSS/templates, MeCab registrations, external API integrations, Forvo/local-audio integrations, and AnkiDroid with explicit versions. Documentation does not substitute for those tests.
- Review automatic Anki field mappings against the exact versions of community note types users install; presets are covered by focused source tests, but third-party note types can change their schemas independently.
- Replace or supplement inherited/earlier screenshots and videos as current Manabitan release captures become available. Until then, preserve the useful workflow media with explicit provenance/status captions.
- Establish comparable-device benchmarks before publishing a speed ratio. Battery improvements remain an expectation, not a measured claim.

The upstream maintainer relationship wording comes from the Manabitan maintainer's account of those discussions. It is not presented as a formal endorsement, source-code audit, or guarantee of Manabitan releases.

## Reproduction

See README for local/CI commands. `scripts/asset-sources.json` pins exact logo and language-source bytes. The preparation step verifies Git blob hashes. The deployment bundle records the resolved Python package inventory; direct dependency pins alone are not a complete transitive lock.

The existing PDF.js distribution is inherited from the baseline above. Do not invent a release version for it: inspect the bundled build metadata and upstream security history before the next vendor update. `scripts/update-pdfjs.py --version X.Y.Z --sha256 <verified-sha256>` records the next reviewed distribution in `scripts/pdfjs-source.json`.
