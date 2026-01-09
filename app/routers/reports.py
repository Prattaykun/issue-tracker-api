from fastapi import APIRouter
from sqlalchemy import func
from app.database import SessionLocal
from app import models

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/top-assignees")
def top_assignees():
    db = SessionLocal()
    result = db.query(models.Issue.assignee_id, func.count()).group_by(models.Issue.assignee_id).all()
    return result
