from typing import List

from fastapi import APIRouter, HTTPException

from habit_backend.models.habit import Habit
from habit_backend.services.habit_service import get_all_habits, create_habit

router = APIRouter()


@router.post("/", response_model=Habit)
async def create_habit_endpoint(habit: Habit):
    created_habit = await create_habit(habit)
    if created_habit is None:
        # Raise a 409 Conflict if the habit already exists
        raise HTTPException(
            status_code=409, detail="Habit with the same key already exists"
        )
    return created_habit


@router.get("/", response_model=List[Habit])
async def get_all_habits_endpoint():
    return await get_all_habits()