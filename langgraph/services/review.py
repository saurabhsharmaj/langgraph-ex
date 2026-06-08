from typing import List
from ..models import Review


class ReviewService:
    """Manage user reviews and ratings."""

    def add_review(self, review: Review) -> Review:
        raise NotImplementedError

    def get_reviews_for_target(self, target_id: str) -> List[Review]:
        return []
