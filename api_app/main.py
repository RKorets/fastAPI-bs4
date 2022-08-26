from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

favicon_path = 'favicon.ico'


@app.get('/favicon.ico')
async def favicon():
    return FileResponse(favicon_path)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/items/", response_model=schemas.Item)
def create_item_for_site(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@app.get("/items/{category}", response_model=list[schemas.ItemBase])
def read_items_by_category(category: str, db: Session = Depends(get_db)):
    items = crud.get_all_items_by_category(db, category)
    if items:
        return items
    else:
        raise HTTPException(status_code=404, detail="Items category empty")


@app.get("/items/{category}/{item_id}", response_model=schemas.ItemBase)
def read_item_by_id_in_category(category: str, item_id: int, db: Session = Depends(get_db)):
    item = crud.get_items_by_id_in_category(db, category, item_id)
    if item:
        return item
    else:
        raise HTTPException(status_code=404, detail="Item in this category empty")


@app.get("/items/{category}/{item_id}/name", response_model=schemas.ItemName)
def read_item_name_by_id_in_category(category: str, item_id: int, db: Session = Depends(get_db)):
    item = crud.get_items_by_id_in_category(db, category, item_id)
    if item:
        return item
    else:
        raise HTTPException(status_code=404, detail="Item name in this category empty")


@app.get("/items/{category}/{item_id}/price", response_model=schemas.ItemPrice)
def read_item_price_by_id_in_category(category: str, item_id: int, db: Session = Depends(get_db)):
    item = crud.get_items_by_id_in_category(db, category, item_id)
    if item:
        return item
    else:
        raise HTTPException(status_code=404, detail="Item name in this category empty")


@app.delete("/items/{item_id}/delete")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"ok": True}


@app.put("/items/{item_id}/put")
def put_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    get_item = crud.get_item_by_id(db, item_id)
    if not get_item:
        raise HTTPException(status_code=404, detail="Item not found")
    crud.update_item(db=db, item=item)
    return {'update': True}