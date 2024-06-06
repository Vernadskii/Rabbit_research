import sys
from connection import get_channel, EXCHANGE, ROUTING_KEY, declare_exchange


def send_message(message: str):
    try:
        with get_channel() as channel:
            declare_exchange(channel)
            channel.basic_publish(
                exchange=EXCHANGE,
                routing_key=ROUTING_KEY,
                body=message,
            )
            print(f" [+] Message '{message}' sent successfully")
    except Exception as e:
        print(f"There was an error sending the message: {e}")


def main():
    while True:
        message = input("Enter text for message or 'q' to exit:\n")
        if message == "q":
            sys.exit(0)
        send_message(message=message)


if __name__ == "__main__":
    main()
