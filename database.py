from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/blog"

engine = create_engine(DATABASE_URL, echo = True)
meta = MetaData()

SessionLocal = sessionmaker(bind = engine,autocommit=False, autoflush=False)

Base = declarative_base()

def getdb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()