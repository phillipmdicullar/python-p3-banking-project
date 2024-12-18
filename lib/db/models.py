from sqlalchemy import Column, Integer, String, Float

from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    account_number = Column(Integer, unique=True, nullable=False)
    account_holder_name = Column(String, nullable=False)
    balance = Column(Float, default=0.0)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
# Setup the database
DATABASE_URL = 'sqlite:///banking_system.db'

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()