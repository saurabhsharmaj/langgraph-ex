from typing import Dict


class BillingService:
    """Bill generation, tax calculation, and payment processing."""

    def generate_bill(self, order_id: str) -> Dict:
        raise NotImplementedError

    def calculate_tax(self, amount: float) -> float:
        raise NotImplementedError

    def process_payment(self, order_id: str, payment_info: Dict) -> Dict:
        raise NotImplementedError
