from pydentic import BaseModel


class Category Base(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(BaseModel):
    id: int
    name: str

Class category(CategoryBase):
        id: int
