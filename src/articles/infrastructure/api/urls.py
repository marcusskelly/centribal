from django.urls import path

from src.articles.infrastructure.api.views import (
    ArticleListCreateView,
    ArticleDetailView
)

urlpatterns = [
    path("articles/", ArticleListCreateView.as_view()),
    path("articles/<int:article_id>/", ArticleDetailView.as_view()),
]