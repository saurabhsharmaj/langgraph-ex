from typing import List
from ..models import Order, OrderItem, OrderStatus


class OrderService:
    """Create and manage orders."""

    def create_order(self, customer_id: str, items: List[OrderItem]) -> Order:
        """Create a new order and return it."""
        raise NotImplementedError

    def update_order_status(self, order_id: str, status: OrderStatus) -> None:
        """Update the status of an existing order."""
        raise NotImplementedError

    def get_order_history(self, customer_id: str) -> List[Order]:
        """Return past orders for a customer."""
        return []
