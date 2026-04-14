from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.ingestion import router as ingestion_router
import uvicorn

app = FastAPI(
    title="Intention brain",
    description="Asynchronous API provider for Intention",
    docs_url="/docx"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingestion_router)

@app.get('/')
def root():
    return {
        "title": "Intention brain",
        "description": "Asynchronous API provider for Intention",
        "docs_url": "/docx"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    