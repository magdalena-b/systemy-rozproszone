#!/usr/bin/env python
import pika

# Consumer - odbiera zlecenia
# Dostawca posiada liste dostepnych produktow
# 1. dostawca -> tlen, buty; 2. dostawca -> tlen, plecak

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host = 'localhost')
)

channel = connection.channel()
channel.queue_declare(queue = 'Everest')
channel.basic_publish(exchange = '', routing_key = 'halo', body = 'halo wieje halny')
channel.close()

