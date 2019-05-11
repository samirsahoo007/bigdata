**Hello World In Kafka Using Python**

*This is our first guest post here at Timber. If you\'re interested in
writing for us, reach out* [*on
Twitter*](https://twitter.com/timberdotio)

This blog is for you if you\'ve ever wondered:

1 What is Kakfa?

2 Why do I need a streaming/queueing/messaging system?

3 What are the benefits?

4 How does it fit with my current backend?

*Just a disclaimer: we\'re a logging company here @ Timber. We\'d love
it if you tried out our product (it\'s seriously great!), but that\'s
all we\'re going to advertise our product \... you guys came here to
learn about Kafka and this guide won\'t disappoint.*

**What Is This Blog About?**

The title might have given it away, but we\'re going to show you what
Kafka is, help you understand the need for a tool like Kafka, and then
get started with it. We\'re believers that the best way to learn
something is to do it, so get out your terminal and your favorite code
editor and get ready.

**What Is Kafka? Why Should One Use It?**

In short, Kafka is a distributed streaming platform.

*Oh wait! What does that even mean?*

Imagine that you have a simple web application which consists of an
interactive UI, a web server, and a database.

![](https://github.com/samirsahoo007/bigdata/blob/master/kafka/images/streamingPlatform.jpg){width="6.6929757217847765in"
height="1.7155610236220473in"}

You need to record all the events such as clicks, requests, impressions
and searches that take place on your web application and store them for
computation, reporting, and analysis, each of which is done by separate
applications or services. A simple solution would be to store the data
in your database and connect all other applications and services to your
database.

![](https://github.com/samirsahoo007/bigdata/blob/master/kafka/images/beforeKafka.jpg){width="6.6929757217847765in"
height="7.446183289588801in"}

This might look simple, but you\'re not finished. There are multiple
challenges that can arise:

1 Events like clicks, requests, impressions and searches results in
high-frequency interaction/requests or data flow to your web server and
your primary database may not be equipped to scale seamlessly. This
could introduce a high latency as more and more events pour into the
server.

2 If you choose to store high-frequency data in database systems like
SQL or MongoDB, it would be hard to introduce and reconstruct a new
system or a database on all of the historical data. You lose the
flexibility to extend the capabilities of your system by introducing new
technologies.

3 What if you have data processing systems in place to process these
events to gain deeper insights? Since these systems wouldn\'t be capable
of handling high-frequency reads and you wouldn\'t have access to the
true source of data, it is practically impossible to experiment with
various data processing or machine learning algorithms on all of the
data.

4 Each application can follow its own data format, which means that you
will need systems for data transformations when there is the exchange of
data across these applications.

All these problems can be better addressed by bringing a streaming
platform like Kafka into the picture. A streaming platform is a system
that can perform the following:

1 Store a huge amount of data that can be persistent, checksummed and
replicated for fault tolerance

2 Process continuous flow of data (data streams) in real time across
systems

3 Allow applications to publish data or data streams independently and
agnostic to the application/service consuming it

*Interesting! How different is it from traditional databases?*

Although Kafka can store persistent data, it is NOT a database.

Kafka not only allows applications to push or pull a continuous flow of
data, but it also deals with processing them to build and support
real-time applications. This is different than performing CRUD
operations on passive data or running queries on traditional databases.

*That sounds convincing! But how does Kafka solve the above-mentioned
challenges and why would one need a system like this?*

Kafka is a distributed platform and built for scale, which means it can
handle sky-high frequency reads and writes & store huge volumes of data.
It ensures that the data is always reliable. It also supports strong
mechanisms for recovery from failures. Here are some of the key aspects
of why one should be using Kafka:

*Things to Note:*
- Apache Kafka is an open-source streaming platform that was initially built by LinkedIn. It was later handed over to Apache foundation and open sourced it in 2011.

- Apache Kafka is an open-source stream-processing software platform developed by the Apache Software Foundation, written in Scala and Java. The project aims to provide a unified, high-throughput, low-latency platform for handling real-time data feeds. Its storage layer is essentially a “massively scalable pub/sub message queue architected as a distributed transaction log,”[3] making it highly valuable for enterprise infrastructures to process streaming data. Additionally, Kafka connects to external systems (for data import/export) via Kafka Connect and provides Kafka Streams, a Java stream processing library.
![alt text](https://kafka.apache.org/11/images/kafka-apis.png)

**1. Simplify The Backend Architecture**

Look at how a complex architecture can be simplified and streamlined
with the help of Kafka

![](https://github.com/samirsahoo007/bigdata/blob/master/kafka/images/backend.jpg){width="6.6929757217847765in"
height="4.52173009623797in"}

**2. Universal Pipeline Of Data**

As you can see above, Kafka acts as a universal data pipeline across
multiple applications and services. This gives us two advantages. The
first one is data integration. We have all the data from different
systems residing at a single place, making Kafka a true source of data.
Any application can push data to this platform which can later be pulled
by another application. Secondly, Kafka makes it easy to exchange data
between applications. Since we have all the data in one place, we can
standardize the data format that we will be using for the platform which
can reduce our data transformations.

**3. Connects To Existing Systems**

Although Kafka allows you to have a standard data format, that does not
mean the applications do not require data transformations. This allows
us to reduce the overall number of data transformations in our
architecture, but there may be cases when we still require
transformations.

Consider connecting a legacy system to your architecture which does not
know about Kafka: In such cases, Kafka offers a framework called Kafka
Connect for us to connect to existing systems maintaining the universal
data pipeline.

**4. Process Data In Real-Time**

A real-time application usually requires a continuous flow of data which
can be processed immediately or within the current span of time with
reduced latency. Kafka Streams make it possible to build, package and
deploy applications without any need for separate stream processors or
heavy and expensive infrastructure.

These features allow Kafka to become the true source of data for your
architecture. This enables you to add new services and applications to
your existing infrastructure and allows you to rebuild existing
databases or migrate from legacy systems with less effort.

**Getting Started With Kafka**

**Installation**

Installing Kafka is a fairly simple process. Just follow the given steps
below:

1 Download the latest 1.1.0 release of
[Kafka](https://www.apache.org/dyn/closer.cgi?path=/kafka/1.1.0/kafka_2.11-1.1.0.tgz)

2 Un-tar the download using the following command: tar -xzf
kafka\_2.11-1.1.0.tgz

3 cd to Kafka directory to start working with it: cd kafka\_2.11-1.1.0

**Starting The Server**

Kafka makes use of a tool called ZooKeeper which is a centralized
service for a distributed environment like Kafka. It offers
configuration service, synchronization service, and a naming registry
for large distributed systems. You can read more about it
[here](https://zookeeper.apache.org/).

Thus, we need to first start the ZooKeeper server followed by the Kafka
server. This can be achieved using the following commands:

1

2

3

4

5

*\# Start ZooKeeper Server*

bin/zookeeper-server-start.sh config/zookeeper.properties

*\# Start Kafka Server*

bin/kafka-server-start.sh config/server.properties

**Understanding Kafka**

Here is a quick introduction to some of the core concepts of Kafka
architecture:

1 Simply put, Kafka is a distributed publish-subscribe messaging system that maintains feeds of messages in partitioned and replicated topics. 
In the simplest way there are three players in the Kafka ecosystem: producers, topics (run by brokers) and consumers.

2 Kafka stores a stream of records in categories called topics. Each
record consists of a key, value and a timestamp

3 Kafka works on the publish-subscribe pattern. 
  Producers produce messages to a topic of their choice. It is possible to attach a key to each message, in which case the producer guarantees that all messages with the same key will arrive to the same partition.
  Topics are logs that receive data from the producers and store them across their partitions. Producers always write new messages at the end of the log. In our example we can make abstraction of the partitions, since we’re working locally.
  Consumers read the messages of a set of partitions of a topic of their choice at their own pace. If the consumer is part of a consumer group, i.e. a group of consumers subscribed to the same topic, they can commit their offset. This can be important if you want to consume a topic in parallel with different consumers.

![alt text](https://github.com/samirsahoo007/bigdata/tree/master/kafka/images/kafka1.png)

The offset is the position in the log where the consumer last consumed or read a message. The consumer can then commit this offset to make the reading ‘official’. Offset committing can be done automatically in the background or explicitly. In our example we will commit automatically in the background.

![alt text](https://github.com/samirsahoo007/bigdata/tree/master/kafka/images/kafka2.png)

4 Alongside, Producer API and Consumer API, Kafka also offers Streams
API for an application to work as a stream processor and Connector API
through which we can connect Kafka to other existing applications and
data systems

**Architecture**

![alt text](https://github.com/samirsahoo007/bigdata/tree/master/kafka/images/kafkaPartitions.jpg)

As you can see, Kafka topics are divided into partitions. These topics
can be replicated across separate machines using brokers, which allows
consumers to read from a topic in parallel.

Each of these brokers has partitions which are leaders and those that
are replicas. This allows for an incredible level of fault tolerance
through your system. When the system is functioning normally, all reads
and writes to a topic go through the leader and the leader makes sure
that all the other brokers are updated.

If a broker fails, the system can automatically reconfigure itself so a
replica can take over as the new leader for that topic.

**Creating Kafka Topics**

Let us start by creating a sample Kafka topic with a single partition
and replica. This can be done using the following command:

bin/kafka-topics.sh \--create \--zookeeper localhost:2181
\--replication-factor 1 \--partitions 1 \--topic sample

Now, let us list down all of our Kafka topics to check if we have
successfully created our sample topic. We can make use of the list
command here:

bin/kafka-topics.sh \--list \--zookeeper localhost:2181

You can also make use of the describe topics command for more details on
a particular Kafka topic:

bin/kafka-topics.sh \--describe \--zookeeper localhost:2181 \--topic
sample

**Creating Producer And Consumer**

Creating a producer and consumer can be a perfect Hello, World! example
to learn Kafka but there are multiple ways through which we can achieve
it. Some of them are listed below:

1 Command line client provided as default by Kafka

2 [kafka-python](https://github.com/dpkp/kafka-python)

3 [PyKafka](https://github.com/Parsely/pykafka)

4
[confluent-kafka](https://github.com/confluentinc/confluent-kafka-python)

While these have their own set of advantages/disadvantages, we will be
making use of kafka-python in this blog to achieve a simple producer and
consumer setup in Kafka using python.

**Kafka With Python**

Before you get started with the following examples, ensure that you have
kafka-python installed in your system:

pip install kafka-python

**Kafka Consumer**

Enter the following code snippet in a python shell:

from kafka import KafkaConsumer

consumer = KafkaConsumer(\'sample\')

for message in consumer:

print (message)

**Kafka Producer**

Now that we have a consumer listening to us, we should create a producer
which generates messages that are published to Kafka and thereby
consumed by our consumer created earlier:

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap\_servers=\'localhost:9092\')

producer.send(\'sample\', b\'Hello, World!\')

producer.send(\'sample\', key=b\'message-two\', value=b\'This is
Kafka-Python\')

You can now revisit the consumer shell to check if it has received the
records sent from the producer through our Kafka setup.

Thus, a simple Hello, World! in Kafka using Python.

**Final Remarks**

Even though Kafka is a seriously powerful tool, there are some
drawbacks, which is why we chose to go for a managed tool such as AWS
Kinesis here at Timber. We\'ve found that provisioning your own servers
and digging into the nitty-gritty doesn\'t make as much sense when
we\'re aiming for velocity. We\'re starting to reconsider that decision
as we hit some of the limitations of Kinesis.

** Simple Example **

**Let's code**
  
In our example we'll create a **producer** that emits numbers from 1 to
1000 and send them to our Kafka **broker**. Then a **consumer** will
read the data from the **broker** and store them in a MongoDb
collection.

The advantage of using Kafka is that, if our consumer breaks down, the
new or fixed consumer will pick up reading where the previous one
stopped. This is a great way to make sure **all the data is fed into the
database without duplicates or missing data**.

**Create a new Python script named *producer.py**
![](https://github.com/samirsahoo007/bigdata/tree/master/kafka/simple_example/producer.py)

If you want to test the code, it's advised to create a new topic and
send the data to this new topic. This way, you'll avoid duplicates and
possible confusion in the *numtest* topic when we're later testing the
producer and consumer together.

**Consuming the data consumer.py**
![](https://github.com/samirsahoo007/bigdata/tree/master/kafka/simple_example/consumer.py)

**Testing**

Let's test our two scripts. Open a command prompt and go to the
directory where you saved *producer.py* and *consumer.py*. Execute
*producer.py* and open a new command prompt. Launch *consumer.py* and
look how it reads all the messages, including the new ones.

Now interrupt the consumer, remember at which number it was (or check it
in the database) and restart the consumer. Notice that the consumer
picks up all the missed messages and then continues listening for new
ones.

Note that if you turn off the consumer within 1 second after reading the
message, the message will be retrieved again upon restart. Why? Because
our *auto\_commit\_interval* is set to 1 second, remember that if the
offset is not committed, the consumer will read the message again (if
*auto\_offset\_reset* is set to earliest).

