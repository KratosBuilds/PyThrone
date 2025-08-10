from fastapi import FastAPI
from app.routes import quiz_router

app = FastAPI(title="PyThrone API")

app.include_router(quiz_router)

@app.get("/")
def root():
    return {"message": "Welcome to PyThrone"}