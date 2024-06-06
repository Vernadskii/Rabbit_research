# RabbitMQ Message Queue Example

This project demonstrates the use of RabbitMQ for message queuing in a simple producer-consumer scenario. It contains two main scripts: `consumer.py`, which listens for messages on a specified queue, and `producer.py`, which sends messages to the queue. Additionally, there's a `connection.py` script that handles the connection to the RabbitMQ server, and a `docker-compose.yml` file to run RabbitMQ in a Docker container.

## Quick Start

### Prerequisites

- Python 3.x
- Docker and Docker Compose installed (for running RabbitMQ server)
- pika (Python library for RabbitMQ)

### Setting up RabbitMQ with Docker

1. Run RabbitMQ using Docker Compose:
   ```bash
   docker-compose up -d
   ```
   This will start a RabbitMQ server accessible on port `5672` with management UI on port `15672`. Default user and password are both set to "guest".

### Installing Dependencies

Install the necessary Python package by running:

```bash
pip install -r requirement.txt
```

### Running the Producer

Run the producer script to send messages:

```bash
python producer.py
```
Enter your message at the prompt. To quit, type 'q'.

### Running the Consumer

Open another terminal and run the consumer script to receive messages:

```bash
python consumer.py
```

Press `Ctrl + C` to stop the consumer application.

## Files Description

- `consumer.py`: Listens for messages on a predefined RabbitMQ queue (`my-first-queue`) and prints them out.
- `producer.py`: Sends a user-input message to the RabbitMQ exchange (`my-first-exchange`) with a specific routing key (`my-key`).
- `connection.py`: Contains the RabbitMQ connection settings and a context manager for managing the connection to the RabbitMQ server.
- `docker-compose.yml`: Defines the RabbitMQ service and related configurations to run it as a Docker container.

## Usage

After running both the producer and consumer scripts, you can type messages into the producer's prompt. These messages will be sent to the RabbitMQ queue and then printed out by the consumer script when received.

## Notes

- The `QUEUE`, `EXCHANGE`, and `ROUTING_KEY` are hardcoded in this example. For production use, consider making these configurable.
- The RabbitMQ credentials should not be hardcoded for production uses. Use environment variables or a configuration file.
- Ensure the RabbitMQ server is running before executing `producer.py` or `consumer.py`.
- If you encounter any connection issues, make sure the RabbitMQ service is properly started and the ports are correctly mapped.
