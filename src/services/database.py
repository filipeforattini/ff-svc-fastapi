from decouple import config
from sqlalchemy.orm import registry
from sqlalchemy.pool import QueuePool
from sqlalchemy import text, create_engine, __version__

print("app :: sqlalchemy version", __version__)

# constants
POSTGRES_CONNECTION_STRING = config('POSTGRES_CONNECTION_STRING', False)

# singletons
Engine = create_engine(POSTGRES_CONNECTION_STRING,
                       echo=False, future=True, poolclass=QueuePool, pool_pre_ping=True)

mapper_registry = registry()
mapper_registry.metadata
Base = mapper_registry.generate_base()

def sync():
    Base.metadata.create_all(Engine)