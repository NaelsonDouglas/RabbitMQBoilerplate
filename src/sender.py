#https://www.rabbitmq.com/tutorials/tutorial-one-python.html

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='queue')
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
connection.close()
