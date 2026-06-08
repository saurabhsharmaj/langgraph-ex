from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from .routes import get_service_registry
from .agent import Agent

app = FastAPI(title="LangGraph Food Services Skeleton")

services = get_service_registry()
agent = Agent(services)

CURL_EXAMPLES = [
    "curl http://localhost:8000/health",
    "curl http://localhost:8000/services",
    "curl http://localhost:8000/catalog/categories",
    "curl \"http://localhost:8000/catalog/menu?category_id=breakfast\"",
    "curl -X POST http://localhost:8000/order/create -H \"Content-Type: application/json\" -d '{\"customer_id\":\"cust-123\",\"items\":[\"item-1\",\"item-2\"]}'",
    "curl -X PUT http://localhost:8000/order/order-123/status -H \"Content-Type: application/json\" -d '{\"status\":\"completed\"}'",
    "curl http://localhost:8000/order/history/cust-123",
    "curl -X POST http://localhost:8000/agent/ask -H \"Content-Type: application/json\" -d '{\"prompt\":\"What can I order?\",\"context\":{\"customer_id\":\"cust-123\"}}'",
]


@app.get("/curl")
def curl_commands():
    return {"curl_commands": CURL_EXAMPLES}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/services")
def list_services():
    return {"services": list(services.keys())}


@app.get("/catalog/categories")
def list_categories():
    try:
        cats = services["catalog"].list_categories()
        return {"categories": [agent._to_primitive(c) for c in cats]}
    except NotImplementedError:
        raise HTTPException(status_code=501, detail="Catalog.list_categories not implemented")


@app.get("/catalog/menu")
def get_menu(category_id: str = None):
    try:
        items = services["catalog"].get_menu(category_id)
        return {"menu": [agent._to_primitive(i) for i in items]}
    except NotImplementedError:
        raise HTTPException(status_code=501, detail="Catalog.get_menu not implemented")


@app.post("/order/create")
async def create_order(request: Request):
    body = await request.json()
    try:
        order = services["order"].create_order(body.get("customer_id"), body.get("items", []))
        return {"order": agent._to_primitive(order)}
    except NotImplementedError:
        raise HTTPException(status_code=501, detail="Order.create_order not implemented")


@app.put("/order/{order_id}/status")
async def update_order_status(order_id: str, request: Request):
    body = await request.json()
    status = body.get("status")
    try:
        services["order"].update_order_status(order_id, status)
        return {"order_id": order_id, "status": status}
    except NotImplementedError:
        raise HTTPException(status_code=501, detail="Order.update_order_status not implemented")


@app.get("/order/history/{customer_id}")
def order_history(customer_id: str):
    try:
        orders = services["order"].get_order_history(customer_id)
        return {"orders": [agent._to_primitive(o) for o in orders]}
    except NotImplementedError:
        raise HTTPException(status_code=501, detail="Order.get_order_history not implemented")


@app.post("/agent/ask")
async def agent_ask(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    context = body.get("context", {})
    if not prompt:
        raise HTTPException(status_code=400, detail="prompt required")
    result = agent.handle_prompt(prompt, context=context)
    return JSONResponse(content=result)
