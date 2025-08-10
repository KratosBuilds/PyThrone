from fastapi import APIRouter

quiz_router = APIRouter()

@quiz_router.get("/quiz")
def get_quiz():
    return {"quiz": "PyThrone sample quiz data"}