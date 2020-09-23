import pika
credentials = pika.PlainCredentials('mqadmin', 'Admin123XX_')
parameters = pika.ConnectionParameters('localhost','5672','/',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()