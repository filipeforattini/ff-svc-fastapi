import json
import time
import random
import schedule
from faker import Faker

from src.services.rabbitmq import client_factory


faker = Faker()


def randomPageview():
    pageview = dict()
    pageview["ip"] = faker.ipv4_public()
    pageview["page"] = faker.hostname()
    pageview["query"] = "?q=" + faker.word()
    return pageview


def randomLead():
    lead = dict()
    lead["name"] = faker.name()
    lead["mobile"] = faker.phone_number()
    lead["country"] = faker.country()
    lead["state"] = faker.country_code()
    lead["city"] = faker.city()
    lead["address"] = faker.address()
    return lead


def run(client):
    pageview = randomPageview()
    client.basic_publish(exchange='pageviews',
                         routing_key='new',
                         body=json.dumps(pageview, separators=(',', ':')))
    if (random.randint(0, 10) == 0):
        lead = randomLead()
        lead["ip"] = pageview["ip"]
        client.basic_publish(exchange='leads',
                             routing_key='new',
                             body=json.dumps(lead, separators=(',', ':')))


def loop():
    client = client_factory()

    client.exchange_declare('pageviews', exchange_type='fanout')
    client.queue_declare('pageviews.new')
    client.queue_bind(exchange='pageviews', routing_key='new',
                      queue='pageviews.new')

    client.exchange_declare('leads', exchange_type='fanout')
    client.queue_declare('leads.new')
    client.queue_bind(exchange='leads', routing_key='new', queue='leads.new')

    def secondly():
        run(client)

    schedule.every(1).seconds.do(secondly)

    while True:
        schedule.run_pending()
        time.sleep(1)
