# Calories-Alert-Kafka
Simple alert system implemented in Kafka and Python. The code in this repo is the part of the blog post [Getting started with Apache Kafka in Python](http://blog.adnansiddiqi.me/getting-started-with-apache-kafka-in-python/)

**Recipes Alert System in Kafka**
The system we are going to build is an alert system which will send notification about the recipes if it meets the certain threshold of the calories. There will be two topics:

*\# raw_recipes:-* It will be storing the raw HTML of each recipe. The idea is to use this topic as the main source of our data that later can be processed and transformed as per need.
*\# parsed_recipes:-*  As the name suggests, this will be parsed data of each recipe in JSON format.
The length of Kafka topic name should not exceed 249.

A typical workflow look like this:
![alt text](http://blog.adnansiddiqi.me/wp-content/uploads/2018/06/recipe-alert-system-kafka.png)

*Raw recipe producer*
The first program we are going to write is the producer. It will access Allrecpies.com and fetch the raw HTML  and store in raw_recipes topic.
![](https://github.com/samirsahoo007/bigdata/blob/master/kafka/Calories-Alert-Kafka/producer-raw-recipies.py)
