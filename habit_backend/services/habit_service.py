from typing import List

from habit_backend.models.habit import Habit

fake_db = {}


def create_habit(habit: Habit) -> Habit:
    db_id = len(fake_db) + 1
    new_user = Habit(id=db_id, name=habit.name, number_of_days=habit.number_of_days,
                     last_increase_date_time=habit.last_increase_date_time)
    fake_db[db_id] = new_user
    return new_user


def get_habits(user_id: int) -> Habit:
    return fake_db.get(user_id)


def get_all_habits() -> List[Habit]:
    return list(fake_db.values())
