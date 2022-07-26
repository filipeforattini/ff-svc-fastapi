from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.lead import Lead
from src.services.database import EngineMysql

router = APIRouter()


@router.get("/leads")
async def read_users():
    with Session(EngineMysql) as session:
        stmt = select(Lead)
        return session.scalar(stmt)


@router.get("/leads/{id}")
async def read_user(id: str):
    return {"id": id}
