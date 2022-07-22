import pika
from decouple import config

RABBITMQ_CONNECTION_STRING = config('RABBITMQ_CONNECTION_STRING', False)


def client_factory():
    connection = pika.BlockingConnection(
        pika.URLParameters(RABBITMQ_CONNECTION_STRING))
    return connection.channel()
