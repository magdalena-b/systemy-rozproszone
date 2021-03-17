#!/usr/bin/env python
import pika

# Producer

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host = 'localhost')
)

channel = connection.channel()
channel.queue_declare(queue = 'h')
channel.basic_publish(exchange = '', routing_key = 'h', body = 'h alo halo')
channel.close()

