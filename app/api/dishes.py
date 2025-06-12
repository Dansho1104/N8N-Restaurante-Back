from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import DishCreate, DishResponse

router = APIRouter()

# In-memory storage for dishes
dishes_db = []

@router.post("/dishes/", response_model=DishResponse)
async def create_dish(dish: DishCreate):
    dish_id = len(dishes_db) + 1
    new_dish = {**dish.dict(), "id": dish_id}
    dishes_db.append(new_dish)
    return new_dish

@router.get("/dishes/", response_model=List[DishResponse])
async def get_dishes():
    return dishes_db

@router.get("/dishes/{dish_id}", response_model=DishResponse)
async def get_dish(dish_id: int):
    for dish in dishes_db:
        if dish["id"] == dish_id:
            return dish
    raise HTTPException(status_code=404, detail="Dish not found")