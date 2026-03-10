from abc import ABC, abstractmethod
from typing import List
from src.orders.domain.order import Order

class OrderRepository(ABC):

    # save an order
    @abstractmethod
    def save(self, order: Order) -> Order:
        pass

    # Update an existing order
    @abstractmethod
    def update(self, order: Order) -> Order:
        pass

    # Retrieve an order by its id
    @abstractmethod
    def get_by_id(self, order_id: int) -> Order | None:
        pass

    # Retrieve all orders
    @abstractmethod
    def list_all(self) -> List[Order]:
        pass