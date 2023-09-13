from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Orders

OrderInSchema = pydantic_model_creator(
    Orders, name="OrderIn", exclude=["user_id"], exclude_readonly=True)
OrderOutSchema = pydantic_model_creator(
    Orders, name="Order", exclude =[
      "modified_at", "user.password", "author.created_at", "author.modified_at"
    ]
)


class UpdateOrder(BaseModel):
    status: int
