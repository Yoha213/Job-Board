from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.create import create_engine
from app.core.config import settings

database_url = f"postgresql+psycopg://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

engine=create_engine(url=database_url)
SessionLocal=sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():

    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()