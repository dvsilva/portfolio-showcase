# Danilo Valente — Portfolio Showcase

A self-contained, responsive portfolio landing page built with semantic HTML, CSS, and progressive-enhancement JavaScript. It is intentionally dependency-light so it can be served from any static host.

## Run locally

From this directory:

```powershell
python -m http.server 4173
```

Open <http://127.0.0.1:4173> and check desktop and mobile widths. Stop the server with `Ctrl+C`.

## Verify

```powershell
python -m unittest discover -s tests -v
```

The tests check the required semantic sections, accessibility markers, progressive-enhancement controls, and the absence of credential-like content.

## Editable starter content

This first factory pass uses representative portfolio copy. Replace the following before public launch:

- `hello@danilovalente.dev` in `index.html`;
- the LinkedIn URL in `index.html`;
- project descriptions and links when final case studies are available;
- the footer year if the page is reused in a later year.

No backend contact form or analytics is included in this iteration. The page is safe to publish as a static artifact, but the placeholder links should be reviewed first.
