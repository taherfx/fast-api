from database import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):    
    __tablename__ = "blogs"
    id = Column(Integer, primary_key = True, index=True)
    title =  Column(String(20))
    userId = Column(Integer, ForeignKey("users.id"))
    body = Column(String(50))
    creator = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name= Column(String(18))
    email= Column(String(25), unique=True)
    password = Column(Text)
    blogs = relationship("Blog", back_populates="creator")
