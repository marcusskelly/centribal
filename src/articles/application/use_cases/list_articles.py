from typing import List

from src.articles.domain.article import Article
from src.articles.application.ports.article_repository import ArticleRepository

# list all articles
class ListArticlesUseCase:

    def __init__(self, repository: ArticleRepository):
        self.repository = repository

    def execute(self) -> List[Article]:
        return self.repository.list_all()