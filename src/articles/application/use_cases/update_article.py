from decimal import Decimal

from src.articles.domain.article import Article
from src.articles.application.ports.article_repository import ArticleRepository

# update an article
class UpdateArticleUseCase:

    def __init__(self, repository: ArticleRepository):
        self.repository = repository

    def execute(self, article: Article) -> Article:
       
        existing = self.repository.get_by_id(article.id)
        if existing is None:
            raise ValueError(f"Article with id {article.id} does not exist")

        return self.repository.update(article)