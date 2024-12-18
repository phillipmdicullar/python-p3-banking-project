from models import User, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bank.db")  # Or your chosen database
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

# Seed default users
default_users = [
    {"username": "admin", "password": "admin123", "role": "admin"},
    {"username": "user1", "password": "password1", "role": "customer"},
    {"username": "user2", "password": "password2", "role": "customer"},
]

for user_data in default_users:
    user = User(**user_data)
    session.add(user)

session.commit()
