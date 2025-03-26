from typing import Optional
from pydantic import BaseModel
from sqlalchemy import BigInteger


class UserModel(BaseModel):
    username:Optional[str]
    first_name:str
    last_name:Optional[str]
    telegram_id:int
    class Config:
        from_attributes = True
        arbitrary_types_allowed=True

class UserFilter(BaseModel):
    username:Optional[str] = None
    first_name:str = None
    last_name:Optional[str] = None
    telegram_id:int = None
    
    class Config:
        from_attributes = True
        arbitrary_types_allowed=True

class СurrencyModel(BaseModel):
    currency_name:str
    buy_value:str
    sell_value:str

class СurrencyFilter(BaseModel):
    currency_name:str = None
    sell_value:str = None
    buy_value:str = None