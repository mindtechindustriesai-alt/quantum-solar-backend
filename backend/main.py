import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import uvicorn

# Load environment variables
load_dotenv()

# ============================================================
# QUANTUM BADGE DATA
# ============================================================
QUANTUM_BADGE = {
    "chsh_s": 2.76,
    "classical_limit": 2.0,
    "quantum_max": 2.828,
    "percent_above_classical": 38.0,
    "correlation": 0.984,
    "patent": "SA 2026/05142",
    "verification_date": "2026-06-25",
    "ibm_job_id": "d8uhvl4bp3hs738628cg",
    "ibm_processor": "IBM Kingston (156 qubits)",
    "text": "CHSH S=2.76 · 38% above classical"
}

# ============================================================
# FASTAPI APP
# ============================================================
app = FastAPI(
    title="Quantum Solar Backend",
    description="Quantum-enhanced solar forecasting, optimization, and materials discovery",
    version="1.0.0",
    docs_url="/docs"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# ============================================================
# ROOT ENDPOINT
# ============================================================
@app.get("/")
async def root():
    return {
        "service": "Quantum Solar Backend",
        "version": "1.0.0",
        "status": "operational",
        "quantum_badge": QUANTUM_BADGE["text"],
        "patent": QUANTUM_BADGE["patent"],
        "ibm_job_id": QUANTUM_BADGE["ibm_job_id"],
        "endpoints": [
            "/health",
            "/api/quantum/status",
            "/api/solar/forecast",
            "/api/solar/optimize",
            "/api/solar/singlet-fission",
            "/api/solar/irradiance",
            "/api/solar/greenhouse"
        ]
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/api/quantum/status")
async def quantum_status():
    return QUANTUM_BADGE

# ============================================================
# SOLAR ENDPOINTS
# ============================================================
from backend.api.routes.solar import router as solar_router
app.include_router(solar_router, prefix="/api/solar", tags=["Solar"])

# ============================================================
# RUN
# ============================================================
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=False
    )
