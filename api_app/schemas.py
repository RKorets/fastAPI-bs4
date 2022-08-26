from pydantic import BaseModel


class ItemBase(BaseModel):

    id: int
    category: str
    name: str
    price: str

    class Config:
        orm_mode = True


class ItemName(BaseModel):

    name: str

    class Config:
        orm_mode = True


class ItemPrice(BaseModel):

    price: str

    class Config:
        orm_mode = True


class ItemCreate(BaseModel):
    name: str
    price: str
    category: str


class ItemUpdate(BaseModel):
    id: int
    name: str
    price: str


class Item(ItemCreate):
    id: int

    class Config:
        orm_mode = True
#
#
# class UserBase(BaseModel):
#     email: str
#
#
# class UserCreate(UserBase):
#     password: str
#
#
# class User(UserBase):
#     id: int
#     is_active: bool
#     items: list[Item] = []
#
#     class Config:
#         orm_mode = True
#
#
# class CustomUser(UserBase):
#     id: int
#     is_active: bool
#     hashed_password: str
#
#     class Config:
#         orm_mode = True
