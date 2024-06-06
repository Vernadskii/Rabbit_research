import sys
from connection import get_channel, EXCHANGE, ROUTING_KEY, declare_exchange

QUEUE = "my-first-queue"


def callback(ch, method, properties, body):
    print(f" [+] Message received: {body.decode('utf-8')}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def prepare_rabbit(channel):
    declare_exchange(channel)

    # Declare the queue if it hasn't yet been created
    channel.queue_declare(queue=QUEUE, durable=True)

    # Binding the queue to the exchanger
    channel.queue_bind(exchange=EXCHANGE, queue=QUEUE, routing_key=ROUTING_KEY)


def main():
    try:
        with get_channel() as channel:
            prepare_rabbit(channel)
            channel.basic_consume(
                queue=QUEUE,
                auto_ack=False,
                on_message_callback=callback,
            )
            print("Press Control+C to stop the application")
            channel.start_consuming()
    except Exception as e:
        print(f"An error occurred while receiving messages: {e}")
        sys.exit(0)
    except KeyboardInterrupt:
        print("Key combination has been pressed to exit the application")
        channel.stop_consuming()
        sys.exit(0)


if __name__ == "__main__":
    main()
