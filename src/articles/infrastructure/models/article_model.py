from django.db import models

# Django ORM model for Article
class ArticleModel(models.Model):

    reference = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    price_without_tax = models.DecimalField(max_digits=10, decimal_places=2)

    tax = models.DecimalField(max_digits=5, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "articles"

    def __str__(self):
        return f"{self.reference} - {self.name}"