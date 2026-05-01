# Replication Plan

## Purpose

This document explains how another reader should reproduce the research workflow once the dataset and models are completed.

## Environment Setup

```bash
git clone https://github.com/hitesh206-ui/India-em-lbo-research.git
cd India-em-lbo-research
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
pytest
```

## Research Workflow

1. Collect public deal data in `data/raw/india_buyout_deals_template.csv`.
2. Collect regulatory events in `data/raw/regulatory_timeline_template.csv`.
3. Clean and validate datasets using `src/india_em_lbo/data_cleaning.py`.
4. Compute LBO metrics using `src/india_em_lbo/lbo_metrics.py`.
5. Compute regulatory-friction scores using `src/india_em_lbo/regulatory_scoring.py`.
6. Generate charts and tables into `outputs/`.
7. Use outputs in the working paper.

## Data Integrity Rules

- Every deal observation must have a public source.
- Avoid confidential data unless it is explicitly approved for public release.
- Prefer original regulatory sources over media summaries.
- Document assumptions, conversions, currency rates, and estimation methods.

## Reproducibility Target

A future reader should be able to clone the repository, run tests, inspect the templates, reproduce the main charts, and understand the assumptions behind the India-adapted LBO model.
