from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field
from sqlmodel import select


class Game(SQLModel, table=True):
    #Optional is a optional number in the database because is a primary key
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    category: str
    year: int
    console: str
    rate: int
    date: datetime = Field(default_factory=datetime.now)


Mario = Game(name="Mario Bros", category="Adventure", year=1982, console="SNES", rate=9)

print(select(Game))
