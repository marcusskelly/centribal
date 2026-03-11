from django.db import models

# Django ORM model for Order
class OrderModel(models.Model):

    total_without_tax = models.DecimalField(max_digits=12, decimal_places=2)

    total_with_tax = models.DecimalField(max_digits=12, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "orders"

    def __str__(self):
        return f"Order {self.id}"