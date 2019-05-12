import threading
import logging
import time
import json
from kafka import KafkaConsumer, KafkaProducer

# You can send and receive strings if you remove the value_serializer and value_deserializer from the code below.
class Producer(threading.Thread):
    daemon = True
    def run(self):
        producer = KafkaProducer(bootstrap_servers='localhost:6667',
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        while True:
            producer.send('my-topic', {"dataObjectID": "test1"})
            producer.send('my-topic', {"dataObjectID": "test2"})
            time.sleep(1)

class Consumer(threading.Thread):
    daemon = True
    def run(self):
        consumer = KafkaConsumer(bootstrap_servers='localhost:6667',
                                 auto_offset_reset='earliest',
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        consumer.subscribe(['my-topic'])
        for message in consumer:
            print (message)

def main():
    threads = [
        Producer(),
        Consumer()
    ]
    for t in threads:
        t.start()
    time.sleep(10)
if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:' +
               '%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()

'''
Output: You can see the message has been shared between producer and consumer.
2017-11-19 02:18:30,590.590.334892273:kafka.client:140662616688384:INFO:20867:Bootstrap succeeded: found 1 brokers and 11 topics.
2017-11-19 02:18:30,694.694.561004639:kafka.conn:140662625081088:INFO:20867:Broker version identifed as 0.10.0
2017-11-19 02:18:30,694.694.842100143:kafka.conn:140662625081088:INFO:20867:Set configuration api_version=(0, 10, 0) to skip auto check_version requests on startup
2017-11-19 02:18:30,728.728.385925293:kafka.conn:140662616688384:INFO:20867:Broker version identifed as 0.10.0
2017-11-19 02:18:30,728.728.656053543:kafka.conn:140662616688384:INFO:20867:Set configuration api_version=(0, 10, 0) to skip auto check_version requests on startup
2017-11-19 02:18:30,730.730.935096741:kafka.coordinator.consumer:140662616688384:WARNING:20867:group_id is None: disabling auto-commit.
2017-11-19 02:18:30,731.731.933116913:kafka.consumer.subscription_state:140662616688384:INFO:20867:Updating subscribed topics to: ['my-topic']
2017-11-19 02:18:30,738.738.305091858:kafka.consumer.subscription_state:140662616688384:INFO:20867:Updated partition assignment: [TopicPartition(topic='my-topic', partition=0)]
ConsumerRecord(topic=u'my-topic', partition=0, offset=0, timestamp=1511075143446, timestamp_type=0, key=None, value={u'dataObjectID': u'test1'}, checksum=922149137, serialized_key_size=-1, serialized_value_size=25)
I am Getting this>>>>
ConsumerRecord(topic=u'my-topic', partition=0, offset=1, timestamp=1511075143447, timestamp_type=0, key=None, value={u'dataObjectID': u'test2'}, checksum=271715966, serialized_key_size=-1, serialized_value_size=25)
I am Getting this>>>>
ConsumerRecord(topic=u'my-topic', partition=0, offset=2, timestamp=1511075144449, timestamp_type=0, key=None, value={u'dataObjectID': u'test1'}, checksum=2115924298, serialized_key_size=-1, serialized_value_size=25)
I am Getting this>>>>
ConsumerRecord(topic=u'my-topic', partition=0, offset=3, timestamp=1511075144449, timestamp_type=0, key=None, value={u'dataObjectID': u'test2'}, checksum=2086194963, serialized_key_size=-1, serialized_value_size=25)
'''
