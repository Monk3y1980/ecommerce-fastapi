from fastapi import FastAPI
from routers.auth_routers import auth_router
from routers.order_routers import order_router


app = FastAPI()
app.include_router(auth_router)
app.include_router(order_router)