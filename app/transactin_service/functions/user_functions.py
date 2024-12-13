from decimal import Decimal
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from database.dao import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.settings import get_async_session



async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_or_none(session : AsyncSession, user_id : int):
    result = await session.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    return user


async def decrease_balance(session : AsyncSession, user : User, amount : Decimal):
    new_balance = user.balance - Decimal(amount)
    user.balance = new_balance
    session.add(user)
    


async def increase_balance(session : AsyncSession, user : User, amount : Decimal):
    new_balance = user.balance + Decimal(amount)
    user.balance = new_balance
    session.add(user)
    
