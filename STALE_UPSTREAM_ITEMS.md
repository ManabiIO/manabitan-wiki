# Stale Upstream Items To Evaluate

This fork was mechanically rebranded from the Yomitan wiki. The following inherited items should be reviewed before treating the site as final Manabitan documentation.

- Browser marketplace links are currently routed to GitHub Releases. Replace them with Chrome Web Store, Firefox Add-ons, and Edge Add-ons listings when Manabitan-specific listings exist.
- Screenshots and homepage imagery under `docs/assets/ss/` and `overrides/assets/` may still show Yomitan UI or old branding. Replace with Manabitan screenshots after release builds are final.
- The embedded homepage demo video is inherited from upstream and may show Yomitan behavior or branding.
- Dictionary ecosystem links with `yomitan` in the repository name are intentionally left as upstream compatible resources. Decide later whether any should be forked or mirrored under ManabiIO.
- Yomichan migration instructions are inherited and should be validated against Manabitan import/settings compatibility.
- Mobile support notes for Android Firefox, Edge, and Elixir are inherited and should be verified against Manabitan packages.
- PDF viewer URLs were rebranded to `/manabitan-pdf-viewer/`. Confirm the extension points users at the new path, or add redirects if older builds still point to `/yomitan-pdf-viewer/`.
- Export filename examples now use `manabitan-dictionaries-*`. Confirm the app uses the same naming before release.
- Anki, AnkiDroid, AnkiConnectAndroid, local-audio, and EPWING/Yomitan Import compatibility claims are inherited from upstream and should be smoke-tested against Manabitan.
