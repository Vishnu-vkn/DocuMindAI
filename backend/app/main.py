from fastapi import FastAPI
app = FastAPI(title="DocuMind AI API")

@app.get("/health")
def health_check() -> dict[str,str]:
    return {"status":"ok"}