from typing import Optional
from ..models import DeliveryPartner


class DeliveryService:
    """Manage delivery partners and tracking."""

    def assign_partner(self, order_id: str) -> DeliveryPartner:
        raise NotImplementedError

    def get_tracking(self, order_id: str) -> dict:
        return {"order_id": order_id, "eta_minutes": None}

    def calculate_eta(self, origin: str, destination: str) -> Optional[int]:
        """Return ETA in minutes."""
        return None
