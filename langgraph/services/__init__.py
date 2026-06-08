"""Service package: exports service classes for the application.

Each module under this package provides a simple service class with
method stubs. These are intended as a starting point for implementation.
"""
from .catalog import CatalogService
from .order import OrderService
from .kitchen import KitchenService
from .user import UserService
from .delivery import DeliveryService
from .notification import NotificationService
from .billing import BillingService
from .review import ReviewService
from .search import SearchService
from .promo import PromoService

__all__ = [
    "CatalogService",
    "OrderService",
    "KitchenService",
    "UserService",
    "DeliveryService",
    "NotificationService",
    "BillingService",
    "ReviewService",
    "SearchService",
    "PromoService",
]
