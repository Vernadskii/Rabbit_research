from contextlib import contextmanager
import pika
from pika.credentials import PlainCredentials

USER = "guest"
PASSWORD = "guest"
HOST = "localhost"
PORT = 5672
EXCHANGE_TYPE = 'direct'
EXCHANGE = "my-first-exchange"
ROUTING_KEY = "my-key"


def declare_exchange(channel):
    """Declare exchange if not already created."""
    channel.exchange_declare(exchange=EXCHANGE, exchange_type=EXCHANGE_TYPE, durable=True)


@contextmanager
def get_channel():
    credentials = PlainCredentials(
        username=USER,
        password=PASSWORD,
    )
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=HOST,
            port=PORT,
            credentials=credentials,
        )
    )
    print("Connection to the RabbitMQ server is successful")
    yield connection.channel()
    connection.close()
    print("Connection to RabbitMQ server closed successfully")
