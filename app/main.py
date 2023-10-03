from fastapi import FastAPI, status

from app.admin.routes import router as ecommerce_router
from app.core.auth import router as auth_router
from app.users.routes import router as user_router

app = FastAPI(title="E-Commerce Admin API")

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(ecommerce_router)


@app.get("/", status_code=status.HTTP_200_OK)
def hello():
    return {"message": "Welcome to E-Commerce Admin App by Irshad"}
