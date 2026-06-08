from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class OrderStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    PREPARING = "preparing"
    READY = "ready"
    OUT_FOR_DELIVERY = "out_for_delivery"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


@dataclass
class Category:
    id: str
    name: str


@dataclass
class MenuItem:
    id: str
    name: str
    category_id: str
    veg: bool = False
    price: float = 0.0
    available: bool = True


@dataclass
class Price:
    amount: float
    currency: str = "USD"


@dataclass
class Availability:
    item_id: str
    available: bool = True


@dataclass
class OrderItem:
    item_id: str
    quantity: int = 1


@dataclass
class Order:
    id: str
    customer_id: str
    items: List[OrderItem] = field(default_factory=list)
    status: OrderStatus = OrderStatus.PENDING
    total: float = 0.0


@dataclass
class CustomerProfile:
    id: str
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None


@dataclass
class Address:
    id: str
    customer_id: str
    line1: str
    line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None


@dataclass
class DeliveryPartner:
    id: str
    name: str
    phone: Optional[str] = None


@dataclass
class Review:
    id: str
    customer_id: str
    target_id: str
    rating: int
    text: Optional[str] = None


@dataclass
class Coupon:
    id: str
    code: str
    discount_percent: Optional[float] = None
    discount_amount: Optional[float] = None
    active: bool = True
