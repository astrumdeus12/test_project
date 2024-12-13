from decimal import Decimal
from database.dao import Transaction
from database.settings import get_async_session
from ...dto.transaction_schema import TransactionSchema
from .user_functions import get_user_or_none, increase_balance, decrease_balance
from datetime import date 
from logs.settings import transaction_logger



async def add_new_transaction(sender_id : int, transaction : TransactionSchema):
    async for session in get_async_session():
        async with session.begin():
            
            amount = Decimal(transaction.amount)
            day = date.today()
            sender = await get_user_or_none(session, sender_id)
            recipient = await get_user_or_none(session, transaction.recipient_id)
            status = 'accepted'
            text = 'текст успешной транзакции'
            
            if not recipient:
                return 'текст о том, что получатель не найден'

            if amount > sender.balance:
                status = 'rejected'
                text = 'текст о недостаточном балансе'

            else:
                text = 'текст успешной транзакции'
                await increase_balance(session, recipient, amount)
                await decrease_balance(session, sender, amount)
            
            new_transaction = Transaction(sender_id = sender_id, recipient_id = transaction.recipient_id,
                                          amount = transaction.amount, day = day, status = status)
            session.add(new_transaction)
            transaction_logger.info(f'Транзакция: перевод {transaction.amount} от {sender_id} к {transaction.recipient_id} статус: {status}')
            await session.commit()
            return text
                
            
            

async def balance_replenishment(user_id : int, amount : Decimal):
    async for session in get_async_session():
        async with session.begin():
            user = await get_user_or_none(session, user_id)
            await increase_balance(session, user, amount)
            await session.commit()
            status = 'accepted'
            
            transaction_logger.info(f'Транзакция: пополнение {amount} пользователь {user_id} статус: {status}')
            return f'Пополнение баланса на {amount} текущий баланас: {user.balance}'
            
            
async def balance_withdrawal(user_id : int, amount : Decimal):
    async for session in get_async_session():
        async with session.begin():
            user = await get_user_or_none(session, user_id)
            status = 'accepted'
            text = f'Вывод средств на {amount} текущий баланас: {user.balance - amount}'
            if amount > user.balance:
                
                text = f'Недостаточный баланс для вывода средств \n Текущий баланс: {user.balance}'
            
                
            await decrease_balance(session, user, amount)
            await session.commit()
            
            
            transaction_logger.info(f'Транзакция: вывод {amount} пользователь {user_id} статус: {status}')
            return text