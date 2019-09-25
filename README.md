# bigdata

Hadoop Ecosystem is a platform or a suite which provides various services to solve the big data problems.

Following are the components that collectively form a Hadoop ecosystem:

* HDFS: Hadoop Distributed File System
* YARN: Yet Another Resource Negotiator
* MapReduce: Programming based Data Processing
* Spark: In-Memory data processing
* PIG, HIVE: Query based processing of data services
* HBase: NoSQL Database
* Mahout, Spark MLLib: Machine Learning algorithm libraries
* Solar, Lucene: Searching and Indexing
* Zookeeper: Managing cluster
* Oozie: Job Scheduling
* Kibana - data visualisation tool for Elasticsearch
* Elasticsearch - data store & analytics / search engine
* Beeline - Hive command line interface
* Datasift - online service that streams tweets matching a given pattern to a nominated datastore (such as MongoDB)
* Apache Storm - Storm is about real-time processing of data streams. It consists of higher level of abstraction than simple message passing (which permits describing topologies as a DAG), per-process fault-tolerance and definite at-least-once semantics for each message in the structure.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/HadoopEcosystem-min.png)

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/HADOOP-ECOSYSTEM.png)

				(https://www.edureka.co/blog/hadoop-ecosystem)


Note: Apart from the above-mentioned components, there are many other components too that are part of the Hadoop ecosystem.

All these toolkits or components revolve around one term i.e. Data. That’s the beauty of Hadoop that it revolves around data and hence making its synthesis easier.

## Analytics with Kibana and Elasticsearch through Hadoop
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/elastic_search_example1.png)
Refer for more info: https://www.rittmanmead.com/blog/2014/11/analytics-with-kibana-and-elasticsearch-through-hadoop-part-1-introduction/

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/elasticsearch_ex2.jpeg)

## ES-Hadoop architecture
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/elasticsearch_hadoop.jpg)

# HDFS - Hadoop Distributed File System:

* HDFS is the primary or major component of Hadoop ecosystem and is responsible for storing large data sets of structured or unstructured data across various nodes and thereby maintaining the metadata in the form of log files.
* HDFS consists of two core components i.e.
	1. Name node
	2. Data Node
* Name Node is the prime node which contains metadata (data about data) requiring comparatively fewer resources than the data nodes that stores the actual data. These data nodes are commodity hardware in the distributed environment. Undoubtedly, making Hadoop cost effective.
* HDFS maintains all the coordination between the clusters and hardware, thus working at the heart of the system.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/HDFSnodes-min.png)

# YARN - Yet Another source Navigator:

* Yet Another Resource Negotiator, as the name implies, YARN is the one who helps to manage the resources across the clusters. In short, it performs scheduling and resource allocation for the Hadoop System.
* Consists of three major components i.e.
	1. Resource Manager
	2. Nodes Manager
	3. Application Manager

* Resource manager has the privilege of allocating resources for the applications in a system whereas Node managers work on the allocation of resources such as CPU, memory, bandwidth per machine and later on acknowledges the resource manager. Application manager works as an interface between the resource manager and node manager and performs negotiations as per the requirement of the two.

# MapReduce:
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/Map-Reduce.jpg)
* By making the use of distributed and parallel algorithms, MapReduce makes it possible to carry over the processing’s logic and helps to write applications which transform big data sets into a manageable one.

* MapReduce makes the use of two functions i.e. Map() and Reduce() whose task is:
* Map() performs sorting and filtering of data and thereby organizing them in the form of group. Map generates a key-value pair based result which is later on processed by the Reduce() method.
* Reduce(), as the name suggests does the summarization by aggregating the mapped data. In simple, Reduce() takes the output generated by Map() as input and combines those tuples into smaller set of tuples.

# PIG - Data Query System:

* Pig was basically developed by Yahoo which works on a pig Latin language, which is Query based language similar to SQL.
* It is a platform for structuring the data flow, processing and analyzing huge data sets.
* Pig does the work of executing commands and in the background, all the activities of MapReduce are taken care of. After the processing, pig stores the result in HDFS.
* Pig Latin language is specially designed for this framework which runs on Pig Runtime. Just the way Java runs on the JVM.
* Pig helps to achieve ease of programming and optimization and hence is a major segment of the Hadoop Ecosystem.

# HIVE - Data Query System:

* With the help of SQL methodology and interface, HIVE performs reading and writing of large data sets. However, its query language is called as HQL (Hive Query Language).
* It is highly scalable as it allows real-time processing and batch processing both. Also, all the SQL datatypes are supported by Hive thus, making the query processing easier.
* Similar to the Query Processing frameworks, HIVE too comes with two components: JDBC Drivers and HIVE Command Line.
* JDBC, along with ODBC drivers work on establishing the data storage permissions and connection whereas HIVE Command line helps in the processing of queries.

# Mahout:

* Mahout, allows Machine Learnability to a system or application. Machine Learning, as the name suggests helps the system to develop itself based on some patterns, user/environmental interaction or om the basis of algorithms.
* It provides various libraries or functionalities such as collaborative filtering, clustering, and classification which are nothing but concepts of Machine learning. It allows invoking algorithms as per our need with the help of its own libraries.

# Apache Spark:

* It’s a platform that handles all the process consumptive tasks like batch processing, interactive or iterative real-time processing, graph conversions, and visualization, etc.
* It consumes in memory resources hence, thus being faster than the prior in terms of optimization.
* Spark is best suited for real-time data whereas Hadoop is best suited for structured data or batch processing, hence both are used in most of the companies interchangeably.

# Apache HBase:

* It’s a NoSQL database which supports all kinds of data and thus capable of handling anything of Hadoop Database. It provides capabilities of Google’s BigTable, thus able to work on Big Data sets effectively.
* At times where we need to search or retrieve the occurrences of something small in a huge database, the request must be processed within a short quick span of time. At such times, HBase comes handy as it gives us a tolerant way of storing limited data.
* Other Components: Apart from all of these, there are some other components too that carry out a huge task in order to make Hadoop capable of processing large datasets. They are as follows:

# Solr, Lucene: 
* These are the two services that perform the task of searching and indexing with the help of some java libraries, especially Lucene is based on Java which allows spell check mechanism, as well. However, Lucene is driven by Solr.

# Zookeeper: 
* There was a huge issue of management of coordination and synchronization among the resources or the components of Hadoop which resulted in inconsistency, often. Zookeeper overcame all the problems by performing synchronization, inter-component based communication, grouping, and maintenance.

# Oozie: 
* Oozie simply performs the task of a scheduler, thus scheduling jobs and binding them together as a single unit. There is two kinds of jobs .i.e Oozie workflow and Oozie coordinator jobs. Oozie workflow is the jobs that need to be executed in a sequentially ordered manner whereas Oozie Coordinator jobs are those that are triggered when some data or external stimulus is given to it.

# How Spark Is Better than Hadoop?
* In-memory Processing: 
	Spark is 100 times faster than MapReduce as everything is done here in memory.
* Stream Processing: 
	It involves continuous input and output of data. Stream processing is also called real-time processing.
	
* Less Latency: 
	Since it caches most of the input data in memory by the Resilient Distributed Dataset (RDD).
	Each dataset in an RDD is partitioned into logical portions, which can then be computed on different nodes of a cluster.
* Lazy Evaluation: 
	Apache Spark starts evaluating only when it is absolutely needed. This plays an important role in contributing to its speed.

# Components of Spark:
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/Components-of-Spark.jpg)
	
# Why Use Hadoop and Spark Together?
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/Why-Use-Hadoop-and-Spark-Together.jpg)
* Spark does not have its own distributed file system. By combining Spark with Hadoop, you can make use of various Hadoop capabilities. For example, resources are managed via YARN Resource Manager. You can integrate Hadoop with Spark to perform Cluster Administration and Data Management.

* Hadoop provides enhanced security, which is a critical component for production workloads. Spark workloads can be deployed on available resources anywhere in a cluster, without manually allocating and tracking individual tasks.

* Spark can run on Hadoop, stand-alone Mesos, or in the Cloud.
* Spark’s MLlib components provide capabilities that are not easily achieved by Hadoop’s MapReduce. By using these components, * Machine Learning algorithms can be executed faster inside the memory.

# Kafka:
* Apache Kafka is a distributed streaming platform that lets you publish and subscribe to streams of records. 

Note: Publish/Subscribe is a messaging model where senders send the messages, which are then consumed by the multiple consumers. 

* Kafka is usually integrated with Apache Storm, Apache HBase, and Apache Spark in order to process real-time streaming data. It is capable of delivering massive message streams to Hadoop cluster regardless of the industry or use case.

* Basically, Kafka is a data ingestion mechanism through which you can load data into Hadoop clusters in real time. 
* Website activity tracking, Log aggregation, Stream processing are some of the use cases of Kafka.

## Kafka Architecture:
Kafka is deployed as a cluster implemented on one or more servers. The cluster is capable of storing topics which consist of streams of ‘records’ or ‘messages’. Every message holds details like a key and a value. Brokers are abstractions used to manage the persistence and replication of the message.

* Producer: publish messages to a topic
* Topic: category or feed name to which records are published
* Consumer: subscribes to a topic and consume the messages 
* Broker: set of servers in Kafka cluster

While, ZooKeeper is used for managing, coordinating Kafka broker. Each Kafka broker is coordinating with other Kafka brokers using ZooKeeper. Producer and consumer are notified by ZooKeeper service about the presence of new broker in Kafka system or failure of the broker in Kafka system.

### Single Node Multiple Brokers
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/single_node_multiple_broker.png)

# Topic Replication Factor in Kafka
While designing a Kafka system, it’s always a wise decision to factor in topic replication. As a result, its topics’ replicas from another broker can solve the crisis, if a broker goes down. For example, we have 3 brokers and 3 topics. Broker1 has Topic 1 and Partition 0, its replica is in Broker2, so on and so forth. It has got a replication factor of 2; it means it will have one additional copy other than the primary one. Below is the image of Topic Replication Factor:

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/kafka-topic-replication.png)

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/kafka-architecture-topic-partition-consumer-group-offset-producers.png)
					
### Multiple Nodes Multiple Brokers
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/multiple-node-multiple-broker.jpg)


Kafka Ecosystem: Diagram of Connect Source, Connect Sink, and Kafka Streams

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/kafka-ecosystem.png)



Kafka Ecosystem: Kafka REST Proxy and Confluent Schema Registry


![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/kafka-ecosystem-rest-proxy-schema-registry.png)
	

Kafka @ LinkedIn



![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/kafka1.png)



LinkedIn Newsfeed is powered by Kafka

 
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/kafka2.png)


LinkedIn recommendations are powered by Kafka


![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/kafka3.png)



Refer: http://bigdata.andreamostosi.name

# Doing Computation
The goal: get the compute work to some computer with processor/memory to do it, and get the results back.

Apache YARN: Hadoop's resource manager.
Mesos: resource manager more closely aligned with Spark.
Amazon EC2: get VMs to do work with.
Amazon EMR: EC2 + Hadoop set up automatically.
Google Compute Engine: get VMs from Google.
Amazon Lambda: give Amazon functions; it runs them when you call.
Google AppEngine: give Google functions; it runs them when you call.
This could also extend to tools like Kubernetes or AWS Elastic Container Service that can get compute work running and scale up/down.

# Expressing Computation
The goal: Describe your computation in a way that can be run on a cluster.

MapReduce.
Spark.
Flink: competitor to Spark. Scala/​Java. Streaming first.
Hive: take varied data and do SQL-like queries.
Pig: high-level language to analyze data. Produces MapReduce jobs.
Programming. Distributed systems.
Data Warehousing
The goal: Take lots of data from many sources, and do reporting/​analysis on it.

# Spark DataFrames.
Hive: take varied data and do SQL-like queries.
Apache Impala: massively-parallel SQL queries on Hadoop, against varied inputs.
Apache Drill: take data from many sources (SQL, NoSQL, files, …) and query it.
Google BigQuery: Google's data warehouse tool.
Amazon RedShift: Amazon's data warehouse tool.

# Storing Files
The goal: Store files or file-like things in a distributed way.

HDFS.
Amazon S3: Amazon's file storage.
Gluster: distributed network filesystem.
Alluxio: in-memory distributed storage system.
Ceph: distributed filesystems and object store.
Files. Filesystems. Disks. NAS.

# Databases
The goal: store records and access/update them quickly. I don't need SQL/​relations.

Cassandra: Good clustering. Secondary keys, but no joins.
HBase: Good clustering, fast. Otherwise very manual.
MongoDB. Clustered, but questionable reliability. Suggest not using for primary data storage. **
Amazon SimpleDB and DynamoDB.
The goal: store records and access/update them quickly. I want SQL and/or relations.

Amazon Aurora: Amazon's scalable relational database.
Other NewSQL databases.
PostgreSQL, MySQL, etc.

# Serialization/Storage
The goal: read/write data efficiently for memory/​disk/​network.

Parquet: efficient columnar storage representation. Supported by Spark, Pandas, Impala.
HDF5: on-disk storage for columnar data.
CSV, JSON: well-understood interchange formats.
Arrow: in-memory representation for fast processing. Available in Spark 2.3+.

# Streaming
The goal: deal with a continuously-arriving stream of data.

Spark Streaming (DStreams for RDDs, Structured Streaming for DataFrames).
Apache Storm.
Apache Flume.
Amazon Kinesis.

# ML Libraries
The goal: use machine learning algorithms (at scale) without having to implement them.

Spark MLlib.
Apache Mahout.
Amazon Machine Learning.
Or at smaller scale, scikit-learn, PyTorch, etc.

# Visualization
The goal: take the data you worked so hard to get, and let people understand it and interact with it.

Tableau.
Qlik.
Power BI.
Programming and plotting/​drawing libraries.

# Extract-Transform-Load
The goal: Extract data from the source(s); transform it into the format we want; load it into the database/​data warehouse.

Apache Sqoop.
Amazon Data Pipeline.
NiFi
MapReduce, Spark, programming.

# Message Queues
The goal: pass messages between nodes/​processes and have somebody else worry about reliability, queues, who will send/receive, etc.

Apache Kafka.
RabbitMQ.
ZeroMQ/ØMQ.
Amazon SQS.
All designed to scale out and handle high volume.

The idea:

Some nodes publish messages into a queue.
The message queue makes sure that they are queued until they can be processed; ensures each message is processed once (depending on the tool).
Some nodes subscribe to the queue(s) and consume messages.
Or other interactions with the queues. Freely switch languages between publisher/consumer too.

These things are fast: RabbitMQ Hits One Million Messages Per Second.

Realistic streaming scenario: Spark streaming takes in the data stream, filters/processes minimally, and puts each record into a queue for more processing. Then many nodes subscribe to the queue and handle the data out of it.

Or without Hadoop, just generate a bunch of work that needs to be done, queue it all, then start consumer processes on each computer you have.

Either way: you can move around the bottleneck (and hopefully then fix it).

Message passing example with RabbitMQ:

rabbit-receiver.py
rabbit-source.py
rabbit-source.rb
Let's try it…

window1> python3 rabbit-receiver.py
window2> python3 rabbit-receiver.py
window3> python3 rabbit-source.py
window4> ruby rabbit-source.rb
# kill/restart some and see what happens
Message passing example with Kafka:

kafka-producer.py
kafka-consumer.py
Let's try it…

window1> python3 kafka-consumer.py
window2> python3 kafka-consumer.py
window3> python3 kafka-producer.py
Task Queues
The goal: get some work on a distributed queue. Maybe wait for results, or maybe don't.

Celery (Python).
Resque, Sidekiq (Ruby).
Google AppEngine Task Queues (Python, Java, Go, PHP).
Amazon Simple Workflow Service.
Any message queue + some code.
With a task queue, you get to just call a function (maybe with slightly different syntax). You can then retrieve the result (or just move on an let the work happen later).

Where the work happened is transparent.

A task with Celery: tasks.py.

Let's try it…

window1> celery -A tasks worker --loglevel=info --hostname=worker1@%h
window2> celery -A tasks worker --loglevel=info --hostname=worker2@%h
window3> ipython3
from tasks import add
result = add.delay(4, 4)
result.get(timeout=1)
Need a lot of work done without Hadoop? Run task queue workers on many nodes; make all the asynchronous calls you want; let the workers handle it.

Need nightly batch analysis done? Have a scheduled task start a Spark task.

Have a spike in usage? Let tasks queue up and process as possible. Or add more workers.

Text Search
The goal: index lots of data so you (or your users) can search for records they want.

Apache Solr/Apache Lucene.
Elasticsearch.
Amazon CloudSearch.
All of these are designed to scale out across many nodes.

Indexing and searching with Elasticsearch:

elastic-index.py
elastic-search.py
Let's try it… (See also CourSys search when an instructor.)

python3 elastic-index.py
python3 elastic-search.py
curl -XGET 'http://localhost:9200/comments/_search?q=comment' \
  | python3 -m json.tool
Hadoop Distributions
The goal: Get a Hadoop cluster running without becoming an expert on Hadoop configuration.

Cloudera: what is running our cluster.
Hortonworks HDP.
MapR.
Amazon EMR: EC2 + Hadoop set up automatically.


# Splunk

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/WhatSplunkCanIndex.jpg)

The Splunk App for Jenkins helps engineering teams, including developers, test/QA engineers and program managers as well as Jenkins admins to:
	* Get instant visibility into test results.
	* Gain instant and detailed insights into the progress and results of Jenkins builds.  
	* Monitor the health of Jenkins infrastructure.
	
	
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/splunk_jenkins1.png)

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/splunk_jenkins1.png)

