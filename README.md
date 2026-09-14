# Manabitan wiki

Documentation and homepage for [Manabitan](https://manabi.io/manabitan/).

Manabitan is a Yomitan fork with rewritten dictionary storage and query engines plus user-facing improvements around dictionary management and Anki setup. [Why use Manabitan?](https://manabi.io/manabitan/why-manabitan/) describes the product differences. [Why Manabitan is a fork](https://manabi.io/manabitan/about-manabitan/) separately explains the upstream relationship, implementation scope, migration responsibility, and why the fork uses the Manabitan name.

Yomitan's primary maintainers have supported releasing this work as a separate fork, offered guidance, and reviewed our release preparations. Manabitan is maintained and released independently. It remains free and open source.

## Working on the documentation

Use Python 3.12. Create a virtual environment, then run:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/prepare-assets.py
python -m mkdocs serve
```

Before submitting a change:

```sh
python -m unittest discover -s tests
python -m mkdocs build --strict
python scripts/check-site.py site
```

The asset preparation step fetches the real Manabitan logo from a pinned extension revision and checks its Git blob hash. It also prepares the PDF viewer's introduction. Do not copy or rename Yomitan artwork as Manabitan artwork. See `AUDIT_STATUS.md` for source provenance and checks that require released packages or production access.

## Deployment

Production is owned by `lake-of-fire/manabi`, not this repository. Its conditional wiki workflow builds these sources and publishes static files to the existing Manabi server. Nginx serves them beneath `/manabitan/`; there is no dedicated wiki container, Pages site, or Worker. Wiki CI builds and validates only.

Do not reintroduce `gh-deploy`, a CNAME, or a Cloudflare Pages/Workers deployment here. See the companion Manabi deployment documentation for first-time host setup, forwarding rules, and rollback.

## Attribution and licenses

This site is adapted from [Yomitan Wiki](https://github.com/yomidevs/yomitan-wiki). Manabitan is based on Yomitan, which continues Yomichan. See [Credits](docs/credits.md).

Website source retains [GPL-3.0](LICENSE-GPL-3.0); documentation content in `docs/*.md` retains [CC BY 4.0](LICENSE-CC-BY-4.0). The bundled PDF.js viewer retains its Apache-2.0 and third-party notices. Changes in this fork include Manabitan-specific documentation, branding, and deployment. These licenses do not replace licenses on dictionaries or linked third-party projects.
