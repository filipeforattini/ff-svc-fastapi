import json
from sqlalchemy.orm import Session

from src.models.lead import Lead
from src.models.pageview import Pageview
from src.services.database import EnginePostgres, EngineMysql
from src.services.rabbitmq import client_factory


def savePageview(ch, method, properties, body):
    print('pageview  |', body)
    body = json.loads(str(body.decode("utf-8")))
    pageview = Pageview(body)
    with Session(EnginePostgres) as session:
        session.add(pageview)
        session.commit()


def saveLead(ch, method, properties, body):
    print('lead      |', body)
    body = json.loads(str(body.decode("utf-8")))
    lead = Lead(body)
    with Session(EngineMysql) as session:
        session.add(lead)
        session.commit()


def loop():
    client = client_factory()
    client.basic_consume(queue='pageviews.new',
                         on_message_callback=savePageview, auto_ack=True)

    client.basic_consume(queue='leads.new',
                         on_message_callback=saveLead, auto_ack=True)

    client.basic_qos(prefetch_count=10)
    client.start_consuming()
