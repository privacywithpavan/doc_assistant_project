from typing import List, Literal
from pydantic import BaseModel, Field
from datetime import datetime


class AnswerResponse(BaseModel):
    """This schema ensures consistent formatting of answers and tracks which documents were referenced."""

    question: str = Field(description="The original user question")
    answer: str = Field(description="The generated answer")
    sources: List[str] = Field(description="List of source document IDs used")
    confidence: float = Field(description="Confidence score between 0 and 1")
    timestamp: datetime = Field(description="When the response was generated")


class UserIntent(BaseModel):
    """This schema helps the system understand what type of request the user is making and route it to the appropriate agent."""

    intent_type: Literal["qa", "summarization", "calculation", "unknown"] = Field(
        description="The classified intent"
    )
    confidence: float = Field(
        description="Confidence in classification, score between 0 and 1"
    )
    reasoning: str = Field(description="Explanation for the classification")
