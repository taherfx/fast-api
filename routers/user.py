from fastapi import APIRouter, status, Depends
from database import getdb
from sqlalchemy.orm import Session
from typing import List
import schemas
from repository import user

router = APIRouter(
    prefix= "/user",
    tags=["Users"]
)

@router.get("/",response_model=List[schemas.Showuser])
def get_all(db: Session = Depends(getdb)):
    return user.get_all(db)

@router.post("/", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.Showuser)
def create(request: schemas.User, db: Session = Depends(getdb)):
    return user.insert_user(request, db)

@router.get("/{id}",response_model=schemas.Showuser)
def showUser(id:int, db : Session = Depends(getdb)):
    return user.get_one(id, db)