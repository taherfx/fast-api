from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import models, hashing, schemas

def get_all(db: Session):
    query = db.query(models.User).all()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user found")
    return query

def get_one(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the user id {id} is not found")
    return user

def insert_user(request: schemas.User, db: Session):
    query = models.User(name = request.name, email = request.email, password = hashing.Hash.bcrypt(request.password))
    db.add(query)
    db.commit()
    db.refresh(query)
    return query