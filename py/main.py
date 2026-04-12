from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gunicorn.app.base import BaseApplication
from log import LOGGING_CONFIG
from routes.ingestion import router as ingestion_router

app = FastAPI(
    title="Intention brain",
    description="Asynchronous API provider for Intention",
    middleware=[
        
    ],
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

class GunicornApp(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        for key, value in self.options.items():
            if key in self.cfg.settings:
                self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

if __name__ == "__main__":
    options = {
        "bind": "0.0.0.0:8000",
        "workers": 2,
        "worker_class": "uvicorn.workers.UvicornWorker",
        "logconfig_dict": LOGGING_CONFIG,
    }

    GunicornApp(app, options).run()