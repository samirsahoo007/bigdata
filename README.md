# bigdata

## quickstart

```
docker pull cloudera/quickstart:latest
docker run --hostname=quickstart.cloudera --privileged=true -v /tmp/:/tmp/ -it cloudera/quickstart /usr/bin/docker-quickstart
```
If any service fails to start make sure to cleanup following files from /tmp
```
rm -rf /tmp/Jetty_* /tmp/hadoop* /tmp/hsperfdata_*
```

Ref: https://docs.cloudera.com/documentation/enterprise/5-6-x/topics/quickstart_docker_container.html

Hadoop Ecosystem is a platform or a suite which provides various services to solve the big data problems.

Following are the components that collectively form a Hadoop ecosystem:

* Oozie: Job Scheduling, workflow monitoring
* Chukwa: Monitoring, data collection system for monitoring large distributed systems 
* Flume, Sqoop - (Monitoring)Data Ingesting Services(Flume plays on Unstructured/Semi-structured data; Sqoop plays on Structured data). More below
* Zookeeper: cluster management(provides a distributed configuration service, a synchronization service and a naming registry for distributed systems)
* HIVE, PIG: Query based processing of data services(SQL, Dataflow)
* Mahout, Spark MLLib: Machine Learning algorithm libraries
* Avro: (RPC)row-oriented remote procedure call and data serialization framework(uses JSON for defining data types and protocols,& serializes data in a compact binary format. Apache Spark SQL can access Avro as a data source)
* Sqoop: (RDBMS Connector) Data Ingesting Services on structured data
* MapReduce: Programming based Data Processing
* YARN: Cluster and resource management(Yet Another Resource Negotiator)
* HDFS: Hadoop Distributed File System
* HBase: Column DB Storage (NoSQL Database)
* Spark: In-Memory data processing
* Solar, Lucene: Searching and Indexing
* Kibana - data visualisation tool for Elasticsearch
* Elasticsearch - data store & analytics / search engine
* Beeline - Hive command line interface
* Datasift - online service that streams tweets matching a given pattern to a nominated datastore (such as MongoDB)
* Ambari - Provision, Monitor and Maintain cluster
* Apache Drill - SQL on Hadoop
* Apache Storm - real-time processing of data streams. It consists of higher level of abstraction than simple message passing (which permits describing topologies as a DAG), per-process fault-tolerance and definite at-least-once semantics for each message in the structure.
* Kafka is a scalable, high performance, low latency platform that allows reading and writing streams of data like a messaging system. 
* Spark Streaming is part of the Apache Spark platform that enables scalable, high throughput, fault tolerant processing of data streams.
* Cassandra is a distributed and wide-column NoSQL data store.
* Hue(Hadoop User Experience) is a web-based interactive query editor that enables you to interact with data warehouses. It allows you to browse, analyze query (hive, pig or impala) and visualizie data. 

#### Notes:
* Flume is service for efficiently collecting, aggregating, and moving large amounts of log data

* Sqoop is a tool designed to transfer data between Hadoop and relational database servers. It is used to import data from relational databases such as MySQL, Oracle to Hadoop HDFS, and export from Hadoop file system to relational databases.

* Hive has a declarative SQL like language termed as HiveQL. Pig has a procedural data flow like language termed as Pig Latin. 
* Hive is basically used for generation/creation of reports. Pig is basically used for programming(Map Reduce). Hive operates on the server side of an HDFS cluster.

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
* Oozie simply performs the task of a scheduler, thus scheduling jobs and binding them together as a single unit. 

There is two kinds of jobs .i.e Oozie workflow and Oozie coordinator jobs. 

Oozie Workflow jobs are Directed Acyclical Graphs (DAGs) of actions i.e. Oozie workflow is the jobs that need to be executed in a sequentially ordered manner.

Oozie Coordinator jobs are those that are triggered when some data or external stimulus is given to it. Oozie Coordinator jobs are recurrent Oozie Workflow jobs triggered by time (frequency) and data availability.

## Use case

### A Recurrent Problem

Hadoop, Pig, Hive, and many other projects provide the foundation for storing and processing large amounts of data in an efficient way. Most of the time, it is not possible to perform all required processing with a single MapReduce, Pig, or Hive job. Multiple MapReduce, Pig, or Hive jobs often need to be chained together, producing and consuming intermediate data and coordinating their flow of execution.

At Yahoo!, as developers started doing more complex processing using Hadoop, multistage Hadoop jobs became common. This led to several ad hoc solutions to manage the execution and interdependency of these multiple Hadoop jobs. Some developers wrote simple shell scripts to start one Hadoop job after the other. Others used Hadoop’s JobControl class, which executes multiple MapReduce jobs using topological sorting. One development team resorted to Ant with a custom Ant task to specify their MapReduce and Pig jobs as dependencies of each other—also a topological sorting mechanism. Another team implemented a server-based solution that ran multiple Hadoop jobs using one thread to execute each job.

As these solutions started to be widely used, several issues emerged. It was hard to track errors and it was difficult to recover from failures. It was not easy to monitor progress. It complicated the life of administrators, who not only had to monitor the health of the cluster but also of different systems running multistage jobs from client machines. Developers moved from one project to another and they had to learn the specifics of the custom framework used by the project they were joining. Different organizations within Yahoo! were using significant resources to develop and support multiple frameworks for accomplishing basically the same task.

### A Common Solution: Oozie

It was clear that there was a need for a general-purpose system to run multistage Hadoop jobs with the following requirements:

It should use an adequate and well-understood programming model to facilitate its adoption and to reduce developer ramp-up time.

It should be easy to troubleshot and recover jobs when something goes wrong.

It should be extensible to support new types of jobs.

It should scale to support several thousand concurrent jobs.

Jobs should run in a server to increase reliability.

It should be a multitenant service to reduce the cost of operation.

Toward the end of 2008, Alejandro Abdelnur and a few engineers from Yahoo! Bangalore took over a conference room with the goal of implementing such a system. Within a month, the first functional version of Oozie was running. It was able to run multistage jobs consisting of MapReduce, Pig, and SSH jobs. This team successfully leveraged the experience gained from developing PacMan, which was one of the ad hoc systems developed for running multistage Hadoop jobs to process large amounts of data feeds.

Yahoo! open sourced Oozie in 2010. In 2011, Oozie was submitted to the Apache Incubator. A year later, Oozie became a top-level project, Apache Oozie.

#### Oozie’s role in the Hadoop Ecosystem

In this section, we briefly discuss where Oozie fits in the larger Hadoop ecosystem. Figure 1-1 captures a high-level view of Oozie’s place in the ecosystem. Oozie can drive the core Hadoop components—namely, MapReduce jobs and Hadoop Distributed File System (HDFS) operations. In addition, Oozie can orchestrate most of the common higher-level tools such as Pig, Hive, Sqoop, and DistCp. More importantly, Oozie can be extended to support any custom Hadoop job written in any language. Although Oozie is primarily designed to handle Hadoop components, Oozie can also manage the execution of any other non-Hadoop job like a Java class, or a shell script.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/oozie/images/apoo_0101.png)

#### What exactly is Oozie?

Oozie is an orchestration system for Hadoop jobs. Oozie is designed to run multistage Hadoop jobs as a single job: an Oozie job. Oozie jobs can be configured to run on demand or periodically. Oozie jobs running on demand are called workflow jobs. Oozie jobs running periodically are called coordinator jobs. There is also a third type of Oozie job called bundle jobs. A bundle job is a collection of coordinator jobs managed as a single job.

#### The name "Oozie"

Alejandro and the engineers were looking for a name that would convey what the system does—managing Hadoop jobs. Something along the lines of an elephant keeper sounded ideal given that Hadoop was named after a stuffed toy elephant. Alejandro was in India at that time, and it seemed appropriate to use the Hindi name for elephant keeper, mahout. But the name was already taken by the Apache Mahout project. After more searching, oozie (the Burmese word for elephant keeper) popped up and it stuck.


# Pepperdata (https://www.pepperdata.com/):

- It's an Application Profiler — a platform that developers can use to understand how to optimize the capacity of applications running within their networks.

- The Pepperdata Application Profiler is essentially a big data production platform that is accompanied by three products — a cluster analyzer, a capacity optimizer, and a policy enforcer.

- Real-time visibility for troubleshooting, debugging, and planning.

- Automated tuning for optimal performance on-prem and in the cloud.

- Run More Apps, Track Spend, and Manage Costs

- Rely on Hadoop to guarantee service levels in mixed workload and multi-tenant production clusters. Pepperdata installs in less than 30 minutes on your existing Hadoop cluster without any modifications to the scheduler, workflow, or jobs.

## Application Description
Diagnose problems faster. Pepperdata gives you a both a macro and granular view of everything that’s happening across the cluster by monitoring the use of CPU, memory, disk I/O, and network for every job and task, by user or group in real time. This detailed telemetry data is captured second by second, and is saved so that you can analyze performance variations and anomalies over time.

Guarantee SLAs. Pepperdata senses contention for CPU, memory, disk I/O, and network at run time and will automatically slow down low-priority tasks when needed to ensure that high-priority SLAs are maintained.

Increase cluster throughput by 30-70%. In many cases, jobs will run much faster. Pepperdata knows the true hardware resource capacity of your cluster and dynamically allows more tasks to run on servers that have free resources at any given moment.

### Note:

Application Profiler is based off the open source <b>Dr. Elephant</b> project created by LinkedIn, and its software is integrated with the open source project as well. Dr. Elephant is a set of monitoring tools for Hadoop and Spark, and it automatically gathers metrics to increase cluster efficiency. It gives developers suggestions of what to change in their code when there is a bug or a capacity issue.

Pepperdata’s software is essentially the same as Dr. Elephant except it’s packaged with more features to provide more context.

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

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/fig1-large.jpg)
			Traffic Data Monitoring Using IoT, Kafka and Spark Streaming
			
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/netflix.png)
			(Building an Event-Driven Reactive Asynchronous System with Spring Boot and Kafka)

# Hystrix: What is it and why is it used?

Hystrix is a latency and fault tolerance library designed to isolate points of access to remote systems, services and 3rd party libraries. which helps in

* Stop cascading failures

* Realtime monitoring of configurations changes

* Concurrency aware request caching

* Automated batching through request collapsing

* IE. If a micro service is failing then return the default response and wait until it recovers.

In any distributed environment (with lot of dependencies), inevitably some of the many service dependencies fail. So Hystrix library is used to control the interaction between these distributed services by adding some latency tolerance and fault tolerance logic. It does so by the following methods:

* Isolating the points of access between the services

* Stopping cascading failures in distributed system

* Introducing timeout for particular action

* Fallback and gracefully degrade when possible.

* Complex distributed architectures have lot of dependencies, any one of them will inevitably fail at some point. For example, an application having 50 services has 99.99% uptime for each of it’s services, thus we can expect that

over all uptime is 99.99⁵⁰ = 99.5%

0.5% of downtime

so 0.5% of 1 billion requests = 5,000,000 failures

this means 4hr+ downtime/month, even when all the dependencies have an excellent uptime individually.

We see that even when all dependencies perform well, the aggregate impact of even 0.01% downtime leads to 4 hour downtime per month if we do not make the whole system resilient. The above example or statistics shows the importance of Hystrix in any distributed system.

Hence, all of the failing and latency needs to be isolated and managed, so that a single failing dependency can not take down an entire application and whole of the system. Hystrix puts a wrapper around the dependencies and limits concurrent access to any one of them. If Hystrix library is used in the system, then the clients execute on separate threads. This isolates them from the calling threads, and so the caller may walk away from the dependency call that is taking a long time. When Hystrix is used then each dependencies is isolated form one other, restricted in the resources it can saturate when the latency occur and covered it in fall back logic that and covered in fallback logic that decides what response to make when any time of failure occurs in the dependencies.


![alt text](https://github.com/Netflix/Hystrix/wiki/How-it-Works)



Refer: http://bigdata.andreamostosi.name

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/architecture-00-b.png)
			Building Analytics Engine Using Akka, Kafka & ElasticSearch

# Kafka streaming

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/microservices-exercises-combined.png)

Read more at https://docs.confluent.io/current/tutorials/examples/microservices-orders/docs/index.html

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/mapr-architectures.png)
			Fast Data Processing Pipeline for Predicting Flight Delays Using Apache APIs
Read more at https://dzone.com/articles/fast-data-processing-pipeline-for-predicting-fligh-2

# Kafka with Spark (Building real-time applications)

Traditional machine learning methods have been developed to work using batch or offline approaches.
Spark streaming and Kafka Integration are the best combinations to build real-time applications. Spark is an in-memory processing engine on top of the Hadoop ecosystem, and Kafka is a distributed public-subscribe messaging system. Kafka can stream data continuously from a source and Spark can process this stream of data instantly with its in-memory processing primitives. By integrating Kafka and Spark, a lot can be done. We can even build a real-time machine learning application.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/Data-Pipeline-With-Checkpoints-1.jpg)

			Highly scalable and fault tolerant data pipeline for a real-time data stream.
			
In a stream processing application, it's often useful to retain state between batches of data being processed. For example, in our previous attempt, we are only able to store the current frequency of the words. What if we want to store the cumulative frequency instead? Spark Streaming makes it possible through a concept called checkpoints. Please note that we'll be using checkpoints only for the session of data processing. This does not provide fault-tolerance. However, checkpointing can be used for fault tolerance as well. Here, we are using the local filesystem to store checkpoints. However, for robustness, this should be stored in a location like HDFS, S3 or Kafka. 

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/kafka_spark_pipeline.png)

Here, we use a Receiver to receive the data. So, by using the Kafka high-level consumer API, we implement the Receiver. Further, the received data is stored in Spark executors. Then jobs launched by Kafka – Spark Streaming processes the data.
Although, it is a possibility that this approach can lose data under failures under default configuration. Hence, we have to additionally enable write-ahead logs in Kafka Spark Streaming, to ensure zero-data-loss. That saves all the received Kafka data into write-ahead logs on a distributed file system synchronously. In this way, it is possible to recover all the data on failure.

More info: https://dzone.com/articles/kafka-and-spark-streams-living-happily-ever-after

# Flafka
Cloudera engineers and other open source community members have recently committed code for Kafka-Flume integration, informally called "Flafka," to the Flume project. Flume is a distributed, reliable, and available system for efficiently collecting, aggregating, and moving large amounts of data from many different sources to a centralized data store. Flume provides a tested, production-hardened framework for implementing ingest and real-time processing pipelines. Using the new Flafka source and sink, now available in CDH 5.2, Flume can both read and write messages with Kafka.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/flafka-f11.png)

Flume can act as a both a consumer (above) and producer for Kafka (below)
Producers – Use Flume sources to write to Kafka			Consumers – Write to Flume sinks reading from Kafka

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/flafka-f31.png)

## Example: Transaction Ingest
Assume that you are ingesting transaction data from a card processing system, and want to pull the transactions directly from Kafka and write them into HDFS.

The record simply contains a UUID for a transaction_id, a dummy credit-card number, timestamp, amount, and store_id for the transaction.

888fc23a-5361-11e4-b76d-22000ada828b|4916177742705110|2014-10-14 01:18:29|67.88|1433
888fdb26-5361-11e4-b76d-22000ada828b|4929011455520|2014-10-14 01:18:29|45.22|886
888ff1e2-5361-11e4-b76d-22000ada828b|4532623020656|2014-10-14 01:18:29|27.14|681
88900c72-5361-11e4-b76d-22000ada828b|4024007162856600|2014-10-14 01:18:29|34.63|577

# Flume Architecture

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/flume/images/UserGuide_image00.png)

			Data flow model
OR

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/flume/images/061114_1038_Introductio2.png)

Undoubtedly, Apache Flume is robust and reliable due to its tunable reliability and recovery mechanisms. It also uses a simple extendable model for data that allows the application of online analytics. Flume sends the data to the Spark ecosystem, where data acceptance and processing happens

## Data ingestion
Flume supports a number of mechanisms to ingest data from external sources.

### RPC
An Avro client included in the Flume distribution can send a given file to Flume Avro source using avro RPC mechanism:

```
$ bin/flume-ng avro-client -H localhost -p 41414 -F /usr/logs/log.10
The above command will send the contents of /usr/logs/log.10 to to the Flume source listening on that ports.
```

### Executing commands
There’s an exec source that executes a given command and consumes the output. A single ‘line’ of output ie. text followed by carriage return (‘\r’) or line feed (‘\n’) or both together.

### Network streams
Flume supports the following mechanisms to read data from popular log stream types, such as:

1. Avro
2. Thrift
3. Syslog
4. Netcat

### Setting multi-agent flow¶
Two agents communicating over Avro RPC

In order to flow the data across multiple agents or hops, the sink of the previous agent and source of the current hop need to be avro type with the sink pointing to the hostname (or IP address) and port of the source.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/flume/images/UserGuide_image03.png)

### Consolidation
A very common scenario in log collection is a large number of log producing clients sending data to a few consumer agents that are attached to the storage subsystem. For example, logs collected from hundreds of web servers sent to a dozen of agents that write to HDFS cluster.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/flume/images/UserGuide_image02.png)
			A fan-in flow using Avro RPC to consolidate events in one place

This can be achieved in Flume by configuring a number of first tier agents with an avro sink, all pointing to an avro source of single agent (Again you could use the thrift sources/sinks/clients in such a scenario). This source on the second tier agent consolidates the received events into a single channel which is consumed by a sink to its final destination.

### Multiplexing the flow
Flume supports multiplexing the event flow to one or more destinations. This is achieved by defining a flow multiplexer that can replicate or selectively route an event to one or more channels.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/flume/images/UserGuide_image01.png)
			A fan-out flow using a (multiplexing) channel selector

The above example shows a source from agent “foo” fanning out the flow to three different channels. This fan out can be replicating or multiplexing. In case of replicating flow, each event is sent to all three channels. For the multiplexing case, an event is delivered to a subset of available channels when an event’s attribute matches a preconfigured value. For example, if an event attribute called “txnType” is set to “customer”, then it should go to channel1 and channel3, if it’s “vendor” then it should go to channel2, otherwise channel3. The mapping can be set in the agent’s configuration file.


## Log Data with Flume in HDFS

Some of the data that ends up in the Hadoop Distributed File System (HDFS) might land there via database load operations or other types of batch processes, but what if you want to capture the data that’s flowing in high-throughput data streams, such as application log data? Apache Flume is the current standard way to do that easily, efficiently, and safely.

Apache Flume, another top-level project from the Apache Software Foundation, is a distributed system for aggregating and moving large amounts of streaming data from different sources to a centralized data store.

Put another way, Flume is designed for the continuous ingestion of data into HDFS. The data can be any kind of data, but Flume is particularly well-suited to handling log data, such as the log data from web servers. Units of the data that Flume processes are called events; an example of an event is a log record.

To understand how Flume works within a Hadoop cluster, you need to know that Flume runs as one or more agents, and that each agent has three pluggable components: sources, channels, and sinks:

Sources retrieve data and send it to channels.

Channels hold data queues and serve as conduits between sources and sinks, which is useful when the incoming flow rate exceeds the outgoing flow rate.

Sinks process data that was taken from channels and deliver it to a destination, such as HDFS.

An agent must have at least one of each component to run, and each agent is contained within its own instance of the Java Virtual Machine (JVM).

An event that is written to a channel by a source isn’t removed from that channel until a sink removes it by way of a transaction. If a network failure occurs, channels keep their events queued until the sinks can write them to the cluster. An in-memory channel can process events quickly, but it is volatile and cannot be recovered, whereas a file-based channel offers persistence and can be recovered in the event of failure.

Each agent can have several sources, channels, and sinks, and although a source can write to many channels, a sink can take data from only one channel.

An agent is just a JVM that’s running Flume, and the sinks for each agent node in the Hadoop cluster send data to collector nodes, which aggregate the data from many agents before writing it to HDFS, where it can be analyzed by other Hadoop tools.

Agents can be chained together so that the sink from one agent sends data to the source from another agent. Avro, Apache’s remote call-and-serialization framework, is the usual way of sending data across a network with Flume, because it serves as a useful tool for the efficient serialization or transformation of data into a compact binary format.

In the context of Flume, compatibility is important: An Avro event requires an Avro source, for example, and a sink must deliver events that are appropriate to the destination.

What makes this great chain of sources, channels, and sinks work is the Flume agent configuration, which is stored in a local text file that’s structured like a Java properties file. You can configure multiple agents in the same file. Look at an sample file, which is named flume-agent.conf — it’s set to configure an agent named shaman:

### Types of flume sources and sinks

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/flume/images/Types-of-Flume-Source-01-1.jpg)

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/flume/images/Types-of-Flume-Sinks-01.jpg)
```
# Identify the components on agent shaman:
shaman.sources = netcat_s1
shaman.sinks = hdfs_w1
shaman.channels = in-mem_c1
# Configure the source:
shaman.sources.netcat_s1.type = netcat
shaman.sources.netcat_s1.bind = localhost
shaman.sources.netcat_s1.port = 44444
# Describe the sink:
shaman.sinks.hdfs_w1.type = hdfs
shaman.sinks.hdfs_w1.hdfs.path = hdfs://<path>
shaman.sinks.hdfs_w1.hdfs.writeFormat = Text
shaman.sinks.hdfs_w1.hdfs.fileType = DataStream
# Configure a channel that buffers events in memory:
shaman.channels.in-mem_c1.type = memory
shaman.channels.in-mem_c1.capacity = 20000
shaman.channels.in-mem_c1.transactionCapacity = 100
# Bind the source and sink to the channel:
shaman.sources.netcat_s1.channels = in-mem_c1
shaman.sinks.hdfs_w1.channels = in-mem_c1
```

The configuration file includes properties for each source, channel, and sink in the agent and specifies how they’re connected. In this example, agent shaman has a source that listens for data (messages to netcat) on port 44444, a channel that buffers event data in memory, and a sink that logs event data to the console.

This configuration file could have been used to define several agents; here, you’re configuring only one to keep things simple.

To start the agent, use a shell script called flume-ng, which is located in the bin directory of the Flume distribution. From the command line, issue the agent command, specifying the path to the configuration file and the agent name.

The following sample command starts the Flume agent:

flume-ng agent -f /<path to flume-agent.conf> -n shaman
The Flume agent’s log should have entries verifying that the source, channel, and sink started successfully.

To further test the configuration, you can telnet to port 44444 from another terminal and send Flume an event by entering an arbitrary text string. If all goes well, the original Flume terminal will output the event in a log message that you should be able to see in the agent’s log.

## Flume Case Study: Website Log Aggregation

### Problem Statement

This case study focuses on a multi hop flume agent to aggregate the log reports from various web servers which have to be analyzed with the help of Hadoop. Consider a scenario we have multiple servers located in various locations serving from different data centers. The objective is to distribute the log files based on the device type and  store a backup of all logs. For example logs of US server has to be transferred based on the data center the server is located and copy all of the logs in the master database.


![alt text](https://github.com/samirsahoo007/bigdata/blob/master/flume/images/web-log.png)
 

In this case every server flume agent has a single source and two channels and sinks. One sending the data to the main database flume agent and other to the flume agent that is dividing the data based on the user agent present in the logs.

### Proposed Solution

Before aggregating the logs, configuration has to be set for various components in our architecture. In case of the web server flume system, as discussed two sinks are needed, channels to distribute the same data to both the destinations. In the beginning, define the names of the various components that are going to be used:

```
​server_agent.sources = apache_server
server_agent.channels = storage1 storage2
server_agent.sinks= sink1 sink2
The source is configured to execute the command in the shell to retrieve the data. It is assumed as a Apache2 server and the logs location hasn’t been changed. The location can be varied based on the requirement. Then introduce a header for each event defining the data center from which it originated

​server_agent.sources.apache_server.type = exec
server_agent.sources.apache_server.command = tail -f 
     /var/log/apache2/access.log
server_agent.sources.apache_server.batchSize = 1
server_agent.sources.apache_server.interceptors = int1
server_agent.sources.apache_server.interceptors.int1.type = static
server_agent.sources.apache_server.interceptors.int1.key = datacenter
server_agent.sources.apache_server.interceptors.int1.value = US
```

The sink is considered to be of avro sink retrieving events from the channel ‘storage1’. It is connected to the source of the master database flume agent which has to be of avro type. It has been defined to replicate all the events received by source to all the sources in the agent. The same goes with another sink with a different channel, IP and port number. We have choose two different channel as an event is successfully sent to one sink it is immediately deleted and can’t be sent to other sink.

```
source_agent.sinks.sink1.type = avro
source_agent.sinks.sink1.channel = storage1
source_agent.sinks.sink1.hostname = 
source_agent.sinks.sink1.port = 
source_agent.sinks.sink2.type = avro
source_agent.sinks.sink2.channel = storage2
source_agent.sinks.sink2.hostname = 
source_agent.sinks.sink2.port = 
source_agent.sources.apache_server.selector.type = replicating
```

The same configuration for all the server flume agents with just a variation in the datacenter value. The sink1 sends the data to be stored in the master database while sink2 sends data to divide the data and store them in different databases. The code for the user agent based flume agent is similar to the server agent code with additional feature of Multiplexing as different events have to be sent to different channels based on the header value. Select the header ‘datacenter’ and divide the data between channels c1 and c2 based on the value of the header.

```
​database_agent.sources.r1.selector.type = multiplexing
database_agent.sources.r1.selector.header = datacenter
database_agent.sources.r1.selector.mapping.ASIA = c1
database_agent.sources.r1.selector.mapping.US = c2
```

### Executing Solution

Start individual agents on each server using the following command:

```
​$ bin/flume-ng agent -n $agent_name -c conf -f
conf/flume-conf.properties.template
```

As the log reports are generated in the apache log file, the log reports are transferred to various servers as required without bandwidth or security concerns with better reliability.

Ref: https://www.dummies.com/programming/big-data/hadoop/log-data-with-flume-in-hdfs/
Twitter Data Streaming: https://www.edureka.co/blog/apache-flume-tutorial/
Types of flume source: https://data-flair.training/blogs/flume-source/
Types of flume sink: https://data-flair.training/blogs/flume-sink/
Create your first flume program: https://www.guru99.com/create-your-first-flume-program.html
User guide: https://flume.apache.org/FlumeUserGuide.html


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

### Message Queues
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

```
window1> python3 rabbit-receiver.py
window2> python3 rabbit-receiver.py
window3> python3 rabbit-source.py
window4> ruby rabbit-source.rb
```

kill/restart some and see what happens

Message passing example with Kafka:

kafka-producer.py
kafka-consumer.py
Let's try it...

```
window1> python3 kafka-consumer.py
window2> python3 kafka-consumer.py
window3> python3 kafka-producer.py
```

### Task Queues

The goal: get some work on a distributed queue. Maybe wait for results, or maybe don't.

Celery (Python).

Resque, Sidekiq (Ruby).

Google AppEngine Task Queues (Python, Java, Go, PHP).

Amazon Simple Workflow Service.

Any message queue + some code.

With a task queue, you get to just call a function (maybe with slightly different syntax). You can then retrieve the result (or just move on an let the work happen later).

Where the work happened is transparent.

A task with Celery: tasks.py.

Let's try it...

```
window1> celery -A tasks worker --loglevel=info --hostname=worker1@%h
window2> celery -A tasks worker --loglevel=info --hostname=worker2@%h
window3> ipython3
from tasks import add
result = add.delay(4, 4)
result.get(timeout=1)
```

Need a lot of work done without Hadoop? Run task queue workers on many nodes; make all the asynchronous calls you want; let the workers handle it.

Need nightly batch analysis done? Have a scheduled task start a Spark task.

Have a spike in usage? Let tasks queue up and process as possible. Or add more workers.

### Text Search

The goal: index lots of data so you (or your users) can search for records they want.

Apache Solr/Apache Lucene.

Elasticsearch.

Amazon CloudSearch.

All of these are designed to scale out across many nodes.

Indexing and searching with Elasticsearch:

elastic-index.py

elastic-search.py

Let's try it... (See also CourSys search when an instructor.)

```
python3 elastic-index.py
python3 elastic-search.py
curl -XGET 'http://localhost:9200/comments/_search?q=comment' | python3 -m json.tool
```

### Hadoop Distributions

The goal: Get a Hadoop cluster running without becoming an expert on Hadoop configuration.

Cloudera: what is running our cluster.

Hortonworks HDP.

MapR.

Amazon EMR: EC2 + Hadoop set up automatically.

### Another Scenario:

Real-time data is data with potentially high business value, but also with a perishable expiration date. If the value of the data is not realized in a certain window of time, its value is lost and the decision or action that was needed as a result never occurs. This category of big data comes in continuously and often quickly, so we call it streaming data. Streaming data needs special attention because a sudden price change, a critical threshold met, a sensor reading changing rapidly, or a blip in a log file can all be of immense value, but only if we are alerted in time.

There are four big names in big data technologies designed to handle time-sensitive, streaming data -- Kafka, Kinesis, Flume, and Storm. They are alike in their ability to process massive amounts of streaming data generated from social media, logging systems, click streams, Internet-of-Things devices, and so forth. However, each has a few distinctions, strengths, and weaknesses.

Kafka is one of the better-known streaming data processors. Born at LinkedIn, Kafka has been and is used by some big names in the industry, such as LinkedIn, Netflix, PayPal, Spotify, and Uber. In short, Kafka is a distributed messaging system that maintains feeds of messages called topics. Publishers write data to topics and subscribers read from topics. Kafka topics are partitioned and replicated across multiple nodes in your Hadoop cluster.

Kafka messages are simple, byte-long arrays that can store objects in virtually any format with a key attached to each message, so that all messages within a topic will arrive together within the same partition or be delivered to the same subscriber. Kafka is unique in how it treats each topic like a log file, and the messages within are ordered by a unique offset. To be efficient, subscribers must track their own location within each log, which allows Kafka to dedicate itself to processing data for large volumes of users and data with little overhead.

Kafka has a follow-on competitor -- Amazon Kinesis. Kafka and Kinesis are much the same under the hood. However, although Kafka is very fast and also free, it requires you to make it into an enterprise-class solution for your organization. Amazon filled that gap by offering Kinesis as an out-of-the-box streaming data tool with the speed and scale of Kafka in an enterprise-ready package. Kinesis has shards -- what Kafka calls partitions -- that Amazon users pay for by the shard-hour and payload.

Apache Flume is also a service for collecting large amounts of streaming data, particularly logs. Kafka and Kinesis require consumers to pull data. Flume pushes data to consumers using mechanisms it calls data sinks. Flume can push data to many popular sinks right out of the box, including HDFS, HBase, Cassandra, and some relational databases. Thus, it’s a quick starter, as opposed to Kafka, where you have to build your consumers’ ability to plug into the data stream from scratch. Kafka provides event replication, meaning if a node goes down, the others will pick up the slack and still make the data available. Flume does not. Thus, if your data is so mission-critical that if any loss is unacceptable, then Kafka is the way to go.

Finally, Apache Storm involves streaming data. Storm is the bridge between batch processing and stream processing, which Hadoop is not natively designed to handle. Storm runs continuously, processing a stream of incoming data and dicing it into batches, so Hadoop can more easily ingest it. Data sources are called spouts and each processing node is a bolt. Bolts perform computations and processes on the data, including pushing output to data stores and other services.

If you have a streaming data use case, you have some architectural decisions to make regarding which solution you should choose. If you want a fault-tolerant, do-it-yourself solution and you have the developers to support it, go with Kafka. If you need something that works out of the box, choose Kinesis or Flume, once you decide whether push or pull makes more sense. Finally, if streaming data is, for now, just a small add-on to your already developed Hadoop environment, Storm is a good choice.

Streaming data offers an opportunity for real-time business value. Knowing who's who in streaming data technologies and which one best integrates with your infrastructure will help you make the right architectural decisions.

Let's discuss an industry scenario which employs Spark to process data in real-time. The source of the data is Apache Flume. Flume is a service, which can move large amounts of data. It is usually disperse and can process all forms of data. Industries use Flume to process real-time log data.

### Flume Integration

There are two approaches to integrate flume with Spark Streaming

Push-based approach: Spark listens on particular port for Avro event and flume connects to that port and publishes event

Pull-based approach: You use special Spark Sink in flume that keeps collecting published data and Spark pulls that data at certain frequency

#### Push-based approach

In this approach, Spark Streaming sets up a receiver that acts as an Avro agent for Flume. You need:

a Spark worker to run on a specific machine (used in Flume configuration)
create an Avro sink in your Flume configuration to push data to a port on that machine
     agent.sinks = avroSink
     agent.sinks.avroSink.type = avro
     agent.sinks.avroSink.channel = memoryChannel
     agent.sinks.avroSink.hostname = localhost
     agent.sinks.avroSink.port = 33333

#### Pull-based approach

Instead of Flume pushing data directly to Spark Streaming, this approach runs a custom Flume sink allowing:

Flume to push data into the sink, and data stays buffered
Spark Streaming uses a reliable Flume receiver and transaction to pull data from the sink. This solution guarantees that a transaction succeeds only after data is recevide and replicated by Spark Streaming Therefore this solution guarantees stronger reliability and fault-tolerance and should be preferred when these requirements are mandatory, the difference with respect to the push-based approach is that you are required to configure Flume to run a custom sink.
To setup this configuration you need to:

select a machine that will run the custom sink in a Flume agent, this is where the Flume pipeline is configured to send data.
the Spark Streaming - Flume integration jar contains the custom sink implementation and it must be used to configure a Flume sink like
  agent.sinks = spark
  agent.sinks.spark.type = org.apache.spark.streaming.flume.sink.SparkSink
  agent.sinks.spark.hostname = localhost
  agent.sinks.spark.port = 33333
  agent.sinks.spark.channel = memoryChannel
Examples

Examples for these approaches are:

FlumeMultiPullBased

FlumeSinglePullBased

FlumeMultiPushBased

FlumeSinglePushBased

examples of flume configurations are provided in resources folder, you can also find a start.sh script that can be used to start Flume agent.

Push-based

To execute push-based examples you need to:

start Spark Streaming example. It creates a sink to which flume will connect to
start Flume pipeline, the provided configurations use a Flume source that monitors a file for new input lines

Pull-based

To execute pull-based examples you need to:

start Flume agent, it creates the pipeline with the configured custom sink
start Spark Streaming example. It connects to the custom sink to retrieve data

## Spark Streaming
Spark Streaming is a component of the Spark ecosystem that enables scalable, high-throughput, fault-tolerant stream processing of live data. Also, the source of this data can be any of the following: Kafka, Flume, TCP sockets, etc. The data can be processing can be done using complex algorithms, which expresses high-level functions like map, filter, flatMap, reduce, join, window, etc.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/flume/images/2-fig2.png)

# Flume vs Kafka

"What tool is the best for transporting data/logs across servers in a system?"

## Problems targeted by these systems

Flume is designed to ease the ingestion of data from one component to other.
It's focus is mostly on Hadoop although now it has sources and sinks for several other tools also, like Solr.

Kafka on the other hand is a messaging system that can store data for several days (depending on the data size of-course).
Kafka focuses more on the pipe while Flume focuses more on the end-points of the pipe.
That's why Kafka does not provide any sources or sinks specific to any component like Hadoop or Solr.
It just provides a reliable way of getting the data across from one system to another.
Kafka uses partitioning for achieving higher throughput of writes and uses replication for reliability and higher read throughput.

Push / Pull

Flume pushes data while Kafka needs the consumers to pull the data. Due to push nature, Flume needs some work at the consumers' end for replicating data-streams to multiple sinks. With Kafka, each consumer manages its own read pointer, so its relatively easy to replicate channels in Kafka and also much easier to parallelize data-flow into multiple sinks like Solr and Hadoop.

Latest trend is to use both Kafka and Flume together.

KafkaSource and KafkaSink for Flume are available which help in doing so.
The combination of these two gives a very desirable system because Flume's primary effort is to help ingest data into Hadoop and doing this in Kafka without Flume is a significant effort. Also note that Flume by itself is not sufficient for processing streams of data as Flume's primary purpose is not to store and replicate data streams. Hence it would be poor system if it uses only a single one of these two tools.

#### Persistence storage on disk

Kafka keeps the messages on disk till the time it is configured to keep them.
Thus if a Kafka broker goes offline for a while and comes back, the messages are not lost.

Flume also maintains a write-ahead-log which helps it to restore messages during a crash.

#### Flume error handling and transactional writes

Flume is meant to pass messages from source to sink (All of which implement Flume interfaces for get and put, thus treating Flume as an adapter). For example, a Flume log reader could send messages to a Flume sink which duplicates the incoming stream to Hadoop Flume Sink and Solr Flume Sink. For a chained system of Flume sources and sinks, Flume achieves reliability by using transactions - a sending Flume client does not close its write transaction unless the receiving client writes the data to its own Write-Ahead-Log and informs the sender about the same. If the receiver does not acknowledge the writing of WAL to the sender, then the sender marks this as a failure. The sender then begins to buffer all such events unless it can no longer hold any more. At this point, it begins to reject writes from its own upstream clients as well. 

# Apache Spark vs. MapReduce
## How did Spark become so efficient in data processing compared to MapReduce?

Hadoop MapReduce and Apache Spark are both Big Data processing tools.

### Core Definition

<p>
MapReduce is a programming model that is implemented in processing huge amounts of data.
MapReduce has been developed using Java
MapReduce Programs work in two phases:
The Map Phase
The Reduce Phase
The entire MapReduce process goes through the following 4 phases:

Splitting: The input is divided into a fixed size splits called input-splits. An input split is consumed by a single map.
Mapping: Here, data in each map is passed into a mapping function to produce output values.
Shuffling: This phase consumes the output of the mapping phase and the relevant records are consolidated.
Reducing: In this phase the relevant records are aggregated and a single output value is returned. This phase summarizes the complete dataset.
</p>

<p>
Apache Spark is an open-source, distributed processing system which is used for Big Data. Spark is an engine for large scale data processing.
Spark has been developed using Scala.
The main components of Apache Spark are as follows:
Apache Spark Core: It is the underlying general execution engine over which all other functionality is built. It provides in-memory computing and dataset references in external storage systems.
Spark SQL: It is the module which provides information about the data structure and the computation being performed
Spark Streaming: Allows processing of real-time data. This data is then processed using complex algorithms and pushed out to file systems, databases and live systems.
MLlib[Machine Learning]: It is a library that contains a wide array of machine learning algorithms and tools for constructing, evaluating and tuning ML pipelines.
GraphX: It comes with a library to manipulate graph databases and perform computations. It unifies ETL process, exploratory process and iterative graph computation within a single system.
</p>

### Processing Speed	

MapReduce reads and writes data from the disk. Though it is faster than traditional systems, it is substantially slower than Spark.	

Apache Spark runs on RAM, stores intermediate data in-memory reducing the number of read/write cycles to the disk. Hence it is faster than the classical MapReduce.


### Data Processing	

MapReduce was designed to perform Batch Processing for a voluminous amount of data. Hence, for extended data processing, it is dependent on different engines like Storm, Giraph, Impala, etc. Managing many different components adds to the hassle. MapReduce cannot process data interactively

Apache Spark Performs Batch Processing, Real-time processing, Iterative Processing, Graph Processing, Machine Learning and Streaming all in the same cluster. It thus accounts for a complete data analytics engine and is enough to handle all the requirements. Spark has the ability to process live streams efficiently. Spark can process data interactively.


### Memory Usage	

MapReduce does not support caching of Data.

Apache Spark Enhances the system performance by caching the data in-memory.

### Coding	

MapReduce requires handling low-level APIs due to which developers need to code each and every operation which makes it very difficult to work with.

Spark is easy to use and its Resilient Distributed Dataset helps to process data with its high-level operators. It provides rich APIs in Java, Scala, Python and R.

### Latency(Latency means Delay. It is the time the CPU has to wait to get a response after it makes a request to the RAM)

MapReduce has a high-latency computing framework.	

Spark provides a low latency computing.

### Recovery From Failure	

MapReduce is highly faulted tolerant and is resilient to system faults and failures. Here there is no need to restart the application from scratch in case of failure.	

Spark is also fault tolerant. Resilient Distributed Dataset [RDDs] allow for recovery of partitions on failed nodes. It also supports recovery by checkpointing to reduce the dependencies of an RDD. Hence, here too there is no need to restart the application from scratch in case of failure.

### Scheduler	

MapReduce is dependant on external job scheduler like Oozie to schedule its complex flows.	

Due to in-memory computation Spark acts like its own flow scheduler.

### Security	

MapReduce is comparatively more secure because of Kerberos. It also supports Access Control Lists (ACLs) which are traditional file permission model.	

Spark supports only one authentication which is the shared secret password authentication.


### Cost	

MapReduce is a cheaper option in terms of cost.	

Spark is costlier due to its in-memory processing power and RAM requirement.

### Function	

MapReduce is a Data Processing Engine.	

Spark is a Data Analytics Engine hence a choice for Data Scientist.


### Framework	

MapReduce is an open-source framework for writing data into HDFS and processing structured and unstructured data present in HDFS.	

Spark is an independent real-time processing engine that can be installed in any Distributed File System.


### Programming Language Supported	

MapReduce supports Java, C, C++, Ruby, Groovy, Perl, Python	

Spark supports Scala, Java, Python, R, SQL


### SQL Support

MapReduce Runs SQL queries using Apache Hive	

Spark Runs SQL queries using Spark SQL


### Hardware Requirement	

MapReduce can be run on commodity hardware.	

Apache Spark requires mid to high-level hardware configuration to run efficiently.

Hadoop requires a machine learning tool, one of which is Apache Mahout.	Spark has its own set of Machine Learning i.e. MLlib.

### Redundancy Check	

MapReduce does not support this feature.	

Spark processes every record exactly once and hence eliminates duplication.

## Conclusion

From the above comparison, it is quite clear that Apache Spark is a more advanced cluster computing engine than MapReduce. Due to its advanced features, it is now replacing MapReduce very quickly. However, MapReduce is an economical option. Furthermore, the intent of the business is a major factor in deciding the software to be used. There is no one size fits all in today’s market. Hence, it is a combination of technical, non-technical, economic and business factors that ultimately influence the software selection.
Spark can be deployed on a variety of platforms. It runs on Windows and UNIX (such as Linux and Mac OS) and can be deployed in standalone mode on a single node when it has a supported OS. Spark can also be deployed in a cluster node on Hadoop YARN as well as Apache Mesos. Spark is a Java Virtual Machine (JVM)-based distributed data processing engine that scales, and it is fast compared to many other data processing frameworks. Spark originated at the University of California at Berkeley and later became one of the top projects in Apache. 

Apache Spark includes several libraries to help build applications for machine learning (MLlib), stream processing (Spark Streaming), and graph processing (GraphX). 

To test the hypothesis that simple specialized frameworks provide value, we identified one class of jobs that were found to perform poorly on Hadoop by machine learning researchers at our lab — iterative jobs where a dataset is reused across a number of iterations. We built a specialized framework called Spark optimized for these workloads.

The biggest claim from Spark regarding speed is that it is able to "run programs up to 100x faster than Hadoop MapReduce in memory, or 10x faster on disk." Spark could make this claim because it does the processing in the main memory of the worker nodes and prevents the unnecessary I/O operations with the disks. The other advantage Spark offers is the ability to chain the tasks even at an application programming level without writing onto the disks at all or minimizing the number of writes to the disks.

How did Spark become so efficient in data processing compared to MapReduce? It comes with a very advanced directed acyclic graph (DAG) data processing engine. What it means is that for every Spark job, a DAG of tasks is created to be executed by the engine. The DAG in mathematical parlance consists of a set of vertices and directed edges connecting them. The tasks are executed as per the DAG layout.

In the case of MapReduce, the DAG consists of only two vertices, with one vertex for the map task and the other one for the reduce task. The edge is directed from the map vertex to the reduce vertex. The in-memory data processing combined with its DAG-based data processing engine makes Spark very efficient. In Spark's case, the DAG of tasks can be as complicated as it can. Thankfully, Spark comes with utilities that can give an excellent visualization of the DAG of any Spark job that is running. In a word count example, Spark's Scala code will look something like the following code snippet. The details of this programming aspects will be covered in the coming chapters:

val textFile = sc.textFile("README.md") 
val wordCounts = textFile.flatMap(line => line.split(" ")).map(word => 
(word, 1)).reduceByKey((a, b) => a + b) 
wordCounts.collect()
The web application that comes with Spark is capable of monitoring workers and applications. The DAG of the preceding Spark job generated on the fly will look like this:

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/spark.png)

In addition to the core data processing engine, Spark comes with a powerful stack of domain-specific libraries that use the core Spark libraries and provide various functionalities useful for various big data processing needs. The following table lists the supported libraries:

Bottom line: Spark performs better when all the data fits in memory, especially on dedicated clusters. Hadoop MapReduce is designed for data that doesn’t fit in memory, and can run well alongside other services.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/splunk_jenkins1.png)

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/spark_history.png)

Ref: https://www.slideshare.net/ishizaki/exploiting-gpus-in-spark

### RDD 
	is a fault-tolerant collection of elements that can be operated on in parallel.

### DataFrame
	is a Dataset organised into named columns. It is conceptually equivalent to a table in a relational database or a data frame in R/Python, but with richer optimisations under the hood.

### Dataset
	is a distributed collection of data. Dataset is a new interface added in Spark 1.6 that provides the benefits of RDDs (strong typing, ability to use powerful lambda functions) with the benefits of Spark SQL’s optimized execution engine.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/rdddfds.jpg)

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/rdddfds2.jpg)

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/Hadoop-MapReduce-vs-Apache-Spark.jpg)

![alt text](https://intellipaat.com/blog/wp-content/uploads/2016/07/Difference-between-MapReduce-and-Spark_A.jpg)

#### Q: Can you convert one to the other like RDD to DataFrame or vice-versa?

Yes, both are possible
1. RDD to DataFrame with .toDF()

val rowsRdd: RDD[Row] = sc.parallelize(
  Seq(
    Row("first", 2.0, 7.0),
    Row("second", 3.5, 2.5),
    Row("third", 7.0, 5.9)
  )
)

val df = spark.createDataFrame(rowsRdd).toDF("id", "val1", "val2")

df.show()
+------+----+----+
|    id|val1|val2|
+------+----+----+
| first| 2.0| 7.0|
|second| 3.5| 2.5|
| third| 7.0| 5.9|
+------+----+----+
more ways: Convert an RDD object to Dataframe in Spark

2. DataFrame/DataSet to RDD with .rdd() method

val rowsRdd: RDD[Row] = df.rdd() // DataFrame to RDD


Note:

Dataset of Rows (Dataset[Row]) in Scala/Java will often refer as DataFrames.

Also

val sampleRDD = sqlContext.jsonFile("hdfs://localhost:9000/jsondata.json")
val sample_DF = sampleRDD.toDF()

# Splunk

Splunk Enterprise can index many different kinds of data, as illustrated by the following diagram.
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/WhatSplunkCanIndex.jpg)

The Splunk App for Jenkins helps engineering teams, including developers, test/QA engineers and program managers as well as Jenkins admins to:
* Search,analyse and report
* Get instant visibility into test results.
* Gain instant and detailed insights into the progress and results of Jenkins builds.
* Monitor the health of Jenkins infrastructure.
	
	
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/splunk_jenkins1.png)




# Hue:

Hue(Hadoop User Experience) is a web-based interactive query editor that enables you to interact with data warehouses. It allows you to browse, analyze query (hive, pig or impala) and visualizie data. 
Hue Server is a "container" web application that sits in between your CDH installation and the browser. It hosts the Hue applications and communicates with various servers that interface with CDH components.
e.g. By default, for hive you are provided a hive shell which is used to submit query. Now, you can run the same query using hive query editor that comes with hue. 

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hue/images/hue.jpg)


## Features of Hue

* Hadoop API Access

* Presence of HDFS File Browser

* Browser and Job Designer

* User Admin Interface

* Editor for Hive Query

* Editor for Pig Query

* Hadoop Shell Access

* Workflows can access Oozie Interface

* SOLR searches can get a separate interface

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hue/images/hue_overview_central_region.png)

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hue/images/hue_4.5.png)
			open source SQL Assistant for Databases & Data Warehouses

* The left panel enables you to:

* Browse your databases

* Drill down to specific tables

* View HDFS directories and cloud storage

* Discover indexes and HBase or Kudu tables

* Find documents

The user can write SQL like queries and execution of these queries can produce MapReduce job by processing data and the job browser can be checked from the browser even when it is in running state.
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hue/images/hue_4_assistant_2.gif)


Connect to all the databases

Pick one of the multiple interpreters for Apache Hive, Apache Impala, Apache Presto and all the others too: MySQL, SparkSQL, Oracle, Apache Phoenix, KSQL, Elastic Search, Apache Druid, PostgreSQL, Redshift, BigQuery...

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hue/images/blog_top_search_.png)

Visually discover insights

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hue/images/dashboard_layout_dimensions.gif)


I can click on a document to open it up in appropriate query editor:
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hue/images/hue_hive_query_editor_1.png)

I can view and edit the query, and then run it on my cluster with a single click of the Execute button. After I do this, I can inspect the logs as the job runs:
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hue/images/hue_hive_query_log_1.png)

After the query runs to completion I can see the results, again with one click:
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hue/images/hue_hive_query_results_1.png)


![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hue/images/HIVE-VS-HUE.jpg)

## Job Browser
Hadoop ecosystems consist of many jobs and sometimes developers may need to know that which job is currently running on the Hadoop cluster and which job has been successfully completed and which has errors. Through Job browser, you can access all of the job-related information right from inside the browser. For this there is a button in Hue that can enlist the number of jobs and their status. Following image shows the job browser screen of Hue:Apache Hue Hadoop TutorialAbove image shows MapReduce type job that has been finished successfully. Along with Job ID, Application Type, Name, Status and Duration of the job is also listed with its time of submission and the name of the user that have. To show the job status, four color codes are used that are listed below:

For Successful Job – Green Code is Used

For Currently Running Jobs – Yellow color is Used

For Failed Jobs- Red Color is Used

For Manually Killed Jobs – Black Color is Used

If the user needs to access more information about any job then by clicking the job or Job ID user can access the job details. Moreover, another job-related information like in above case two subtasks were also performed for the above-listed job one is MapReduce and other is Reduce that is shown in the below image:
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hue/images/6-1.png)

So recent tasks for the job are displayed and that is MapReduce and Reduce. Here other job-related properties like metadata can also be accessed easily from the same platform. Information like the user who has submitted the job, Total execution duration of this job, the time when it was started and ended along with their temporary storage paths and tablespaces, etc can also be listed and checked through Hue job interface like shown in the below image:

## Oozie Workflows
Hue also provides the interface for Oozie workflow. All of the past and previous workflows of Hadoop cluster can be checked through this workflow interface. Again, three colors can be used to check the workflow status:

Successful Jobs – Green
Running Jobs – Yellow
Failed Job – Red

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hue/images/10.png)

New workflows can also be designed through this interface. An inbuilt Oozie editor is there that can be used to create new workflows just by using drag and drop interface.
