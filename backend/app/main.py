from fastapi import FastAPI

app = FastAPI(
    title="CareerPilot AI",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to CareerPilot AI 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }