from fastapi import FastAPI

from habit_backend.endpoints import habit

app = FastAPI()

app.include_router(habit.router, prefix="/habits", tags=["Habits"])

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI library!"}