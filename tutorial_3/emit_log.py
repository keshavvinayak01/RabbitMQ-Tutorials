import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Message saved to disk

# Dont dispatch new message to a worker until it has processed and ack the previous, 
# Dispatch it to non busy worker
message = ' '.join(sys.argv[1:]) or "Hello World"

channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'
)

channel.basic_publish(
    exchange='logs',
    routing_key='',
    body = message
)
print(" [x] Sent %r" % message)
connection.close()