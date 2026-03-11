from src.orders.domain.order import Order
from src.orders.application.ports.order_repository import OrderRepository
from src.articles.application.ports.article_repository import ArticleRepository

# update an order by id
class UpdateOrderUseCase:

    def __init__(self, order_repository: OrderRepository, article_repository: ArticleRepository):
        self.order_repository = order_repository
        self.article_repository = article_repository

    def execute(self, order: Order) -> Order:

        existing = self.order_repository.get_by_id(order.id)

        if existing is None:
            raise ValueError(f"Order with id {order.id} does not exist")

        articles = self.article_repository.list_all()

        order.calculate_totals(articles)

        return self.order_repository.update(order)