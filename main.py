from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "SifraOS backend is live!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "SifraOS backend"}
