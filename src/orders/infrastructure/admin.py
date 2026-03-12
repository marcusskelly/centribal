from django.contrib import admin
from .models.order_model import OrderModel
from .models.order_item_model import OrderItemModel

class OrderItemInline(admin.TabularInline):
    model = OrderItemModel
    extra = 1  # número de líneas adicionales al crear un pedido

@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at")
    inlines = [OrderItemInline]