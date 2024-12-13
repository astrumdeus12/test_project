from pydantic import BaseModel, Field
from decimal import Decimal



class TransactionSchema(BaseModel):
    
    recipient_id : int
    amount : Decimal = Field(gt=0)