from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Date
from ..dao import Base
from decimal import Decimal
from datetime import date
from typing import List
from fastapi_users.db import SQLAlchemyBaseUserTable




class User(SQLAlchemyBaseUserTable[int],Base):
    __tablename__ = 'users'
    
    id : Mapped[int] = mapped_column(unique=True, autoincrement=True, primary_key=True)
    balance : Mapped[Decimal] = mapped_column()
    
    send_transactions : Mapped[List['Transaction']] = relationship(back_populates='sender', foreign_keys= 'Transaction.sender_id')
    receive_transactions : Mapped[List['Transaction']] = relationship(back_populates='recipient', foreign_keys='Transaction.recipient_id')
    


class Transaction(Base):
    __tablename__ =  'transactions'
    
    id : Mapped[int] = mapped_column(unique=True, autoincrement=True, primary_key=True)

    sender_id : Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    recipient_id : Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    amount : Mapped[Decimal] = mapped_column()
    day : Mapped[date] = mapped_column(Date)
    status : Mapped[str] = mapped_column()

    sender : Mapped['User'] = relationship(back_populates='send_transactions', foreign_keys=[sender_id])
    recipient : Mapped['User'] = relationship(back_populates='receive_transactions', foreign_keys=[recipient_id])