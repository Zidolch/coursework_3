from typing import Optional

from project.dao.main import GenresDAO
from project.exceptions import ItemNotFound
from project.models import Genre


class GenresService:
    """
    Сервис для работы с жанрами
    """
    def __init__(self, dao: GenresDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Genre:
        """
        Метод для получения одного жанра по pk
        """
        if genre := self.dao.get_by_id(pk):
            return genre
        raise ItemNotFound(f'Genre with pk={pk} does not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Genre]:
        """
        Метод для получения всех жанров
        """
        return self.dao.get_all(page=page)
