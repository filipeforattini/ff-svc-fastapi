from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import Integer, String, Column, DateTime

from src.services.database import Base


class Lead(Base):
    __tablename__ = 'leads'

    id = Column(Integer, primary_key=True)
    ip = Column(String(32))
    name = Column(String(64))
    email = Column(String(64))
    mobile = Column(String(64))
    country = Column(String(32))
    state = Column(String(32))
    city = Column(String(64))
    address = Column(String(256))
    createdAt = Column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), default=datetime.now, server_default=func.now(), onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True))

    def __repr__(self) -> str:
        return f"Lead(id={self.id!r})"

    def __init__(self, data):
        self.ip = data["ip"]
        self.name = data["name"]
        self.email = data["email"]
        self.mobile = data["mobile"]
        self.country = data["country"]
        self.state = data["state"]
        self.city = data["city"]
        self.address = data["address"]
        super().__init__()
