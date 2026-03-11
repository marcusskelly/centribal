from datetime import datetime
from typing import List
from src.orders.domain.order import Order
from src.orders.domain.order_item import OrderItem
from src.orders.application.ports.order_repository import OrderRepository
from src.articles.application.ports.article_repository import ArticleRepository

# create a new order
class CreateOrderUseCase:

    def __init__(self, order_repository: OrderRepository, article_repository: ArticleRepository):
        self.order_repository = order_repository
        self.article_repository = article_repository

    def execute(self, items: List[OrderItem]) -> Order:

        articles = self.article_repository.list_all()

        # instantiate new order object
        order = Order(id=None, items=items,created_at=datetime.now())

        order.calculate_totals(articles)

        return self.order_repository.save(order)