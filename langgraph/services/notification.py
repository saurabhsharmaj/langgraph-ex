from typing import Dict, Any


class NotificationService:
    """Send notifications via SMS, Email, WhatsApp, Push."""

    def send_sms(self, to: str, message: str) -> Dict[str, Any]:
        raise NotImplementedError

    def send_email(self, to: str, subject: str, body: str) -> Dict[str, Any]:
        raise NotImplementedError

    def send_whatsapp(self, to: str, message: str) -> Dict[str, Any]:
        raise NotImplementedError

    def send_push(self, device_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError
