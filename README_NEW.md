# Solara AI

Solara is a personal financial AI system designed to analyze markets, generate signals, and produce actionable investment decisions.

## Problem

Most personal finance tools are either:
- Dashboards with no intelligence
- AI chat tools with no real data integration

Solara bridges that gap by combining:
- Real market data
- AI-driven interpretation
- Structured decision output

## Current Working Slice (NVDA)

This repository includes a working end-to-end pipeline:

1. Fetch real NVDA stock data using yfinance
2. Generate a sentiment score using TextBlob
3. Compute a conviction score (0–10)
4. Output a real trade decision (BUY / SELL / HOLD)

Run it:

```bash
pip install -r requirements.txt
python nvda_pipeline.py
```

Example output:

```json
{
  "ticker": "NVDA",
  "price_trend": 0.12,
  "sentiment": 0.5,
  "conviction_score": 7.3,
  "decision": "BUY"
}
```

## Local-Only Usage

This project is intended for local use only.
