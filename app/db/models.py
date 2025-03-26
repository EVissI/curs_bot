from sqlalchemy import Integer,BIGINT
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    
    telegram_id: Mapped[int] = mapped_column(BIGINT,nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    

class Сurrency(Base):
    __tablename__ = 'currencies'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    currency_name: Mapped[str] = mapped_column(nullable=False)
    buy_value:Mapped[str] = mapped_column(nullable=True)
    sell_value:Mapped[str] = mapped_column(nullable=True)