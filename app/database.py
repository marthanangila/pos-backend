from sqlalchemy import create_engine
from app.config import get_settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

settings= get_settings()
engine= create_engine(settings.database_url)

SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base= declarative_base()
