from sqlalchemy import Integer, String, Column

from src.services.database import Base


class Pageview(Base):
    __tablename__ = 'pageviews'

    id = Column(Integer, primary_key=True)
    ip = Column(String(64))
    page = Column(String(64))
    query = Column(String(64))

    def __repr__(self) -> str:
        return f"Pageview(id={self.id!r})"

    def __init__(self, data):
        self.ip = data["ip"]
        self.page = data["page"]
        self.query = data["query"]
        super().__init__()
