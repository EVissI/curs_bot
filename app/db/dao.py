from app.db.base import BaseDAO
from app.db.models import User, Сurrency


class CurencyDAO(BaseDAO):
    model = Сurrency

class UserDAO(BaseDAO):
    model = User