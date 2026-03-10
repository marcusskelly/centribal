from datetime import datetime
from decimal import Decimal
from typing import List
from .order_item import OrderItem
from src.articles.domain.article import Article


class Order:

    def __init__(self,id: int | None,items: List[OrderItem],created_at: datetime | None = None):
        self.id = id
        self.items = items
        self.created_at = created_at
        self.total_without_tax = Decimal("0.00")
        self.total_with_tax = Decimal("0.00")

    def calculate_totals(self, articles: list[Article]) -> None:

        total = Decimal("0.00")
        total_with_tax = Decimal("0.00")

        articles_by_reference = {}

        #{"123": Article(),"456": Article()}
        for article in articles:
            articles_by_reference[article.reference] = article

        for item in self.items:

            article = articles_by_reference.get(item.reference)

            if article is None:
                raise ValueError(f"Article with reference {item.reference} not found")

            subtotal = article.price_without_tax * item.quantity
            subtotal_with_tax = subtotal + (subtotal * article.tax)

            total += subtotal
            total_with_tax += subtotal_with_tax

        self.total_without_tax = total
        self.total_with_tax = total_with_tax