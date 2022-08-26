from sqlalchemy.orm import Session

from . import models, schemas


def get_all_items_by_category(db: Session, category: str):
    return db.query(models.Item).filter(models.Item.category == category).all()


def get_items_by_id_in_category(db: Session, category: str, items_id: int):
    return db.query(models.Item).filter(models.Item.category == category, models.Item.id == items_id).first()


def get_item_by_id(db: Session, items_id: int):
    return db.query(models.Item).filter(models.Item.id == items_id).first()


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, item: schemas.ItemUpdate):
    db_item = db.query(models.Item).filter(models.Item.id == item.id).update({'name': item.name, 'price': item.price})
    db.commit()
    return db_item