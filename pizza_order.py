from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Dict
from uuid import uuid4

app = FastAPI()

# Sample pizza menu data
pizza_menu = [
    {
        "id": 1,
        "name": "Margherita",
        "size": "Medium",
        "price": 8.99,
        "toppings": ["tomato sauce", "mozzarella", "basil"]
    },
    {
        "id": 2,
        "name": "Pepperoni",
        "size": "Medium",
        "price": 9.99,
        "toppings": ["tomato sauce", "mozzarella", "pepperoni"]
    },
    {
        "id": 3,
        "name": "Vegetarian",
        "size": "Medium",
        "price": 10.99,
        "toppings": ["tomato sauce", "mozzarella", "bell peppers", "onions", "mushrooms"]
    },
    {
        "id": 4,
        "name": "Hawaiian",
        "size": "Medium",
        "price": 11.99,
        "toppings": ["tomato sauce", "mozzarella", "ham", "pineapple"]
    }
]

pizza_menu_by_name = {pizza["name"].lower(): pizza for pizza in pizza_menu}
pizza_menu_by_id = {pizza["id"]: pizza for pizza in pizza_menu}

class OrderItem(BaseModel):
    id: int
    quantity: int

class Order(BaseModel):
    items: List[OrderItem]
@app.get("/")
def read_root():
    return {"Welcome": "Pizza"}
@app.get("/menu")
async def get_pizza(name: str = Query(..., description="Name of the pizza")):
    pizza = pizza_menu_by_name.get(name.lower())
    if not pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")
    return pizza

@app.post("/order")
async def create_order(order: Order):
    total_price = 0
    for item in order.items:
        pizza = pizza_menu_by_id.get(item.id)
        if not pizza:
            raise HTTPException(status_code=404, detail=f"Pizza with id {item.id} not found")
        total_price += pizza["price"] * item.quantity
    
    order_id = str(uuid4())[:8]  # Using first 8 characters of UUID for a shorter order ID
    return {"order_id": order_id, "price": round(total_price, 2)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)