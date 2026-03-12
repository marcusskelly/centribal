from django.contrib import admin
from .models.article_model import ArticleModel

@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "reference", "name", "price_without_tax", "tax", "created_at")
    search_fields = ("reference", "name")
    list_filter = ("created_at",)