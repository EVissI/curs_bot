from pydantic import BaseModel
from sqlalchemy import BigInteger


class UserModel(BaseModel):
    username:str
    first_name:str
    last_name:str
    telegram_id:BigInteger
    class Config:
        arbitrary_types_allowed=True

class UserFilter(BaseModel):
    username:str = None
    first_name:str = None
    last_name:str = None
    telegram_id:BigInteger = None
    class Config:
        arbitrary_types_allowed=True

class СurrencyModel(BaseModel):
    currency_name:str
    buy_value:str
    sell_value:str

class СurrencyFilter(BaseModel):
    currency_name:str = None
    sell_value:str = None
    buy_value:str = None