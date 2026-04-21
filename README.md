<p align="center">
  <img src="app/logo.svg" alt="Urban Research" width="420">
</p>

<p align="center">
  <strong>Interactive dashboard for real estate investment research.</strong>
</p>

---

A Streamlit dashboard that visualizes data from the [cityscope](https://github.com/kkarbasi/cityscope) package — population growth, job growth, wages, and unemployment for 370+ US metros and cities.

## Setup

```bash
git clone https://github.com/kkarbasi/urban-research-ui.git
cd urban-research-ui
uv sync

# Fetch data (only needed once)
uv run cityscope fetch census_population
uv run cityscope fetch bls_employment --skip-laus

# Launch dashboard
uv run python run.py
```

Open **http://localhost:8501**.

## Tabs

- **Rankings** — Rank metros by population growth, job growth, unemployment, or avg pay
- **Trends** — Compare up to 15 metros with line charts across any metric
- **City Profile** — All metrics for a single metro, charted over time
- **Data Explorer** — Full data table with filters + CSV download
- **Address Lookup** — Enter any US address to see metro, city, and county stats side-by-side with a map pin and historical trend charts. Toggle **Auto-fetch missing** to pull data from Census/BLS on-the-fly for counties or smaller cities not in the default fetch.

## Dependencies

This dashboard uses the [`cityscope`](https://github.com/kkarbasi/cityscope) package for data fetching and storage, pulled directly from its GitHub repository (see `[tool.uv.sources]` in `pyproject.toml`). The package provides:
- CLI (`cityscope fetch`, `query`, `status`, `lookup`)
- Python API (`from cityscope import api` — `fetch`, `query`, `lookup`, `to_dataframe`, etc.)
- SQLite storage with upsert semantics

To pull the latest cityscope changes during development:

```bash
uv sync --upgrade-package cityscope
```

## License

MIT
