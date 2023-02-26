#!/usr/bin/env python
import pika
import time
import channel_configs

connection = pika.BlockingConnection(pika.ConnectionParameters(host=channel_configs.HOST))
channel = connection.channel()

channel.queue_declare(queue=channel_configs.QUEUE, durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=channel_configs.QUEUE, on_message_callback=callback, auto_ack=False)

channel.start_consuming()