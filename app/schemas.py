from pydantic import BaseModel
from typing import List, Optional

class IssueCreate(BaseModel):
    title: str
    description: Optional[str] = None
    assignee_id: int


class IssueUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    version: int


class CommentCreate(BaseModel):
    body: str
    author_id: int


class LabelCreate(BaseModel):
    names: List[str]
