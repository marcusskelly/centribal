# tests/unit/test_article_use_cases.py

import pytest
from src.articles.domain.article import Article
from src.articles.application.use_cases.create_article import CreateArticleUseCase
from src.articles.application.use_cases.update_article import UpdateArticleUseCase
from src.articles.application.use_cases.get_article import GetArticleUseCase
from src.articles.application.use_cases.list_articles import ListArticlesUseCase


class TestArticleRepository:

    def __init__(self):
        self.articles = []

    def save(self, article: Article):
        if article.id is None:
            article.id = len(self.articles) + 1
            self.articles.append(article)
        else:
            for idx, existing in enumerate(self.articles):
                if existing.id == article.id:
                    self.articles[idx] = article
        return article

    def get_by_id(self, article_id):
        for article in self.articles:
            if article.id == article_id:
                return article
        return None

    def list_all(self):
        return self.articles

# inyecta el objeto de la clase a cada función
@pytest.fixture
def repo():
    return TestArticleRepository()


def test_create_article(repo):
    use_case = CreateArticleUseCase(repo)
    article = use_case.execute(
        reference="123",
        name="Portatil",
        description="Portatil gaming",
        price_without_tax=400
    )

    assert article.id == 1
    assert article.reference == "123"
    assert article.name == "Portatil"
    assert article.price_without_tax == 400


def test_update_article(repo):
    
    create_uc = CreateArticleUseCase(repo)
    article = create_uc.execute(
        reference="A234",
        name="laptop1",
        description="laptop for gaming",
        price_without_tax=100,
        tax=0.1,
    )

    update_uc = UpdateArticleUseCase(repo)
    updated = update_uc.execute(
        article_id=article.id,
        name="new laptop",
        description="Nueva descipcion",
        price_without_tax=120
    )

    assert updated.id == article.id
    assert updated.name == "New Name"
    assert updated.description == "New Description"
    assert updated.price_without_tax == 120


def test_get_article(repo):
    create_uc = CreateArticleUseCase(repo)
    article = create_uc.execute(
        reference="345",
        name="Test Article",
        description="Descripcion",
        price_without_tax=50,
        tax=0.05,
    )

    get_uc = GetArticleUseCase(repo)
    fetched = get_uc.execute(article_id=article.id)

    assert fetched.id == article.id
    assert fetched.name == "Test Article"
    assert fetched.reference == "345"


def test_list_articles(repo):
    create_uc = CreateArticleUseCase(repo)
    create_uc.execute(
        reference="A4",
        name="Article 1",
        description="Desc 1",
        price_without_tax=10,
        tax=0.1
    )
    create_uc.execute(
        reference="A5",
        name="Article 2",
        description="Desc 2",
        price_without_tax=20,
        tax=0.2
    )

    list_uc = ListArticlesUseCase(repo)
    articles = list_uc.execute()

    assert len(articles) == 2
    references = []
    for article in articles:
        references.append(article.reference)
    assert "A4" in references
    assert "A5" in references