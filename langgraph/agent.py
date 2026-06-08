import os
import re
from enum import Enum
from typing import Any, Dict, Optional


class LLMParser:
    """Pluggable parser that can be replaced with a Groq/LLM-based parser.

    The default implementation is a lightweight regex-based intent extractor
    for demo purposes. Replace `parse` with a call to your LLM/Groq parser
    when you have credentials and want richer parsing.
    """

    def parse(self, prompt: str) -> Dict[str, Any]:
        p = prompt.lower()
        # Simple intent detection rules
        if "create order" in p or "place order" in p or re.search(r"order\b", p):
            # naive item extraction: look for words like '1x burger' or 'burger'
            items = re.findall(r"(\d+)x\s*([a-zA-Z ]+)|([a-zA-Z ]+?)\b(?=,|$)", prompt)
            parsed_items = []
            for g in items:
                qty = g[0] or "1"
                name = g[1] or g[2]
                if name:
                    parsed_items.append({"name": name.strip(), "quantity": int(qty)})
            return {"intent": "create_order", "items": parsed_items}

        if "categories" in p or "menu" in p or "list" in p:
            return {"intent": "list_menu"}

        if "availability" in p or "available" in p or "in stock" in p:
            m = re.search(r"for ([a-zA-Z ]+)", prompt)
            return {"intent": "check_availability", "item": (m.group(1).strip() if m else None)}

        if "assign chef" in p or "assign a chef" in p:
            return {"intent": "assign_chef", "order_id": None}

        if "eta" in p or "estimate" in p:
            return {"intent": "calculate_eta"}

        if "apply coupon" in p or "coupon" in p:
            m = re.search(r"code[: ]?(\w+)", prompt, re.IGNORECASE)
            return {"intent": "apply_coupon", "code": (m.group(1) if m else None)}

        # fallback
        return {"intent": "unknown", "text": prompt}


class Agent:
    def __init__(self, services: Dict[str, Any], parser: Optional[LLMParser] = None):
        self.services = services
        self.parser = parser or LLMParser()

    def _to_primitive(self, o: Any) -> Any:
        """Recursively convert dataclasses/enums to primitives for JSON serialization."""
        if o is None:
            return None
        if isinstance(o, (str, int, float, bool)):
            return o
        if isinstance(o, Enum):
            return o.value
        if isinstance(o, dict):
            return {k: self._to_primitive(v) for k, v in o.items()}
        if isinstance(o, (list, tuple, set)):
            return [self._to_primitive(v) for v in o]
        if hasattr(o, "__dict__"):
            return {k: self._to_primitive(v) for k, v in o.__dict__.items()}
        try:
            return str(o)
        except Exception:
            return None

    def handle_prompt(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        parsed = self.parser.parse(prompt)
        intent = parsed.get("intent")

        if intent == "create_order":
            items = parsed.get("items", [])
            # map item names to item ids using catalog (naive match)
            catalog = self.services.get("catalog")
            menu = catalog.get_menu()
            resolved = []
            for it in items:
                name = it.get("name")
                qty = it.get("quantity", 1)
                match = next((m for m in menu if name.lower() in m.name.lower()), None)
                if match:
                    resolved.append({"item_id": match.id, "quantity": qty})
            # require customer_id in context
            customer_id = (context or {}).get("customer_id") or "guest"
            order_service = self.services.get("order")
            try:
                order = order_service.create_order(customer_id, resolved)
                return {"status": "ok", "action": "create_order", "order": self._to_primitive(order)}
            except Exception as e:
                return {"status": "error", "error": str(e)}

        if intent == "list_menu":
            menu = self.services.get("catalog").get_menu()
            return {"status": "ok", "menu": [self._to_primitive(m) for m in menu]}

        if intent == "check_availability":
            item = parsed.get("item")
            if not item:
                return {"status": "error", "error": "no item specified"}
            menu = self.services.get("catalog").get_menu()
            match = next((m for m in menu if item.lower() in m.name.lower()), None)
            if not match:
                return {"status": "error", "error": "item not found"}
            avail = self.services.get("catalog").check_availability(match.id)
            return {"status": "ok", "item": self._to_primitive(match), "availability": self._to_primitive(avail)}

        if intent == "apply_coupon":
            code = parsed.get("code")
            if not code:
                return {"status": "error", "error": "no coupon code provided"}
            promo = self.services.get("promo")
            valid = promo.validate_coupon(code, context.get("order_id") if context else None)
            return {"status": "ok", "coupon": self._to_primitive(valid)}

        return {"status": "error", "error": "intent not handled", "parsed": parsed}
