from django.db import models
from src.orders.infrastructure.models.order_model import OrderModel

# Django ORM model for Order items
class OrderItemModel(models.Model):

    # relacion 1:N con Order
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name="items")

    reference = models.CharField(max_length=100)

    quantity = models.PositiveIntegerField()
    
    class Meta:
        db_table = "order_items"