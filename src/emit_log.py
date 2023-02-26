#!/usr/bin/env python
import pika
import sys
import channel_configs

connection = pika.BlockingConnection(pika.ConnectionParameters(host=channel_configs.HOST))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()