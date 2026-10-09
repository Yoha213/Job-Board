from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.create import create_engine
from core.config import settings

database_url=f"psql+psycopg://{settings.database_user}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}"

engine=create_engine(url=database_url)
SessionLocal=sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():

    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()