from sqlalchemy import Integer, String, Column

from src.services.database import Base


class Lead(Base):
    __tablename__ = 'leads'

    id = Column(Integer, primary_key=True)
    ip = Column(String(64))
    name = Column(String(64))
    mobile = Column(String(64))
    country = Column(String(64))
    state = Column(String(64))
    city = Column(String(64))
    address = Column(String(64))

    def __repr__(self) -> str:
        return f"Lead(id={self.id!r})"

    def __init__(self, data):
        self.ip = data["ip"]
        self.name = data["name"]
        self.mobile = data["mobile"]
        self.country = data["country"]
        self.state = data["state"]
        self.city = data["city"]
        self.address = data["address"]
        super().__init__()
