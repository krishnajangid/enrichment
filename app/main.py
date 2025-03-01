from fastapi import FastAPI

from app.api import enrichment

app = FastAPI()

app.include_router(enrichment.router)
