from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Customer:
    loyal: bool

    def is_loyal(self) -> bool:
        return self.loyal


@dataclass(frozen=True)
class OrderItem:
    price: float
    quantity: float


@dataclass(frozen=True)
class OrderSummary:
    subtotal: float
    discount: float
    tax: float
    total: float


class Order:
    def __init__(self, items: List[OrderItem], customer: Customer):
        self.items = items
        self.customer = customer

    def summarise(self) -> OrderSummary:
        # Validation
        self.validate()

        # Subtotal calculation
        subtotal = self.get_subtotal()

        # Discount rules
        discount = self.get_discount(subtotal)

        # Tax calculation
        taxable_amount = subtotal - discount
        tax = self.get_tax(taxable_amount)

        # Total calculation
        total = taxable_amount + tax

        return OrderSummary(subtotal, discount, tax, total)

    def get_tax(self, taxable_amount):
        return taxable_amount * 0.20

    def get_discount(self, subtotal):
        discount = 0.0
        if self.customer.is_loyal():
            discount = subtotal * 0.10
        elif subtotal > 100:
            discount = subtotal * 0.05
        return discount

    def get_subtotal(self):
        return sum(item.price * item.quantity for item in self.items)

    def validate(self):
        if self.items is None:
            raise ValueError("Items cannot be None")
        if len(self.items) == 0:
            raise ValueError("Order must contain items")
