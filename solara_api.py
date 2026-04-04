from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from nvda_pipeline import run_nvda_pipeline

app = FastAPI(title="Solara API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "solara-api"}


@app.get("/nvda-analysis")
def nvda_analysis():
    try:
        return run_nvda_pipeline()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"NVDA analysis failed: {exc}") from exc
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/asset-analysis")
def perform_asset_analysis():
    # Logic for asset analysis
    return {"message": "Asset analysis performed"}

@app.get("/portfolio-optimization")
def optimize_portfolio():
    # Logic for portfolio optimization
    return {"message": "Portfolio optimization completed"}

@app.get("/market-intelligence")
def market_intelligence():
    # Logic for market intelligence
    return {"message": "Market intelligence data provided"}

@app.post("/decision-logs")
def log_decision(data: dict):
    # Logic for logging decisions
    return {"message": "Decision logged", "data": data}
