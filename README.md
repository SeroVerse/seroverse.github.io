# SeroVerse (`seroverse.github.io`)

Main landing portal and canonical Zensical theme source of truth for the **SeroVerse** computational ecosystem:

- **[SeroVerse Home](https://seroverse.github.io/)** — Ecosystem overview, architecture, and unified quickstarts
- **[SeroGen](https://seroverse.github.io/SeroGen/)** — Zero-copy SoA genomic engine, single-pass bacterial & prophage ORF caller, 1D-CNN role classifier, and ACP-DP locus segmenter
- **[KBank](https://seroverse.github.io/KBank/)** — Neuro-symbolic bacterial glycan database, bipartite gene-to-glycan aligner, and Relational MPNN structure predictor
- **[SeroEpi](https://seroverse.github.io/SeroEpi/)** — Bayesian hierarchical sero-epidemiological modelling, LOSO-validated vaccine formulation, and interactive PyShiny web application

## Unified Theme Synchronization

Canonical theme components live in this repository:

- `docs/stylesheets/extra.css` — Shared CSS variables (`--sv-*`), per-pillar palettes (`seroverse`, `serogen`, `kbank`, `seroepi`), glassmorphic hero banner, 3-pillar cards, 16:9 Marimo slide deck frames, and PyShiny app embeds
- `docs/overrides/main.html` — Shared top Ecosystem Switcher bar and multi-column SeroVerse footer

To propagate the canonical theme to the sibling repositories (`../SeroGen`, `../KBank`, `../SeroEpi`):

```bash
uv run python scripts/sync_theme.py
```

## Local Development

```bash
uv run zensical serve
```
