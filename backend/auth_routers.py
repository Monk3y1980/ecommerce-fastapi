from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash

from database import Session, engine
from models import User
from schemas import SignUp

auth_router = APIRouter(prefix="/auth", tags=["auth"])
session = Session(bind=engine)


@auth_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: SignUp):
    email = session.query(User).filter(user.email == User.email).first()
    if email and email is not None:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with the email already exists",
        )

    user_name = session.query(User).filter(user.username == User.username).first()
    if user_name and user_name is not None:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with the username already exists",
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
        is_active=user.is_active,
        is_staff=user.is_staff,
    )

    session.add(new_user)
    session.commit()
    return new_user
