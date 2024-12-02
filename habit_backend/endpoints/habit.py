from typing import List

from fastapi import APIRouter

from habit_backend.models.habit import Habit
from habit_backend.services.habit_service import get_all_habits, create_habit

router = APIRouter()


@router.post("/", response_model=Habit)
def create_habit_endpoint(habit: Habit):
    return create_habit(habit)


@router.get("/", response_model=List[Habit])
def get_all_habits_endpoint():
    habits = get_all_habits()
    return habits