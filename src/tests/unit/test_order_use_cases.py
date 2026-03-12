
import pytest
from src.orders.domain.order import Order
from src.orders.application.use_cases.create_order import CreateOrderUseCase
from src.orders.application.use_cases.update_order import UpdateOrderUseCase
from src.orders.application.use_cases.get_order import GetOrderUseCase
from src.orders.application.use_cases.list_orders import ListOrdersUseCase
from src.articles.domain.article import Article


class TestOrderRepository:
    

    def __init__(self):
        self.orders = []

    def save(self, order: Order):
        if order.id is None:
            order.id = len(self.orders) + 1
            self.orders.append(order)
        else:
            # reemplaza el pedido existente
            for idx, existing in enumerate(self.orders):
                if existing.id == order.id:
                    self.orders[idx] = order
        return order

    def get_by_id(self, order_id: int):
        for order in self.orders:
            if order.id == order_id:
                return order
        return None

    def list_all(self):
        result = []
        for order in self.orders:
            result.append(order)
        return result


class TestArticleRepository:


    def get_by_reference(self, reference):
        return Article(
            id=1,
            reference="A1",
            name="Laptop",
            description="Gaming Laptop",
            price_without_tax=1000,
            tax=0.21
        )


@pytest.fixture
def order_repo():
    return TestOrderRepository()


@pytest.fixture
def article_repo():
    return TestArticleRepository()


def test_create_order(order_repo, article_repo):
    use_case = CreateOrderUseCase(order_repo, article_repo)

    items = [{"reference": "A1", "quantity": 2}]
    order = use_case.execute(items)

    assert order.id == 1
    assert order.total_without_tax == 2000 
    assert order.total_with_tax == 2420   


def test_update_order(order_repo, article_repo):
    create_uc = CreateOrderUseCase(order_repo, article_repo)
    order = create_uc.execute([{"reference": "A1", "quantity": 1}])

    update_uc = UpdateOrderUseCase(order_repo, article_repo)
    updated_order = update_uc.execute(order_id=order.id, items=[{"reference": "A1", "quantity": 3}])

    assert updated_order.id == order.id
    assert updated_order.total_without_tax == 3000  
    assert updated_order.total_with_tax == 3630  


def test_get_order(order_repo, article_repo):
    create_uc = CreateOrderUseCase(order_repo, article_repo)
    order = create_uc.execute([{"reference": "A1", "quantity": 2}])

    get_uc = GetOrderUseCase(order_repo)
    fetched = get_uc.execute(order_id=order.id)

    assert fetched.id == order.id
    assert fetched.total_without_tax == 2000
    assert fetched.total_with_tax == 2420


def test_list_orders(order_repo, article_repo):
    create_uc = CreateOrderUseCase(order_repo, article_repo)
    create_uc.execute([{"reference": "A1", "quantity": 1}])
    create_uc.execute([{"reference": "A1", "quantity": 2}])

    list_uc = ListOrdersUseCase(order_repo)
    orders = list_uc.execute()

    assert len(orders) == 2
    ids = []
    for order in orders:
        ids.append(order.id)

    assert 1 in ids
    assert 2 in ids