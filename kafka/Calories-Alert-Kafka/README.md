# Calories-Alert-Kafka
Simple alert system implemented in Kafka and Python. The code in this repo is the part of the blog post [Getting started with Apache Kafka in Python](http://blog.adnansiddiqi.me/getting-started-with-apache-kafka-in-python/)

**Recipes Alert System in Kafka**
The system we are going to build is an alert system which will send notification about the recipes if it meets the certain threshold of the calories. There will be two topics:

*\# raw_recipes:-* It will be storing the raw HTML of each recipe. The idea is to use this topic as the main source of our data that later can be processed and transformed as per need.
*\# parsed_recipes:-*  As the name suggests, this will be parsed data of each recipe in JSON format.
The length of Kafka topic name should not exceed 249.

A typical workflow look like this:
![alt text](http://blog.adnansiddiqi.me/wp-content/uploads/2018/06/recipe-alert-system-kafka.png)

*Raw recipe producer: producer-raw-recipies.py*
fetch_raw() and get_recipes() methods: The first program we are going to write is the producer. It will access Allrecpies.com and fetch the raw HTML  and store in raw_recipes topic.

The above methods will extract markup of each recipe and return in list format.

Next, we to create a producer object. Before we proceed further, we will make changes in config/server.properties file. We have to set advertised.listeners to PLAINTEXT://localhost:9092 otherwise you could experience the following error:

Error encountered when producing to broker b'adnans-mbp':9092. Retrying.

We will now add two methods:connect_kafka_producer() that will give you an instance of Kafka producer and publish_message() that will just dump the raw HTML of individual recipes.

If it runs well, it shows the following output:

/anaconda3/anaconda/bin/python /Development/DataScience/Kafka/kafka-recipie-alert/producer-raw-recipies.py
Accessing list
Processing..https://www.allrecipes.com/recipe/20762/california-coleslaw/
Processing..https://www.allrecipes.com/recipe/8584/holiday-chicken-salad/
Processing..https://www.allrecipes.com/recipe/80867/cran-broccoli-salad/
Message published successfully.
Message published successfully.
Message published successfully.
 
Process finished with exit code 0

I am using a GUI tool, named as Kafka Tool to browse recently published messages. It is available for OSX, Windows and Linux.

![alt text](http://blog.adnansiddiqi.me/wp-content/uploads/2018/06/Screen-Shot-2018-06-10-at-4.45.57-PM.png)

*Recipe Parser: producer_consumer_parse_recipes.py*
The next script we are going to write will serve as both consumer and producer. First it will consume data from raw_recipes topic, parse and transform data into JSON and then will publish it in parsed_recipes topic. Below is the code that will fetch HTML data from raw_recipes topic, parse and then feed into parsed_recipes topic.

KafkaConsumer accepts a few parameters beside the topic name and host address. By providing auto_offset_reset='earliest' you are telling Kafka to return messages from the beginning. The parameter consumer_timeout_ms helps the consumer to disconnect after the certain period of time. Once disconnected, you can close the consumer stream by calling consumer.close()

After this, I am using same routines to connect producers and publish parsed data in the new topic. KafaTool browser gives glad tidings about newly stored messages.

![alt text](http://blog.adnansiddiqi.me/wp-content/uploads/2018/06/Screen-Shot-2018-06-10-at-7.05.31-PM.png)

So far so good. We stored recipes in both raw and JSON format for later use. Next, we have to write a consumer that will connect with parsed_recipes topic and generate alert if certain calories critera meets.
consumer-notification.py: The JSON is decoded and then check the calories count, a notification is issued once the criteria meet.

