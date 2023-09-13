from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("postgresql://app_user:top-secret@localhost/app_db", echo=True)

Base = declarative_base()

Session = sessionmaker()
