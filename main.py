from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(title="PacketLab — Computer Networks Protocol Visualizer", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok", "mode": "educational simulation"}

@app.get("/")
def home():
    return FileResponse(BASE_DIR / "templates" / "index.html")
