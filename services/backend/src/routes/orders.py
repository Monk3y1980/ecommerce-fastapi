from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.orders as crud
from src.auth.jwthandler import get_current_user
from src.schemas.orders import OrderOutSchema, OrderInSchema, UpdateOrder
from src.schemas.token import Status
from src.schemas.users import UserOutSchema


router = APIRouter()


@router.get(
    "/order",
    response_model=List[OrderOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_order():
    return await crud.get_order()


@router.get(
    "/order/{order_id}",
    response_model=OrderOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_order(order_id: int) -> OrderOutSchema:
    try:
        return await crud.get_order(order_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Order does not exist",
        )


@router.post(
    "/order", response_model=OrderOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_order(
    order: OrderInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> OrderOutSchema:
    return await crud.create_order(order, current_user)


@router.patch(
    "/order/{order_id}",
    dependencies=[Depends(get_current_user)],
    response_model=OrderOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_order(
    order_id: int,
    order: UpdateOrder,
    current_user: UserOutSchema = Depends(get_current_user),
) -> OrderOutSchema:
    return await crud.update_order(order_id, order, current_user)


@router.delete(
    "/order/{order_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_order(
    order_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_order(order_id, current_user)
