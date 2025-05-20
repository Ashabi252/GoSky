from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Product
import database
import models
import crud
from typing import Optional

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

from pydantic import BaseModel
from datetime import datetime



class ProductResponse(BaseModel):
    id: int
    created_at: datetime
    name: str
    category: str
    price: float



@app.get("/products/", response_model=list[ProductResponse])
def read_products(db: Session = Depends(get_db),skip: Optional[int]=0,limit:Optional[int] = None,category: Optional[str]= None):
    return crud.get_all_products(db, skip, limit,category)
