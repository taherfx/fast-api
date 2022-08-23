from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import models, schemas

def get_all(db : Session):
    query = db.query(models.Blog).all()
    return query

def insert_blog(request: schemas.Blog, db : Session):
    new_blog = models.Blog(title= request.title, body= request.body, userId = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_one(id: int, db : Session):
    query = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not query:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Blog with the id {id} not avaliable"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} not avaliable")
    return query

def delete(id: int, db: Session):
    # query = db.query(models.Blog).get(id)
    # db.delete(query)
    query = db.query(models.Blog).filter(models.Blog.id == id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    query.delete(synchronize_session=False)
    db.commit()
    return "done"

def update(id: int, request: schemas.Blog, db: Session):
    query = db.query(models.Blog).filter(models.Blog.id == id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    query.update(request.dict())
    db.commit()
    return f"{request.title} is Updated"