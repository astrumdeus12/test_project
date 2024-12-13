from decimal import Decimal


from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    balance : Decimal


class UserCreate(schemas.BaseUserCreate):
    balance : Decimal


class UserUpdate(schemas.BaseUserUpdate):
    balance : Decimal