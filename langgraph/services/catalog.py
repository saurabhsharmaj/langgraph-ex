from typing import List, Optional
from ..models import Category, MenuItem, Price, Availability


class CatalogService:
    """Handles catalog operations: categories, menu, pricing, availability."""

    def list_categories(self) -> List[Category]:
        """Return all food categories."""
        return []

    def get_menu(self, category_id: Optional[str] = None) -> List[MenuItem]:
        """Return menu items, optionally filtered by category."""
        return []

    def set_price(self, item_id: str, price: Price) -> None:
        """Update pricing for a menu item."""
        raise NotImplementedError

    def check_availability(self, item_id: str) -> Availability:
        """Return availability info for an item."""
        return Availability(item_id=item_id, available=True)
