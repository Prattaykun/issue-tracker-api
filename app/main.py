from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import issues, reports

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Issue Tracker API")

app.include_router(issues.router)
app.include_router(reports.router)
