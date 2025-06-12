from pydantic import BaseModel
from typing import List, Optional

class DishCreate(BaseModel):
    name: str
    quantity: int
    price: float
    observations: Optional[str] = None

class DishResponse(DishCreate):
    id: int

    class Config:
        orm_mode = True