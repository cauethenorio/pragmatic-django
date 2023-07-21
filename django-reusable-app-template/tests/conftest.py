from pytest_factoryboy import register

from . import factories

register(factories.UserFactory)
register(factories.AuthorFactory)
register(factories.ArticleFactory)
register(factories.CommentFactory)
