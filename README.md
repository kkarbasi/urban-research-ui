<p align="center">
  <img src="app/logo.svg" alt="Urban Research" width="420">
</p>

<p align="center">
  <strong>Interactive dashboard for real estate investment research.</strong>
</p>

---

A Streamlit dashboard that visualizes data from the [urban-research](https://github.com/kkarbasi/urban-research) package — population growth, job growth, wages, and unemployment for 370+ US metros and cities.

## Setup

```bash
git clone https://github.com/kkarbasi/urban-research-ui.git
cd urban-research-ui
uv sync

# Fetch data (only needed once)
uv run urban-research fetch census_population
uv run urban-research fetch bls_employment --skip-laus

# Launch dashboard
uv run python run.py
```

Open **http://localhost:8501**.

## Tabs

- **Rankings** — Rank metros by population growth, job growth, unemployment, or avg pay
- **Trends** — Compare up to 15 metros with line charts across any metric
- **City Profile** — All metrics for a single metro, charted over time
- **Data Explorer** — Full data table with filters + CSV download

## Dependencies

This dashboard uses the [`urban-research`](https://github.com/kkarbasi/urban-research) package for data fetching and storage. The package provides:
- CLI (`urban-research fetch`, `query`, `status`)
- Python API (`from urban_research import api`)
- SQLite storage with upsert semantics

## License

MIT
