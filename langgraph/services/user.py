from typing import List, Optional
from ..models import CustomerProfile, Address


class UserService:
    """Customer profile and address management."""

    def get_profile(self, customer_id: str) -> Optional[CustomerProfile]:
        return None

    def update_profile(self, profile: CustomerProfile) -> None:
        raise NotImplementedError

    def list_addresses(self, customer_id: str) -> List[Address]:
        return []

    def add_address(self, address: Address) -> None:
        raise NotImplementedError
