from sqlalchemy.orm import Session
from models import Product
from typing import Optional


def get_all_products(db: Session, skip: int = 0, limit: Optional[int] = None, category: Optional[str] = None):
    get_query = db.query(Product).order_by(Product.created_at.desc())
    
    if category:
        get_query = get_query.filter(Product.category == category)
    
    return get_query.offset(skip).limit(limit).all()
