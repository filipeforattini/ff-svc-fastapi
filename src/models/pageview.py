from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import Integer, String, Column, DateTime

from src.services.database import Base


class Pageview(Base):
    __tablename__ = 'pageviews'

    id = Column(Integer, primary_key=True)
    ip = Column(String(32))
    page = Column(String(64))
    query = Column(String(256))
    createdAt = Column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), default=datetime.now, server_default=func.now(), onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True))

    def __repr__(self) -> str:
        return f"Pageview(id={self.id!r})"

    def __init__(self, data):
        self.ip = data["ip"]
        self.page = data["page"]
        self.query = data["query"]
        super().__init__()
