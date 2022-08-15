from datetime import datetime
import enum

from pydantic import BaseModel


class Color(enum.Enum):
    NONE = 0
    RED = 1
    BLUE = 2
    GREEN = 3


class Event(BaseModel):
    title: str
    description: str = ''
    start_date: datetime
    end_date: datetime
    color: Color = Color.NONE
