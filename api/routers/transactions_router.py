from datetime import date
from typing import Optional
from fastapi import APIRouter, Depends
from app.auth_service.auth_settings import fastapi_users
from app.dto.transaction_schema import TransactionSchema, TransactionStatus
from database.dao import User
from app.transactin_service.functions.transaction_functions import add_new_transaction, balance_replenishment, balance_withdrawal, filter_transactions


transaction_router = APIRouter(prefix='/transaction', tags=['transaction'])

current_active_user = fastapi_users.current_user(active=True)

@transaction_router.post('/make_transaction')
async def make_transaction(new_transaction : TransactionSchema, user : User = Depends(current_active_user)):
    result = await add_new_transaction(user.id, new_transaction)
    return result


@transaction_router.post('/add_balance')
async def add_balance(transaction : TransactionSchema, user : User = Depends(current_active_user)):
    amount = transaction.amount
    user_id = user.id
    result = await balance_replenishment(user_id, amount)
    return result

@transaction_router.post('/subtract_balance')
async def subtract_balance(transaction : TransactionSchema, user : User = Depends(current_active_user)):
    amount = transaction.amount
    user_id = user.id
    result = await balance_withdrawal(user_id, amount)
    return result


@transaction_router.get("/all_transactions")
async def get_user_transactions(start_date : Optional[date] = None,
                                end_date : Optional[date] = None,
                                status: TransactionStatus = None,
                                page : int = 1, 
                                user : User = Depends(current_active_user)):
    
    result = await filter_transactions(status, start_date, end_date, page, user)
    return result


