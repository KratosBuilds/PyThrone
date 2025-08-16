from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes import quiz_router
from app.item_routes import item_router
from app.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database on startup
    await init_db()
    yield

app = FastAPI(title="PyThrone API", lifespan=lifespan)

app.include_router(quiz_router)
app.include_router(item_router)

@app.get("/")
def root():
    return {"message": "Welcome to PyThrone"}