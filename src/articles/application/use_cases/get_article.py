from src.articles.domain.article import Article
from src.articles.application.ports.article_repository import ArticleRepository

# get article by id
class GetArticleUseCase:

    def __init__(self, repository: ArticleRepository):
        self.repository = repository

    def execute(self, article_id: int) -> Article | None:
        return self.repository.get_by_id(article_id)