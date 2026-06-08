"""Lightweight registry of service instances.

This module provides a simple programmatic registry of service instances
to make it easier to wire components together in examples and tests.
"""
from .services.inmemory import InMemoryCatalogService, InMemoryOrderService, InMemoryKitchenService
from .services import (
    UserService,
    DeliveryService,
    NotificationService,
    BillingService,
    ReviewService,
    SearchService,
    PromoService,
)


def get_service_registry() -> dict:
    """Return a dict of name -> service instance.

    This provides simple in-memory implementations for core services to
    power the demo agent. Replace these with production implementations
    or DI wiring as needed.
    """
    catalog = InMemoryCatalogService()
    order = InMemoryOrderService(catalog)
    kitchen = InMemoryKitchenService()

    return {
        "catalog": catalog,
        "order": order,
        "kitchen": kitchen,
        "user": UserService(),
        "delivery": DeliveryService(),
        "notification": NotificationService(),
        "billing": BillingService(),
        "review": ReviewService(),
        "search": SearchService(),
        "promo": PromoService(),
    }
