# libs
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from src.routers import leads, pageviews
import threading

# app
from src.services import database, consumer, producer

def start():
    print('app :: starting ')
    print('database :: sync', database.sync())

    app = FastAPI()
    app.include_router(leads.router)
    app.include_router(pageviews.router)

    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="Custom title",
            version="2.5.0",
            description="This is a very custom OpenAPI schema",
            routes=app.routes,
        )
        openapi_schema["info"]["x-logo"] = {
            "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
        }
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    app.openapi = custom_openapi

    # t1 = threading.Thread(target=producer.loop)
    # t1.start()

    # t2 = threading.Thread(target=consumer.loop)
    # t2.start()

    print('app :: start finished! ')
    return app
