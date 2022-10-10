from typing import Optional

from project.dao.main import MoviesDAO
from project.exceptions import ItemNotFound
from project.models import Movie


class MoviesService:
    """
    Сервис для работы с фильмами
    """
    def __init__(self, dao: MoviesDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        """
        Метод для получения одного фильма по pk
        """
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Movie with pk={pk} does not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Movie]:
        """
        Метод для получения всех фильмов
        """
        return self.dao.get_all(page=page)

    def get_all_by_order(self, page: Optional[int] = None, filter: Optional[int] = None) -> list[Movie]:
        """
        Метод для получения всех фильмов в указанном порядке
        """
        return self.dao.get_all_by_order(page=page, filter=filter)
