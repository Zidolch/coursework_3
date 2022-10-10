from typing import Optional

from project.dao.main import DirectorsDAO
from project.exceptions import ItemNotFound
from project.models import Director


class DirectorsService:
    """
    Сервис для работы с режиссерами
    """
    def __init__(self, dao: DirectorsDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Director:
        """
        Метод для получения одного режиссера по pk
        """
        if director := self.dao.get_by_id(pk):
            return director
        raise ItemNotFound(f'Director with pk={pk} does not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Director]:
        """
        Метод для получения всех режиссеров
        """
        return self.dao.get_all(page=page)
