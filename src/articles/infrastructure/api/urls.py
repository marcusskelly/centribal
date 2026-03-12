from django.urls import path

from src.articles.infrastructure.api.views import (
    ArticleListCreateView,
    ArticleDetailView
)

urlpatterns = [
    path("", ArticleListCreateView.as_view()),
    path("<int:article_id>/", ArticleDetailView.as_view()),
]