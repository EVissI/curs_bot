from pydantic import BaseModel

class СurrencyModel(BaseModel):
    currency_name:str
    currency_name_for_bot:str
    value:str

class СurrencyFilter(BaseModel):
    currency_name:str = None
    currency_name_for_bot:str = None
    value:str = None