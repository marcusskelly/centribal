from typing import List
from src.orders.domain.order import Order
from src.orders.application.ports.order_repository import OrderRepository

# list orders
class ListOrdersUseCase:

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self) -> List[Order]:
        return self.repository.list_all()