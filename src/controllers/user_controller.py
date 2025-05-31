from database import SessionLocal
from models.user import User
from utils.security import hash_password

def get_all_users():
    session = SessionLocal()
    users = session.query(User).all()
    session.close()
    return users

def get_user_by_id(user_id: int):
    session = SessionLocal()
    user = session.query(User).get(user_id)
    session.close()
    return user

def create_user(firstname: str, lastname: str, email: str, password: str):
    session = SessionLocal()
    user = User(
        firstname=firstname,
        lastname=lastname,
        email=email,
        password=hash_password(password),
    )
    session.add(user)
    session.commit()
    session.close()
    return user

def delete_user(user_id: int):
    session = SessionLocal()
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
    session.close()

def update_user(user_id: int, firstname: str, lastname: str, email: str, password: str = None):
    session = SessionLocal()
    user = session.query(User).get(user_id)
    if user:
        user.firstname = firstname
        user.lastname = lastname
        user.email = email
        if password:
            user.password = hash_password(password)
        session.commit()
    session.close()
