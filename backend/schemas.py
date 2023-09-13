from pydantic import BaseModel
from typing import Optional


class SignUp(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "password",
                "is_staff": False,
                "is_active": True,
            }
        }


class Settings(BaseModel):
    authjwt_secret_key: str = (
        "b4bb9013c1c03b29b9311ec0df07f3b0d8fd13edd02d5c45b2fa7b86341fa405"
    )


class LoginModel(BaseModel):
    username: str
    password: str


class Order(BaseModel):
    id: Optional[int]
    order_status: Optional[str] = "PENDING"
    service: Optional[str] = "BUSINESS-SUPPORT"
    user_id: Optional[int]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {"order_status": "PENDING", "service": "BUSINESS-SUPPORT"}
        }


class OrderStatus(BaseModel):
    order_status: Optional[str] = "PENDING"

    class Config:
        orm_mode = True
        schema_extra = {"example": {"order_status": "PENDING"}}
