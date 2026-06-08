from typing import Optional
from ..models import Coupon


class PromoService:
    """Manage coupons, offers, and promo validation."""

    def create_coupon(self, coupon: Coupon) -> Coupon:
        raise NotImplementedError

    def validate_coupon(self, code: str, order_id: str) -> Optional[Coupon]:
        return None
