from typing import List, Dict, Any


class SearchService:
    """Semantic search and recommendation engine stubs."""

    def semantic_search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        return []

    def recommend(self, customer_id: str, limit: int = 10) -> List[Dict[str, Any]]:
        return []

    def popular_foods(self, limit: int = 10) -> List[Dict[str, Any]]:
        return []
