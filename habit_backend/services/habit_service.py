from typing import List

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import DuplicateKeyError

from habit_backend.models.habit import Habit

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.habit_db
habits_collection = db.habits


async def create_habit(habit: Habit) -> Habit:
    habit_dict = habit.model_dump(exclude_unset=True, by_alias=True)
    try:
        result = await habits_collection.insert_one(habit_dict)
        return Habit(**habit_dict, id=str(result.inserted_id))
    except DuplicateKeyError:
        return None


async def get_all_habits() -> List[Habit]:
    habits_cursor = habits_collection.find()
    habits = await habits_cursor.to_list(length=100)
    return [
        Habit(**{**habit, "_id": str(habit["_id"])}) for habit in habits
    ]


async def get_habits(user_id: str) -> Habit:
    habit_data = await habits_collection.find_one({"_id": user_id})
    if habit_data:
        return Habit(**habit_data, id=str(habit_data["_id"]))
    return None
