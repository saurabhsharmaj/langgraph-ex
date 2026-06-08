# LangGraph Service Skeleton

This folder contains a lightweight skeleton for a food-ordering platform split
into logical services. The goal is to provide a starting point so each service
can be implemented and wired into a web framework or message bus.

Structure:
- `models.py` — small dataclasses for DTOs used across services.
- `services/` — individual service modules with class-based stubs:
  - `catalog.py`, `order.py`, `kitchen.py`, `user.py`, `delivery.py`,
    `notification.py`, `billing.py`, `review.py`, `search.py`, `promo.py`.
- `routes.py` — simple registry returning service instances.

Next steps:
- Implement storage (DB) or adapters for each service.
- Optionally expose the services with FastAPI/Flask or an RPC layer.
- Add tests that exercise the service stubs and expected interfaces.

python -m venv vlanggraph
vlanggraph\Scripts\activate


pip install -U langgraph


uvicorn langgraph.main:app --reload --host 127.0.0.1 --port 8000

python -m uvicorn langgraph.main:app --reload --host 127.0.0.1 --port 8000

curl http://127.0.0.1:8000/health

curl -X POST http://127.0.0.1:8000/agent/ask \
  -H 'Content-Type: application/json' \
  -d '{"prompt":"Create order 1x Classic Burger, 2x Veggie Pizza","context":{"customer_id":"cust1"}}'