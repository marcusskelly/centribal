from datetime import datetime
from decimal import Decimal


class Article:

    def __init__(self,id: int | None,reference: str,name: str,description: str,price_without_tax: Decimal,tax: Decimal,created_at: datetime | None = None):
        self.id = id
        self.reference = reference
        self.name = name
        self.description = description
        self.price_without_tax = price_without_tax
        self.tax = tax
        self.created_at = created_at

    def price_with_tax(self) -> Decimal:
        
        return self.price_without_tax + (self.price_without_tax * self.tax)