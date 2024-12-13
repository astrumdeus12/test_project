from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import date

class TransactionStatus(Enum):
    accessed = "accepted"
    rejected = "rejected"

class TransactionSchema(BaseModel):
    
    recipient_id : int
    amount : Decimal = Field(gt=0)

class TansactionFilterSchema(BaseModel):
    start_date : Optional[date] = None
    end_date : Optional[date] = None
    status: TransactionStatus = None
    page : int = 1