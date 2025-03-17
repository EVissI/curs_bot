from pydantic import BaseModel

class СurrencyModel(BaseModel):
    currency_name:str
    buy_value:str
    sell_value:str

class СurrencyFilter(BaseModel):
    currency_name:str = None
    sell_value:str = None
    buy_value:str = None