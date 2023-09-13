from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Orders
from src.schemas.orders import OrderOutSchema
from src.schemas.token import Status


async def get_orders():
    return await OrderOutSchema.from_queryset(Orders.all())


async def get_order(order_id) -> OrderOutSchema:
    return await OrderOutSchema.from_queryset_single(Orders.get(id=order_id))


async def create_order(order, current_user) -> OrderOutSchema:
    order_dict = order.dict(exclude_unset=True)
    order_dict["user_id"] = current_user.id
    order_obj = await Orders.create(**order_dict)
    return await OrderOutSchema.from_tortoise_orm(order_obj)


async def update_order(order_id, order, current_user) -> OrderOutSchema:
    try:
        db_order = await OrderOutSchema.from_queryset_single(Orders.get(id=order_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Order {order_id} not found")

    if db_order.author.id == current_user.id:
        await Orders.filter(id=order_id).update(**order.dict(exclude_unset=True))
        return await OrderOutSchema.from_queryset_single(Orders.get(id=order_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


async def delete_order(order_id, current_user) -> Status:
    try:
        db_order = await OrderOutSchema.from_queryset_single(Orders.get(id=order_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Order {order_id} not found")

    if db_order.author.id == current_user.id:
        deleted_count = await Orders.filter(id=order_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
        return Status(message=f"Deleted order {order_id}")

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")
