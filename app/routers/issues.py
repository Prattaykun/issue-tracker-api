from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter(prefix="/issues", tags=["Issues"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("")
def create_issue(issue: schemas.IssueCreate, db: Session = Depends(get_db)):
    new_issue = models.Issue(**issue.dict())
    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)
    return new_issue

@router.patch("/{issue_id}")
def update_issue(issue_id: int, data: schemas.IssueUpdate, db: Session = Depends(get_db)):
    issue = db.query(models.Issue).filter(models.Issue.id == issue_id).first()
    if not issue:
        raise HTTPException(status_code=404, detail="Issue not found")

    if issue.version != data.version:
        raise HTTPException(status_code=409, detail="Version conflict")

    for key, value in data.dict(exclude={"version"}).items():
        if value is not None:
            setattr(issue, key, value)

    issue.version += 1
    db.commit()
    return issue
@router.post("/{issue_id}/comments")
def add_comment(issue_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    if not comment.body.strip():
        raise HTTPException(status_code=400, detail="Empty comment")

    new_comment = models.Comment(issue_id=issue_id, **comment.dict())
    db.add(new_comment)
    db.commit()
    return new_comment
@router.post("/bulk-status")
def bulk_status(issue_ids: list[int], status: str, db: Session = Depends(get_db)):
    try:
        for issue_id in issue_ids:
            issue = db.query(models.Issue).get(issue_id)
            if issue.status == "closed":
                raise Exception("Invalid issue")
            issue.status = status
        db.commit()
    except:
        db.rollback()
        raise HTTPException(status_code=400, detail="Transaction failed")

    return {"updated": len(issue_ids)}
import pandas as pd
from fastapi import UploadFile

@router.post("/import")
def import_csv(file: UploadFile, db: Session = Depends(get_db)):
    df = pd.read_csv(file.file)
    success, failed = 0, []

    for index, row in df.iterrows():
        if not row.get("title"):
            failed.append(f"Row {index}: missing title")
            continue
        db.add(models.Issue(title=row["title"], assignee_id=row["assignee_id"]))
        success += 1

    db.commit()
    return {"inserted": success, "failed": failed}
