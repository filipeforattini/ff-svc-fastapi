from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.pageview import Pageview
from src.services.database import EnginePostgres

router = APIRouter()


@router.get("/pageviews")
async def read_users():
    with Session(EnginePostgres) as session:
        stmt = select(Pageview)\
            .limit(25)\
            .offset(1)
        return session.execute(stmt).fetchall()


@router.get("/pageviews/{id}")
async def read_user(id: str):
    return {"id": id}
