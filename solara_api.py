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
