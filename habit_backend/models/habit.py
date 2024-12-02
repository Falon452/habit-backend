from datetime import datetime

from pydantic import BaseModel

class Habit(BaseModel):
    id: int
    name: str
    number_of_days: int
    last_increase_date_time: datetime