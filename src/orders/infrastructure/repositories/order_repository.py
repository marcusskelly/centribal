from typing import List
from src.orders.application.ports.order_repository import OrderRepository
from src.orders.domain.order import Order
from src.orders.domain.order_item import OrderItem
from src.orders.infrastructure.models.order_model import OrderModel
from src.orders.infrastructure.models.order_item_model import OrderItemModel

class ORMOrderRepository(OrderRepository):

    def save(self, order: Order) -> Order:

        order_model = OrderModel.objects.create(
            total_without_tax=order.total_without_tax,
            total_with_tax=order.total_with_tax
        )

        for item in order.items:
            OrderItemModel.objects.create(
                order=order_model,
                reference=item.reference,
                quantity=item.quantity
            )

        return self.model_to_domain(order_model)

    def update(self, order: Order) -> Order:

        order_model = OrderModel.objects.get(id=order.id)

        order_model.total_without_tax = order.total_without_tax
        order_model.total_with_tax = order.total_with_tax
        order_model.save()

        order_model.items.all().delete()

        for item in order.items:
            OrderItemModel.objects.create(
                order=order_model,
                reference=item.reference,
                quantity=item.quantity
            )

        return self.model_to_domain(order_model)

    def get_by_id(self, order_id: int) -> Order | None:

        try:
            order_model = OrderModel.objects.get(id=order_id)
            return self.model_to_domain(order_model)
        except OrderModel.DoesNotExist:
            return None

    def list_all(self) -> List[Order]:

        models = OrderModel.objects.all()
        orders = []

        for model in models:
            orders.append(self.model_to_domain(model))

        return orders

    def model_to_domain(self, model: OrderModel) -> Order:

        items = [
            OrderItem(
                reference=item.reference,
                quantity=item.quantity
            )
            for item in model.items.all()
        ]

        order = Order(
            id=model.id,
            items=items,
            created_at=model.created_at
        )

        order.total_without_tax = model.total_without_tax
        order.total_with_tax = model.total_with_tax

        return order