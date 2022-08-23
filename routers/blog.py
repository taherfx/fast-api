from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from typing import List
import schemas
from database import getdb
from repository import blog
from oauth2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

@router.get("/", response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(getdb), currentUser : schemas.User = Depends(get_current_user)):
    return blog.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def index(request: schemas.Blog, db: Session = Depends(getdb), currentUser : schemas.User = Depends(get_current_user)):
    return blog.insert_blog(request, db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def getBlog(id: int, response : Response, db : Session = Depends(getdb), currentUser : schemas.User = Depends(get_current_user)):
    return blog.get_one(id, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db : Session = Depends(getdb), currentUser : schemas.User = Depends(get_current_user)):
    return blog.delete(id, db) 

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id : int, request: schemas.Blog, db: Session = Depends(getdb), currentUser : schemas.User = Depends(get_current_user)):    
    return blog.update(id, request, db)