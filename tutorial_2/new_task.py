import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Message saved to disk
channel.queue_declare(queue='task_queue', durable=True)

# Dont dispatch new message to a worker until it has processed and ack the previous, 
# Dispatch it to non busy worker
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange = '',
    routing_key = 'task_queue',
    body = message,
    properties=pika.BasicProperties(
        delivery_mode=2,
    )
)

print('[x] Sent %r' % message)
connection.close()