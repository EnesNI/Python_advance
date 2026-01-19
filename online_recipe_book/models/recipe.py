 from pydantic import BaseModel
 from typing import Optional

class RecipeBase (BaseModel):
    name: str
    description: Optional [str] = None
    ingredients: str
    instructions: str
    cuisine: str
    difficulty: str
    category_id: Optional [int] = None

class RecipeCreate(RecipeBase): new
    pass

class Recipe (RecipeBase): new*
    id: int