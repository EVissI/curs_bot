from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base


class Сurrency(Base):
    __tablename__ = 'currencies'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    currency_name: Mapped[str] = mapped_column(nullable=False)
    buy_value:Mapped[str] = mapped_column(nullable=True)
    sell_value:Mapped[str] = mapped_column(nullable=True)