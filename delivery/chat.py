def delivery_report(err, msg):
    # to indicate err incase any
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    # to indicate delivery message 
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# server: localhost:9092