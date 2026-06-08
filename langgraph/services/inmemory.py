from typing import Dict, List, Optional
from ..models import Category, MenuItem, Order, OrderItem, CustomerProfile, Availability


class InMemoryCatalogService:
    def __init__(self):
        self.categories: Dict[str, Category] = {
            "c1": Category(id="c1", name="Burgers"),
            "c2": Category(id="c2", name="Pizzas"),
        }
        self.menu: Dict[str, MenuItem] = {
            "m1": MenuItem(id="m1", name="Classic Burger", category_id="c1", veg=False, price=5.99),
            "m2": MenuItem(id="m2", name="Veggie Pizza", category_id="c2", veg=True, price=9.99),
        }

    def list_categories(self) -> List[Category]:
        return list(self.categories.values())

    def get_menu(self, category_id: Optional[str] = None) -> List[MenuItem]:
        if category_id:
            return [m for m in self.menu.values() if m.category_id == category_id]
        return list(self.menu.values())

    def set_price(self, item_id: str, price) -> None:
        if item_id in self.menu:
            self.menu[item_id].price = price.amount

    def check_availability(self, item_id: str) -> Availability:
        item = self.menu.get(item_id)
        return Availability(item_id=item_id, available=(item is not None and item.available))


class InMemoryOrderService:
    def __init__(self, catalog: InMemoryCatalogService):
        self.catalog = catalog
        self.orders: Dict[str, Order] = {}
        self._id = 1

    def create_order(self, customer_id: str, items: List[Dict]) -> Order:
        order_id = f"o{self._id}"
        self._id += 1
        order_items = []
        total = 0.0
        for it in items:
            item_id = it.get("item_id")
            qty = it.get("quantity", 1)
            menu_item = self.catalog.menu.get(item_id)
            price = menu_item.price if menu_item else 0.0
            order_items.append(OrderItem(item_id=item_id, quantity=qty))
            total += price * qty
        order = Order(id=order_id, customer_id=customer_id, items=order_items, total=total)
        self.orders[order_id] = order
        return order

    def update_order_status(self, order_id: str, status) -> None:
        o = self.orders.get(order_id)
        if not o:
            raise KeyError("order not found")
        o.status = status

    def get_order_history(self, customer_id: str) -> List[Order]:
        return [o for o in self.orders.values() if o.customer_id == customer_id]


class InMemoryKitchenService:
    def __init__(self):
        self.queue: List[str] = []
        self.assignments: Dict[str, str] = {}

    def enqueue_order(self, order_id: str) -> None:
        self.queue.append(order_id)

    def assign_chef(self, order_id: str, chef_id: str) -> None:
        self.assignments[order_id] = chef_id

    def track_preparation(self, order_id: str) -> Dict:
        return {"order_id": order_id, "status": "queued" if order_id in self.queue else "unknown"}
