from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models import Item, ItemCreate, ItemResponse
from typing import List

item_router = APIRouter()

@item_router.post("/items", response_model=ItemResponse)
async def create_item(item: ItemCreate, db: AsyncSession = Depends(get_db)):
    """Create a new item."""
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item

@item_router.get("/items", response_model=List[ItemResponse])
async def get_items(db: AsyncSession = Depends(get_db)):
    """Get all items."""
    result = await db.execute(select(Item))
    items = result.scalars().all()
    return items

@item_router.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int, db: AsyncSession = Depends(get_db)):
    """Get a specific item by ID."""
    result = await db.execute(select(Item).where(Item.id == item_id))
    item = result.scalar_one_or_none()
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return item