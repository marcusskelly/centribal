from typing import List
from src.articles.application.ports.article_repository import ArticleRepository
from src.articles.domain.article import Article
from src.articles.infrastructure.models.article_model import ArticleModel

class ORMArticleRepository(ArticleRepository):

    # Recibe entidad de domain, guarda en bbdd y devuelve el objeto convertido a domain
    def save(self, article: Article) -> Article:

        model = ArticleModel.objects.create(
            reference=article.reference,
            name=article.name,
            description=article.description,
            price_without_tax=article.price_without_tax,
            tax=article.tax,
        )

        return self.model_to_domain(model)
    
    # Busca el objeto en bbdd, actualiza campos, guarda y devuelve el objeto convertido a domain
    def update(self, article: Article) -> Article:

        model = ArticleModel.objects.get(id=article.id)

        model.reference = article.reference
        model.name = article.name
        model.description = article.description
        model.price_without_tax = article.price_without_tax
        model.tax = article.tax

        model.save()

        return self.model_to_domain(model)

    def get_by_id(self, article_id: int) -> Article | None:

        try:
            model = ArticleModel.objects.get(id=article_id)
            return self.model_to_domain(model)
        except ArticleModel.DoesNotExist:
            return None

    def list_all(self) -> List[Article]:

        models = ArticleModel.objects.all()
        
        articles = []

        for model in models:
            articles.append(self.model_to_domain(model))

        return articles

    def model_to_domain(self, model: ArticleModel) -> Article:

        return Article(
            id=model.id,
            reference=model.reference,
            name=model.name,
            description=model.description,
            price_without_tax=model.price_without_tax,
            tax=model.tax,
            created_at=model.created_at,
        )