from abc import ABC, abstractmethod
from typing import List
from src.articles.domain.article import Article

class ArticleRepository(ABC):

    # save an article
    @abstractmethod
    def save(self, article: Article) -> Article:
        pass

    # Update an existing article
    @abstractmethod
    def update(self, article: Article) -> Article:
        pass

    # Retrieve an article by its id
    @abstractmethod
    def get_by_id(self, article_id: int) -> Article | None:
        pass
    
    # Retrieve all articles
    @abstractmethod
    def list_all(self) -> List[Article]:
        pass