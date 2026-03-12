from django.urls import path
from src.orders.infrastructure.api.views import (
    OrderListCreateView,
    OrderDetailView
)

urlpatterns = [
    path("", OrderListCreateView.as_view()),
    path("<int:order_id>/", OrderDetailView.as_view()),
]