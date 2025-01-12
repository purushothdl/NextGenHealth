from typing import List
from app.repositories.feedback_repository import FeedbackRepository
from app.schemas.feedback_schemas import Feedback
from datetime import datetime
import uuid

class FeedbackService:
    def __init__(self, feedback_repository: FeedbackRepository):
        self.feedback_repository = feedback_repository

    async def add_feedback(
        self, rating: int, comment: str, user_id: str, user_role: str
    ) -> Feedback:
        # Create a new feedback object
        feedback = Feedback(
            feedback_id=str(uuid.uuid4()),
            user_id=user_id,
            user_role=user_role,
            rating=rating,
            comment=comment,
            timestamp=datetime.utcnow(),
        )
        # Save the feedback
        await self.feedback_repository.add_feedback(feedback)
        return feedback

    async def get_feedback_by_user(self, user_id: str) -> List[Feedback]:
        return await self.feedback_repository.get_feedback_by_user(user_id)

    async def get_all_feedback(self) -> List[Feedback]:
        return await self.feedback_repository.get_all_feedback()