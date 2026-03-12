
from django.apps import AppConfig

class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.articles.infrastructure'  # apunta a donde están los modelos
    label = "articles_app"