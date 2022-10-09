from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://habrpguser:pgpwd4habr@localhost:5432/habrdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
