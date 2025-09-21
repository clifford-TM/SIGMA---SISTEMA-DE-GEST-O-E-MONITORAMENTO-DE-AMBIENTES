from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="SIGMA API")

BASE_DIR = Path(__file__).resolve().parent
PUBLIC = BASE_DIR / "public"

# Servir arquivos estáticos (HTML/CSS/JS/imagens) em /static
app.mount("/static", StaticFiles(directory=str(PUBLIC), html=True), name="static")

#comentário para testar deploy
@app.get("/", response_class=HTMLResponse)
def root():
    index = PUBLIC / "index.html"
    if index.exists():
        return index.read_text(encoding="utf-8")
    return "<h1>SIGMA</h1><p>Backend up. Acesse /static/ para ver os HTMLs.</p>"

@app.get("/health")
def health():
    return {"status": "ok"}
