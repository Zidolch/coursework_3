from flask import request
from flask_restx import Namespace, Resource

from project.container import movie_service
from project.setup.api.models import movie
from project.setup.api.parsers import page_parser

api = Namespace('movies')


@api.route('/')
class MoviesView(Resource):
    """
    Представление для всех фильмов
    """
    @api.expect(page_parser)
    @api.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """
        Получить все фильмы по указанным параметрам
        """
        filter = request.args.get('status')
        if filter is not None and filter == 'new':
            return movie_service.get_all_by_order(filter=filter, **page_parser.parse_args())
        else:
            return movie_service.get_all(**page_parser.parse_args())


@api.route('/<int:movie_id>/')
class MovieView(Resource):
    """
    Представление для одного фильма
    """
    @api.response(404, 'Not Found')
    @api.marshal_with(movie, code=200, description='OK')
    def get(self, movie_id: int):
        """
        Получить фильм по id
        """
        return movie_service.get_item(movie_id)