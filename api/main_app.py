from fastapi import FastAPI
from .routers.auth_router import auth_router
from .routers.transactions_router import transaction_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(transaction_router)