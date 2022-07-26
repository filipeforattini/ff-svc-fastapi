from decouple import config
from sqlalchemy.orm import registry
from sqlalchemy.pool import QueuePool
from sqlalchemy import text, create_engine, __version__

print("app :: sqlalchemy version", __version__)

# constants
MYSQL_CONNECTION_STRING = config('MYSQL_CONNECTION_STRING', False)
POSTGRES_CONNECTION_STRING = config('POSTGRES_CONNECTION_STRING', False)

# singletons
EngineMysql = create_engine(MYSQL_CONNECTION_STRING,
                            echo=False, future=True, poolclass=QueuePool, pool_pre_ping=True)

EnginePostgres = create_engine(POSTGRES_CONNECTION_STRING,
                               echo=False, future=True, poolclass=QueuePool, pool_pre_ping=True)

mapper_registry = registry()
mapper_registry.metadata
Base = mapper_registry.generate_base()


def syncMysql():
    Base.metadata.create_all(EngineMysql)


def syncPostgres():
    Base.metadata.create_all(EnginePostgres)
