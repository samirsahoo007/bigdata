from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

KAFKA_VERSION = (0, 10)

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',   # It handles where the consumer restarts reading after breaking down or being turned off and can be set either to *earliest* or *latest*. When
                                     # set to *latest*, the consumer starts reading at the end of the log. When set to *earliest*, the consumer starts reading at the latest committed offset.
     enable_auto_commit=True,        # makes sure the consumer commits its read offset every interval.

     auto_commit_interval_ms=1000ms,  #sets the interval between two commits. Since messages are coming in every five second, committing every second seems fair.

     group_id='my-group',
     api_version=KAFKA_VERSION,
     value_deserializer=lambda x: loads(x.decode('utf-8')))

client = MongoClient('localhost:27017')
collection = client.numtest.numtest

for message in consumer:
    message = message.value
    collection.insert_one(message)
    print('{} added to {}'.format(message, collection))
