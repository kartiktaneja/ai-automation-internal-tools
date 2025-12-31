# Operations Insight Generator

This tool analyzes operational issue data and produces a short
human-readable report.

## What it does
- Reads issue records from CSV
- Aggregates issue trends
- Generates summary insights and recommendations

## Why it exists
Operations and support teams often have data but lack clear summaries.
This tool demonstrates how automation and AI-style reasoning can help
interpret operational signals.

## How to run
1. Update `input/issues.csv`
2. Run `python ops_insight_generator.py`
3. View results in `output/ops_report.md`

## Notes
The insight layer is designed to support AI-generated summaries
without changing the automation pipeline.
