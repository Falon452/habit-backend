from typing import Optional

from pydantic import BaseModel, Field

class Habit(BaseModel):
    id: Optional[str] = Field(
        default=None, description="MongoDB document ObjectID", alias="_id"
    )
    name: str
    number_of_days: int
    last_increase_date_time: str