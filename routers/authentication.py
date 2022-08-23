from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
import schemas, models
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import getdb
from hashing import Hash
from token_generate import create_access_token

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(getdb)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid username or password")
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid username or password")
        
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}