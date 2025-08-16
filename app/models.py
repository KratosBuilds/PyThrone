# Define your data models here
from sqlalchemy import Column, Integer, String, Text
from pydantic import BaseModel
from app.database import Base

# Existing Quiz class (keeping for backward compatibility)
class Quiz:
    def __init__(self, id: int, question: str, answer: str):
        self.id = id
        self.question = question
        self.answer = answer

# SQLAlchemy database model for Item
class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)

# Pydantic models for API requests/responses
class ItemCreate(BaseModel):
    name: str
    description: str = None

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str = None
    
    class Config:
        from_attributes = True
