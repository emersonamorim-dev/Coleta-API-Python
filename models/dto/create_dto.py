from sqlmodel import Field, SQLModel
from typing import Optional
from decouble import config
from uuid import UUID

class CreateDTO(SQLModel, table=True):
    __tablename__: str = config('TABLE_DB')

    id: Optional[UUID] = Field(
        default=None,
        primary_key=True
    )

    type: str
    daily: str
    destiny: str
    time: int
    price: int
