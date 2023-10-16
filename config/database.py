from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'postgresql://xavierfrancisco353:A6b2DqYBniXw@ep-throbbing-heart-50387528.us-east-2.aws.neon.tech/urbantrade'

engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Database Utilities
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
