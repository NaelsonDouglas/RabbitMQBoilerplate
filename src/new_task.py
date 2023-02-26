#!/usr/bin/env python
import pika
import sys

import channel_configs

message = ' '.join(sys.argv[1:]) or 'Hello World!'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=channel_configs.HOST))
channel = connection.channel()

channel.queue_declare(queue=channel_configs.QUEUE, durable=True)

channel.basic_publish(
                        exchange='',
                        routing_key=channel_configs.QUEUE,
                        body=message,
                        properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
                    )
print(' [x] Sent %r' % message)
connection.close()