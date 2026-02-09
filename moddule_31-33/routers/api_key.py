from fastapi import APIRouter, HTTPException, status, Depends
from auth.security import get_api_key

from online_recipe_book.routers.recipe import router

router = APIRouter()
@router.get("/")
def validate_key(api_key: str = Depends(get_api_key)):
    return {"message":"API Key is valid"}
