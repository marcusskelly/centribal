from src.orders.domain.order import Order
from src.orders.application.ports.order_repository import OrderRepository

# get order by id
class GetOrderUseCase:

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self, order_id: int) -> Order | None:
        return self.repository.get_by_id(order_id)