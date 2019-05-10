from time import sleep
from json import dumps
from kafka import KafkaProducer

KAFKA_VERSION = (0, 10)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],   # : sets the host and port. The producer should contact to bootstrap initial cluster metadata. It is not necessary to set this here, since the default is *localhost:9092*.
                         api_version=KAFKA_VERSION,
                         value_serializer=lambda x: dumps(x).encode('utf-8')) # function of how the data should be serialized before sending to the broker. Here, we convert the data to a json file and encode it to utf-8.

for e in range(1000):                           # Now, we want to generate numbers from one till 1000.
    data = {'number' : e}
    producer.send('numtest', value=data)
    sleep(5)
