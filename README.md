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

* **Oozie**: Job Scheduling, workflow monitoring
* **Chukwa**: Monitoring, data collection system for monitoring large distributed systems 
* **Flume, Sqoop** - (Monitoring)Data Ingesting Services(Flume plays on Unstructured/Semi-structured data; Sqoop plays on Structured data). More below
* **Logstash**: Server-side data processing pipeline that allows you to collect data from a variety of sources, transform it on the fly, and send it to your desired destination.
* **Filebeat**: It collects and sends the log files from tens, hundreds, or even thousands of servers, virtual machines, and containers to Logstash. In this way, all the logs and files can be indexed at a central location for analysis and visualization.
* **Zookeeper**: cluster management(provides a distributed configuration service, a synchronization service and a naming registry for distributed systems)
* **HIVE, PIG**: Query based processing of data services(SQL, Dataflow)
* **Mahout, Spark MLLib**: Machine Learning algorithm libraries
* **Avro**: (RPC)row-oriented remote procedure call and data serialization framework(uses JSON for defining data types and protocols,& serializes data in a compact binary format. Apache Spark SQL can access Avro as a data source)
* **Sqoop**: (RDBMS Connector) Data Ingesting Services on structured data
* **MapReduce**: Programming based Data Processing
* **YARN**: Cluster and resource management(Yet Another Resource Negotiator)
* **HDFS**: Hadoop Distributed File System
* **HBase**: Column DB Storage (NoSQL Database)
* **Spark**: In-Memory data processing
* **Solr, Lucene**: Searching and Indexing
* **Elasticsearch** - data store & analytics / search engine
* **Kibana** - data visualisation tool for Elasticsearch
* **Beeline** - Hive command line interface
* **Datasift** - online service that streams tweets matching a given pattern to a nominated datastore (such as MongoDB)
* **Ambari** - Provision, Monitor and Maintain cluster
* **Apache Drill** - SQL on Hadoop
* **Apache Storm** - real-time processing of data streams. It consists of higher level of abstraction than simple message passing (which permits describing topologies as a DAG), per-process fault-tolerance and definite at-least-once semantics for each message in the structure.
* **Kafka** is a scalable, high performance, low latency platform that allows reading and writing streams of data like a messaging system. 
* **Spark Streaming** is part of the Apache Spark platform that enables scalable, high throughput, fault tolerant processing of data streams.
* **Cassandra** is a distributed and wide-column NoSQL data store.
* **Hue**(Hadoop User Experience) is a web-based interactive query editor that enables you to interact with data warehouses. It allows you to browse, analyze query (hive, pig or impala) and visualizie data. 
* **Data Lakes**: A data lake is a storage repository that holds a large amount of data in its native, raw format.
* **Zeppelin**: Zeppelin is web-based notebook that enables interactive data analytics(data visulisation and exploration). 

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

### Defining the Hive table over Elasticsearch
```
CREATE EXTERNAL TABLE all_blog_posts_es (
ts_epoch bigint ,
post_title string ,
post_title_a string ,
post_author string ,
url string ,
post_type string )
ROW FORMAT SERDE 'org.elasticsearch.hadoop.hive.EsSerDe'
STORED BY 'org.elasticsearch.hadoop.hive.EsStorageHandler'
TBLPROPERTIES (
'es.nodes'='bigdatalite.localdomain',
'es.resource'='all_blog/posts'
) ;
```


### Apache Flume vs Logstash: What are the differences?
Both are "Log Management" tools.

Apache Flume is "A service for collecting, aggregating, and moving large amounts of log data". 
Logstash is detailed as "Collect, Parse, & Enrich Data". You can use it to collect logs, parse them, and store them for later use (like, for searching). 

If you store them in Elasticsearch, you can view and analyze them with Kibana.

When comparing Logstash vs Flume, the Slant community recommends Logstash for most people. In the question“What are the best log management, aggregation & monitoring tools?” Logstash is ranked 2nd while Flume is ranked 17th. 

Logstash’s main strongpoint is flexibility, due to the number of plugins.
while Logstash’s biggest con or “Achille’s heel” has always been performance and resource consumption (the default heap size is 1GB).

Logstash is used to gather logging messages, convert them into json documents and store them in an ElasticSearch cluster.
The minimal Logstash installation has one Logstash instance and one Elasticsearch instance. These instances are directly connected.

Logstash uses an input plugin to ingest data and an Elasticsearch output plugin to index the data in Elasticsearch, following the Logstash processing pipeline.

	Website logs--------------> Logstash --------------> Elastic search

### Log Analysis And End To End Big Data Analytics With ELK Stack
**What is the ELK Stack?**
ELK => Elasticsearch, Logstash, and Kibana

* E stands for ElasticSearch: It's a search server or NoSQL database based on Lucene. It provides a distributed, multitenant-capable full-text search engine with a RESTful web interface and schema-free JSON documents.
* L stands for LogStash : used for both shipping as well as processing and storing logs
* K stands for Kibana: is a visutalization tool (a web interface) which is hosted through Nginx or Apache

ELK Stack is designed to allow users to take to data from any source, in any format, and to search, analyze, and visualize that data in real time.
ELK provides centralized logging that be useful when attempting to identify problems with servers or applications. It allows you to search all your logs in a single place. It also helps to find issues that occur in multiple servers by connecting their logs during a specific time frame.

**Logstash**
Logstash is the data collection pipeline tool. It the first component of ELK Stack which collects data inputs and feeds it to the Elasticsearch. It collects various types of data from different sources, all at once and makes it available immediately for further use.

**Elasticsearch** is a NoSQL database which is based on Lucene search engine and is built with RESTful APIs. It is a highly flexible and distributed search and analytics engine. Also, it provides simple deployment, maximum reliability, and easy management through horizontal scalability. It provides advanced queries to perform detailed analysis and stores all the data centrally for quick search of the documents.

**Kibana** is a data visualization tool. It is used for visualizing the Elasticsearch documents and helps the developers to have an immediate insight into it. Kibana dashboard provides various interactive diagrams, geospatial data, timelines, and graphs to visualize the complex queries done using Elasticsearch. Using Kibana you can create and save custom graphs according to your specific needs.


![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/elk.png)

An use case:

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/ELK_stack_1.png)
nginx for reverse proxy

A more advanced...
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/elk_stack.svg)

The Logstash can directly consume the logs sent by **Filebeat** installed on the other systems to collectively parse the logs and files from multiple sources to be analyzed by using Kibana. The data flow involved in the ELK Stack using Filebeat is shown above.


A bit more advanced
![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/elk_stack.jpeg)

### Flume or Logstash? HDFS or Elasticsearch? … All of them!

Mark Rittman wrote back in April 2014 about using Apache Flume to stream logs from the Rittman Mead web server over to HDFS, from where they could be analysed in Hive and Impala.

Apache Logs -> Flume -> HDFS

Another route for analysing data is through the ELK stack.

Apache Logs -> Logstash -> HDFS

Using a single source is better in terms of load/risk to the source system, but less so for validating a bigger one. If I’m going to go with Elasticsearch as my target, Logstash would be the better fit source. 

The key points here are:

* One hit on the source system. In this case it’s flume, but it could be logstash, or another tool. This streams each line of the log file into Kafka in the exact order that it’s read.
* Kafka holds a copy of the log data, for a configurable time period. This could be days, or months - up to you and depending on purpose (and disk space!)
* Kafka is designed to be distributed and fault-tolerant. As with most of the boxes on this logical diagram it would be physically spread over multiple machines for capacity, performance, and resilience.
* The eventual targets, HDFS and Elasticsearch, are loaded by their respective tools pulling the web server entries exactly as they were on disk. In terms of validating end-to-end design we’re still doing that - we’re just pulling from a different source.
* The source server logs are streamed into Kafka, with a permanent copy up onto Amazon’s S3 for those real “uh oh” moments. Kafka, in a sandbox environment with a ham-fisted sysadmin, won’t be bullet-proof. Better to recover a copy from S3 than have to bother the Production server again. This is something I've put in for this specific use case, and wouldn't be applicable in others.
* From Kafka the web server logs are available to stream, as if natively from the web server disk itself, through Flume and Logstash.

A better/final pipeline:

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/elk_stack.png)

Ref: https://www.rittmanmead.com/blog/2015/10/forays-into-kafka-enabling-flexible-data-pipelines/

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/elasticsearch_ex2.jpeg)

Ref: https://medium.com/@manoharkush22/log-analysis-and-end-to-end-big-data-analytics-with-elk-stack-3e9d3f4e8b48

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

## What is the difference between Solr and Elasticsearch and which one is better?

* Solr is good for static data and Elasticsearch is for realtime/timeseries data

* Solr fits better into enterprise applications that already implement big data ecosystem tools, such as Hadoop and Spark. ... Elasticsearch is focused more on scaling, data analytics, and processing time series data to obtain meaningful insights and patterns. Its large-scale log analytics performance makes it quite popular.

* They are both built around the core underlying search library – Lucene – but they are different in terms of functionalities such as scalability, ease of deployment, as well as community presence and many more. Solr has more advantages when it comes to the static data, because of its caches and the ability to use an uninverted reader for faceting and sorting – for example, e-commerce. On the other hand, Elasticsearch is better suited – and much more frequently used – for timeseries data use cases, like log analysis use cases.  

# Data Lakes:
* A data lake is a storage repository that holds a large amount of data in its native, raw format. ... This approach differs from a traditional data warehouse, which transforms and processes the data at the time of ingestion. Advantages of a data lake: Data is never thrown away, because the data is stored in its raw format.

* A data lake is a centralized repository for hosting raw, unprocessed enterprise data. Data lakes can encompass hundreds of terabytes or even petabytes, storing replicated data from operational sources, including databases and SaaS platforms. They make unedited and unsummarized data available to any authorized stakeholder. Thanks to their potentially large (and growing) size and the need for global accessibility, they are often implemented in cloud-based, distributed storage.

* How does the data get into a data lake? Stakeholders, who may be business managers or data analytics professionals, begin by identifying important or interesting data sources. They then replicate the data from these sources to the data lake with few if any structural, organizational, or formatting transformations. Replicating the raw data allows businesses to simplify the data ingestion process while creating an integrated source of truth for uses such as data analytics or machine learning.

* Data stored in a lake can be anything, from completely unstructured data like text documents or images, to semistructured data such as hierarchical web content, to the rigidly structured rows and columns of relational databases. This flexibility means that enterprises can upload anything from raw data to the fully aggregated analytical results.

* The important point is that a data lake provides a single place to save and access valuable enterprise data. Without a good data lake, businesses increase the threshold of effort needed from stakeholders who would benefit from data.

* The Amazon **S3-based data lake** solution uses Amazon S3 as its primary storage platform. Amazon S3 provides an optimal foundation for a data lake because of its virtually unlimited scalability. You can seamlessly and nondisruptively increase storage from gigabytes to petabytes of content, paying only for what you use. Amazon S3 is designed to provide 99.999999999% durability. It has scalable performance, ease-of-use features, and native encryption and access control capabilities. Amazon S3 integrates with a broad portfolio of AWS and third-party ISV data processing tools.

## Data Ingestion Methods
One of the core capabilities of a data lake architecture is the ability to quickly and easily ingest multiple types of data, such as real-time streaming data and bulk data assets from on-premises storage platforms, as well as data generated and processed by legacy on-premises platforms, such as mainframes and data warehouses. AWS provides services and capabilities to cover all of these scenarios.

## Amazon Kinesis Firehose
Amazon Kinesis Firehose is a fully managed service for **delivering real-time streaming data directly to Amazon S3**. Kinesis Firehose automatically scales to match the volume and throughput of streaming data, and requires no ongoing administration. Kinesis Firehose can also be configured to transform streaming data before it’s stored in Amazon S3. Its transformation capabilities include compression, encryption, data batching, and Lambda functions.

Kinesis Firehose can compress data before it's stored in Amazon S3. It currently **supports GZIP, ZIP, and SNAPPY compression formats**. GZIP is the preferred format because it can be used by Amazon Athena, Amazon EMR, and Amazon Redshift. Kinesis Firehose encryption supports Amazon S3 server-side encryption with AWS Key Management Service (AWS KMS) for encrypting delivered data in Amazon S3. You can choose not to encrypt the data or to encrypt with a key from the list of AWS KMS keys that you own (see the section Encryption with AWS KMS). Kinesis Firehose can concatenate multiple incoming records, and then deliver them to Amazon S3 as a single S3 object. This is an important capability because it reduces Amazon S3 transaction costs and transactions per second load.

Finally, Kinesis Firehose can invoke Lambda functions to transform incoming source data and deliver it to Amazon S3. Common transformation functions include transforming Apache Log and Syslog formats to standardized JSON and/or CSV formats. The JSON and CSV formats can then be directly queried using **Amazon Athena**. If using a Lambda data transformation, you can optionally back up raw source data to another S3 bucket, as shown in the following figure.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/kinesis.png)
**Delivering real-time streaming data with Amazon Kinesis Firehose to Amazon S3 with optional backup**

## AWS Snowball

You can use AWS Snowball to securely and efficiently migrate bulk data from on-premises storage platforms and Hadoop clusters to S3 buckets. After you create a job in the AWS Management Console, a Snowball appliance will be automatically shipped to you. After a Snowball arrives, connect it to your local network, install the Snowball client on your on-premises data source, and then use the Snowball client to select and transfer the file directories to the Snowball device. The Snowball client uses AES-256-bit encryption. Encryption keys are never shipped with the Snowball device, so the data transfer process is highly secure. After the data transfer is complete, the Snowball’s E Ink shipping label will automatically update. Ship the device back to AWS. Upon receipt at AWS, your data is then transferred from the Snowball device to your S3 bucket and stored as S3 objects in their original/native format. Snowball also has an HDFS client, so data may be migrated directly from Hadoop clusters into an S3 bucket in its native format.

## AWS Storage Gateway

AWS Storage Gateway can be used to integrate legacy on-premises data processing platforms with an Amazon S3-based data lake. The File Gateway configuration of Storage Gateway offers on-premises devices and applications a network file share via an NFS connection. Files written to this mount point are converted to objects stored in Amazon S3 in their original format without any proprietary modification. This means that you can easily integrate applications and platforms that don’t have native Amazon S3 capabilities—such as on-premises lab equipment, mainframe computers, databases, and data warehouses—with S3 buckets, and then use tools such as Amazon EMR or Amazon Athena to process this data.

Additionally, Amazon S3 natively supports DistCP, which is a standard Apache Hadoop data transfer mechanism. This allows you to run DistCP jobs to transfer data from an on-premises Hadoop cluster to an S3 bucket. The command to transfer data typically looks like the following:

```
hadoop distcp hdfs://source-folder s3a://destination-bucket
```

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/data_lakes.png)

## Data Cataloging
The earliest challenges that inhibited building a data lake were keeping track of all of the raw assets as they were loaded into the data lake, and then tracking all of the new data assets and versions that were created by data transformation, data processing, and analytics. Thus, an essential component of an Amazon S3-based data lake is the data catalog. The data catalog provides a query-able interface of all assets stored in the data lake’s S3 buckets. The data catalog is designed to provide a single source of truth about the contents of the data lake.

There are two general forms of a data catalog: a comprehensive data catalog that contains information about all assets that have been ingested into the S3 data lake, and a Hive Metastore Catalog (HCatalog) that contains information about data assets that have been transformed into formats and table definitions that are usable by analytics tools like Amazon Athena, Amazon Redshift, Amazon Redshift Spectrum, and Amazon EMR. The two catalogs are not mutually exclusive and both may exist. The comprehensive data catalog can be used to search for all assets in the data lake, and the HCatalog can be used to discover and query data assets in the data lake.

## Comprehensive Data Catalog

The comprehensive data catalog can be created by using standard AWS services like AWS Lambda, Amazon DynamoDB, and Amazon Elasticsearch Service (Amazon ES). At a high level, Lambda triggers are used to populate DynamoDB tables with object names and metadata when those objects are put into Amazon S3 then Amazon ES is used to search for specific assets, related metadata, and data classifications. The following figure shows a high-level architectural overview of this solution.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/extracting_metadata_with_lambda.png)

          Comprehensive data catalog using AWS Lambda, Amazon DynamoDB, and Amazon Elasticsearch Service
        

## HCatalog with AWS Glue

AWS Glue can be used to create a Hive-compatible Metastore Catalog of data stored in an Amazon S3-based data lake. To use AWS Glue to build your data catalog, register your data sources with AWS Glue in the AWS Management Console. AWS Glue will then crawl your S3 buckets for data sources and construct a data catalog using pre-built classifiers for many popular source formats and data types, including JSON, CSV, Parquet, and more. You may also add your own classifiers or choose classifiers from the AWS Glue community to add to your crawls to recognize and catalog other data formats. The AWS Glue-generated catalog can be used by Amazon Athena, Amazon Redshift, Amazon Redshift Spectrum, and Amazon EMR, as well as third-party analytics tools that use a standard Hive Metastore Catalog. The following figure shows a sample screenshot of the AWS Glue data catalog interface.

## Amazon Athena

Amazon Athena is an **interactive query service** that makes it easy for you to analyze data directly in **Amazon S3 using standard SQL**. With a few actions in the AWS Management Console, you can use Athena directly against data assets stored in the data lake and begin using standard SQL to run ad hoc queries and get results in a matter of seconds.

**Athena is serverless**, so there is no infrastructure to set up or manage, and you only **pay for the volume of data assets scanned during the queries you run**. Athena scales automatically—executing queries in parallel—so results are fast, even with large datasets and complex queries. You can use Athena to process unstructured, semi-structured, and structured data sets. Supported data asset formats include **CSV, JSON, or columnar data formats such as Apache Parquet** and Apache ORC. **Athena integrates with Amazon QuickSight for easy visualization**. It can also be used with third-party reporting and business intelligence tools by connecting these tools to Athena with a JDBC driver.

Athena uses Presto, a distributed SQL engine to run queries. It also uses Apache Hive to create, drop, and alter tables and partitions. 
Athena charges you by the amount of data scanned per query. You can save on costs and get better performance if you partition the data, compress data, or convert it to columnar formats such as Apache Parquet.
## Amazon Redshift Spectrum
A second way to perform in-place querying of data assets in an Amazon S3-based data lake is to use Amazon Redshift Spectrum. Amazon Redshift is a large-scale, managed data warehouse service that can be used with data assets in Amazon S3. However, data assets must be loaded into Amazon Redshift before queries can be run. By contrast, Amazon Redshift Spectrum enables you to run Amazon Redshift SQL queries directly against massive amounts of data—up to exabytes—stored in an Amazon S3-based data lake. Amazon Redshift Spectrum applies sophisticated query optimization, scaling processing across thousands of nodes so results are fast—even with large data sets and complex queries. Redshift Spectrum can directly query a wide variety of data assets stored in the data lake, including **CSV, TSV, Parquet, Sequence, and RCFile**. Since Redshift Spectrum supports the SQL syntax of Amazon Redshift, you can run sophisticated queries using the same BI tools that you use today. You also have the flexibility to run queries that span both frequently accessed data assets that are stored locally in Amazon Redshift and your full data sets stored in Amazon S3. Because Amazon Athena and Amazon Redshift share a common data catalog and common data formats, you can use both Athena and Redshift Spectrum against the same data assets. 

You would typically use **Athena for adhoc data discovery and SQL querying, and then use Redshift Spectrum for more complex queries** and scenarios where a large number of data lake users want to run concurrent BI and reporting workloads.

## Data lakes vs. data warehouses
* In data warehouses Data is processed before integration but in data lakes Data is integrated in its raw and unstructured form
* In case of data warehouses mostly the users are Business users but in case of data lakes it's Data scientists
* In case of data warehouses Data is curated and adheres to data governance practices but in case of data lakes Data is more agile and does not necessarily comply with governance guidelines

# Zookeeper and Oozie: Hadoop Workflow and Cluster Managers
We generate petabytes of data every day, which is processed by farms of servers distributed across the geographical location of the globe. With big data seeping into every facet of our lives, we are trying to build robust systems which can process petabytes of data in a fast and accurate manner. Apache Hadoop, an open source framework is used widely for processing gigantic amounts of unstructured data on commodity hardware. Four core modules form the Hadoop Ecosystem: ?**Hadoop Common**, **HDFS**, **YARN** and **MapReduce**. On top of these modules, other components can also run alongside Hadoop, of which, Zookeeper and Oozie are the widely used Hadoop admin tools. Hadoop requires a workflow and cluster manager, job scheduler and job tracker to keep the jobs running smoothly. Apache Zookeeper and Oozie are the Hadoop admin tools used for this purpose.

We have heard a lot about the Distributed Systems and their processing power in the past. Hadoop’s main advantage is its ability to harness the power of distributed systems. A distributed system, in its simple term is a system comprising of various software components running on multiple physical machines independently and concurrently. But with distributed systems, one has to face many challenges like **message delays**, **processor speed**, **system failure**, **master detection**, **crash detection**, **metadata management** and etc. **All these challenges make the distributed systems faulty**. Having pointed this out, a perfect solution has not yet been achieved but **Zookeeper** provides a very simple, easy and nice framework to deal with these problems.

# Zookeeper: 
Apache Zookeeper is an application library, which primarily focuses on coordination between the distributed applications. It exposes simple services like naming, synchronization, configuration management and grouping services, in a very simple manner, relieving the developers to program them from start. It provides off the shelf support for queuing, and leader election.

* There was a huge issue of management of coordination and synchronization among the resources or the components of Hadoop which resulted in inconsistency, often. Zookeeper overcame all the problems by performing synchronization, inter-component based communication, grouping, and maintenance.

## What is the Data Model for Apache Zookeeper?
Apache Zookeeper has a file system-like data model, referred to as “Znode”. Just like a file system has directories, Znodes are also directories, and can have data associated with them. The ZNode can be referenced through absolute path separated with a slash. Each server in the ensemble, stores the Znode hierarchy in the memory, which makes the response quick and scalable as well. Each server maintains a transaction log - which logs each ‘write’ request on the disk. Before sending the response to the client, the transaction has to be synchronized on all the servers making it performance critical. Although it appears to be a file system based architecture, it is advisable that it shouldn’t be used as a general purpose file system. It should be used for storage of small amount of data so that it can be reliable, fast, scalable, available and should be in coordination to distributed application.

# Amazon EMR
Amazon EMR is a highly distributed computing framework used to quickly and easily process data in a cost-effective manner. Amazon EMR uses Apache Hadoop, an open source framework, to distribute data and processing across an elastically resizable cluster of EC2 instances and allows you to use all the common Hadoop tools such as Hive, Pig, Spark, and HBase. Amazon EMR does all the heavily lifting involved with provisioning, managing, and maintaining the infrastructure and software of a Hadoop cluster, and is integrated directly with Amazon S3. With Amazon EMR, you can launch a persistent cluster that stays up indefinitely or a temporary cluster that terminates after the analysis is complete. In either scenario, you only pay for the hours the cluster is up. Amazon EMR supports a variety of EC2 instance types encompassing general purpose, compute, memory and storage I/O optimized (e.g., T2, C4, X1, and I3) instances, and all Amazon EC2 pricing options (On-Demand, Reserved, and Spot). When you launch an EMR cluster (also called a job flow), you choose how many and what type of EC2 instances to provision. Companies with many different lines of business and a large number of users can build a single data lake solution, store their data assets in Amazon S3, and then spin up multiple EMR clusters to share data assets in a multi-tenant fashion.

# Oozie: 
* Oozie simply performs the task of a scheduler, thus scheduling jobs and binding them together as a single unit. 

## OOZIE ARCHITECTURE AND JOB SCHEDULING
Hadoop is designed to handle big amounts of data from many sources, and to carry out often complicated work of various types against that data across the cluster. That’s a lot of work, and the best way to get things done is to be organised with a schedule. That’s what Apache Oozie does. It schedules the work (jobs) in Hadoop.

Oozie enables users to enable multiple different tasks Hadoop, such as map/reduce tasks, pig jobs, sqoop jobs for moving SQL to Hadoop, etc, into a logical unit of work. This is managed via an Oozie Workflow which is a Directed Acyclical Graph  (DAG) of these tasks that are to be carried out. The DAG is stored in an XML Process Definition Language called hPDL.

### Oozie Architecture

An Oozie Server is deployed as Java Web Application hosted in a Tomcat server, and all of the stageful information such as workflow definitions, jobs,  etc, are stored in a database. This database can be either Apache Derby, HSQL, Oracle,  MySQL, or PostgreSQL.

There is an Oozie Client,  which is the client that submits work, either via a CLI, and API,  or a web service / REST.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/oozie/images/oozie-architecture-ong1.png)

Note that it is also possible to deploy Oozie in a High Availability configuration. In production environments where the goal of removing single points of failure is important, it is critical that the element that schedules your Hadoop jobs doesn’t fall down. Oozie enables high availability by enabling multiple instance of Oozie Servers to all point to the same database:

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/oozie/images/oozie-ha2.png)

For this to work, the database must be able to handle multiple concurrent connections. So, PostgreSQL, MySQL, or Oracle. To achieve true HA, you should also have a redundant Database, synchronised with the principal database to remove the database as a SPOF.

When workflow execution arrives in an Action node, it executes the specified Action, and then waits until a callback from the executed process returns before continuing the workflow. Actions can be of the following types:

* Hadoop fs
* map reduce
* ssh
* pig
* hive
* sqoop
* distcp
* email
* http
* custom action


There are two kinds of jobs .i.e Oozie workflow and Oozie coordinator jobs. 

Oozie Workflow jobs are Directed Acyclical Graphs (DAGs) of actions i.e. Oozie workflow is the jobs that need to be executed in a sequentially ordered manner.

Oozie Coordinator jobs are those that are triggered when some data or external stimulus is given to it. Oozie Coordinator jobs are recurrent Oozie Workflow jobs triggered by time (frequency) and data availability.

## Understanding it...
As a developer or data scientist, you rarely want to run a single serial job on an Apache Spark cluster. More often, to gain insight from your data you need to process it in multiple, possibly tiered steps, and then move the data into another format and process it even further. Perhaps you have a constant stream of data coming in and must kick off a job periodically, with dependent jobs that aggregate or further process the output. Something like this:

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/oozie/images/OozieImage1a.png)

This problem is easy to solve, right? You can write scripts that run jobs in sequence, and use the output of one program as the input to another—no problem. But what if your workflow is complex and requires specific triggers, such as specific data volumes or resource constraints, or must meet strict SLAs(service-level agreements)? What if parts of your workflow don't depend on each other and can be run in parallel?

Building your own infrastructure around this problem can seem like an attractive idea, but doing so can quickly become laborious. If, or rather when, those requirements change, modifying such a tool isn’t easy . And what if you need monitoring around these jobs? Monitoring requires another set of tools and headaches.

Enter Apache Oozie. Oozie is a workflow engine that can execute directed acyclic graphs (DAGs) of specific actions (think Spark job, Apache Hive query, and so on) and action sets. Oozie can also send notifications through email or Java Message Service (JMS) on events such as job state changes, or hit or missed SLAs.

**Amazon EMR**(Elastic MapReduce) offers **Oozie** 4.2.0, the latest version, with examples completely set up and ready to go right out of the box. We’ve added a number of user experience improvements that make starting and checking up on Oozie jobs simple. Also, our tools allow you to easily install the Oozie examples, which lets you quickly bootstrap your learning. In a few minutes, you can have everything you need to start prototyping (or just playing with) Oozie workflows.

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

#### Amazon EMR role in Amazon data pipeline
The EMR has a key role in the Amazon data pipeline, its main purpose is to process the inbound data for the Amazon infrastructure so that, after pre-processing and aggregating, the data can flow to the relational databases, S3 or Amazon Redshift.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/oozie/images/MF4.png)


#### A Simple Oozie Job

To get started with writing an Oozie application and running an Oozie job, we’ll create an Oozie workflow application named identity-WF that runs an identity MapReduce job. The identity MapReduce job just echoes its input as output and does nothing else. Hadoop bundles the IdentityMapper class and IdentityReducer class, so we can use those classes for the example.

In this example, after starting the identity-WF workflow, Oozie runs a MapReduce job called identity-MR. If the MapReduce job completes successfully, the workflow job ends normally. If the MapReduce job fails to execute correctly, Oozie kills the workflow. Figure 1-2 captures this workflow.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/oozie/images/apoo_0102.png)

The example Oozie application is built from the examples/chapter-01/identity-wf/ directory using the Maven command:

```
$ cd examples/chapter-01/identity-wf/
$ mvn package assembly:single
...
[INFO] BUILD SUCCESS
...
```
The identity-WF Oozie workflow application consists of a single file, the workflow.xml file. The Map and Reduce classes are already available in Hadoop’s classpath and we don't need to include them in the Oozie workflow application package.

The workflow.xml file in Example 1-1 contains the workflow definition of the application, an XML representation of Figure 1-2 together with additional information such as the input and output directories for the MapReduce job.

When running the workflow job, Oozie begins with the start node and follows the specified transition to identity-MR. The identity-MR node is a <map-reduce> action. The <map-reduce> action indicates where the MapReduce job should run via the job-tracker and name-node elements (which define the URI of the JobTracker and the NameNode, respectively). The prepare element is used to delete the output directory that will be created by the MapReduce job. If we don’t delete the output directory and try to run the workflow job more than once, the MapReduce job will fail because the output directory already exists. The configuration section defines the Mapper class, the Reducer class, the input directory, and the output directory for the MapReduce job. If the MapReduce job completes successfully, Oozie follows the transition defined in the ok element named success. If the MapReduce job fails, Oozie follows the transition specified in the error element named fail. The success transition takes the job to the end node, completing the Oozie job successfully. The fail transition takes the job to the kill node, killing the Oozie job.
	
The example application consists of a single file, workflow.xml. We need to package and deploy the application on HDFS before we can run a job. The Oozie application package is stored in a directory containing all the files for the application.

```
$ hdfs dfs -put target/example/ch01-identity ch01-identity
$ hdfs dfs -ls -R ch01-identity

/user/joe/ch01-identity/app
/user/joe/ch01-identity/app/workflow.xml
/user/joe/ch01-identity/data
/user/joe/ch01-identity/data/input
/user/joe/ch01-identity/data/input/input.txt
```

The Oozie workflow application is now deployed in the ch01-identity/app/ directory under the user’s HDFS home directory. We have also copied the necessary input data required to run the Oozie job to the ch01-identity/data/input directory.

Before we can run the Oozie job, we need a job.properties file in our local filesystem that specifies the required parameters for the job and the location of the application package in HDFS:

```
nameNode=hdfs://localhost:8020
jobTracker=localhost:8032
exampleDir=${nameNode}/user/${user.name}/ch01-identity
oozie.wf.application.path=${exampleDir}/app
```

The parameters needed for this example are jobTracker, nameNode, and exampleDir. The oozie.wf.application.path indicates the location of the application package in HDFS.

Let's submit a OOzie job:

```
$ export OOZIE_URL=http://localhost:11000/oozie
$ oozie job -run -config target/example/job.properties
job: 0000006-130606115200591-oozie-joe-W
```

We will cover Oozie’s command-line tool and its different parameters in detail later in "Oozie CLI Tool". For now, we just need to know that we can run an Oozie job using the -run option. And using the -config option, we can specify the location of the job.properties file.

We can also monitor the progress of the job using the oozie command-line tool:
```
$ oozie job -info 0000006-130606115200591-oozie-joe-W
Job ID : 0000006-130606115200591-oozie-joe-W
-----------------------------------------------------------------
Workflow Name : identity-WF
App Path      : hdfs://localhost:8020/user/joe/ch01-identity/app
Status        : RUNNING
Run           : 0
User          : joe
Group         : -
Created       : 2013-06-06 20:35 GMT
Started       : 2013-06-06 20:35 GMT
Last Modified : 2013-06-06 20:35 GMT
Ended         : -
CoordAction ID: -

Actions
-----------------------------------------------------------------
ID                                                 Status
-----------------------------------------------------------------
0000006-130606115200591-oozie-joe-W@:start:       OK   
-----------------------------------------------------------------
0000006-130606115200591-oozie-joe-W@identity-MR   RUNNING 
-----------------------------------------------------------------
When the job completes, the oozie command-line tool reports the completion state:

$ oozie job -info 0000006-130606115200591-oozie-joe-W
Job ID : 0000006-130606115200591-oozie-joe-W
-----------------------------------------------------------------
Workflow Name : identity-WF
App Path      : hdfs://localhost:8020/user/joe/ch01-identity/app
Status        : SUCCEEDED
Run           : 0
User          : joe
Group         : -
Created       : 2013-06-06 20:35 GMT
Started       : 2013-06-06 20:35 GMT
Last Modified : 2013-06-06 20:35 GMT
Ended         : 2013-06-06 20:35 GMT
CoordAction ID: -

Actions
-----------------------------------------------------------------
ID                                                 Status
-----------------------------------------------------------------
0000006-130606115200591-oozie-joe-W@:start:       OK   
-----------------------------------------------------------------
0000006-130606115200591-oozie-joe-W@identity-MR   OK 
-----------------------------------------------------------------
0000006-130606115200591-oozie-joe-W@success       OK
-----------------------------------------------------------------
The output of our first Oozie workflow job can be found in the ch01-identity/data/output directory under the user’s HDFS home directory:

$ hdfs dfs -ls -R ch01-identity/data/output

/user/joe/ch01-identity/data/output/_SUCCESS
/user/joe/ch01-identity/data/output/part-00000
```

The output of this Oozie job is the output of the MapReduce job run by the workflow job. We can also see the job status and detailed job information on the Oozie web interface, as shown in Figure 1-3.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/oozie/images/apoo_0103.png)

			Oozie workflow job on the Oozie web interface


This section has illustrated the full lifecycle of a simple Oozie workflow application and the typical ways to monitor it.

#### Some Oozie Usage Numbers

Oozie is widely used in several large production clusters across major enterprises to schedule Hadoop jobs. For instance, Yahoo! is a major user of Oozie and it periodically discloses usage statistics. In this section, we present some of these numbers just to give readers an idea about Oozie’s scalability and stability.

Yahoo! has one of the largest deployments of Hadoop, with more than 40,000 nodes across several clusters. Oozie is the primary workflow engine for Hadoop clusters at Yahoo! and is responsible for launching almost 72% of 28.9 million monthly Hadoop jobs as of January 2015. The largest Hadoop cluster processes 60 bundles and 1,600 coordinators, amounting to 80,000 daily workflows with 3 million workflow nodes. About 25% of the coordinators execute at frequencies of either 5, 10, or 15 minutes. The remaining 75% of the coordinator jobs are mostly hourly or daily jobs with some weekly and monthly jobs. Yahoo’s Oozie team runs and supports several complex jobs. Interesting examples include a single bundle with 200 coordinators and a workflow with 85 fork/join pairs.


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

More details here: https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/building-data-lake-aws.html

# Zeppelin
Zeppelin is web-based notebook that enables interactive data analytics(data visulisation and exploration).
You can make beautiful data-driven, interactive, collaborative document with SQL, code and even more!

Multi-purpose notebook which supports 20+ language backends.

* Data Ingestion
* Data Discovery
* Data Analytics
* Data Visualization & Collaboration

![http://zeppelin.apache.org/docs/0.8.1/index.html](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/zeppeline.png)

## Jupyter Vs Zeppelin: A Comprehensive Comparison Of Notebooks

- Zeppelin allows users to combine multiple paragraphs of code written in Python in one single line. The user can combine different data sources and its outputs in one single notebook for creating broad as well as cross-system reports.
- Jupyter being the oldest between among these two, the community is quite larger than Zeppelin and it supports much more external systems.
- Zeppelin has a separate interpreter configuration page
- Installation part is much easier in Jupyter than in Zeppelin
- Jupyter more than 85 of supported engines against Zeppelin’s interpreter types which have only around the 20.
- Both notebooks have markdown support but unlike Jupyter, Zeppelin creates interactive forms and the visualisation results in a faster way. 
- Right now, Jupyter has no such privacy configuration of the end users. On the other hand, in Zeppelin, you can create flexible security configurations for the end users in case they need any privacy for their codes.

## What is HDFS? How does it fit in the Apache Hadoop ecosystem?
HDFS (Hadoop Distributed File System) is a vital component of the Apache Hadoop project. Hadoop is an ecosystem of software that work together to help you manage big data. The two main elements of Hadoop are:

* **MapReduce** – responsible for executing tasks
* **HDFS** – responsible for maintaining data

### What is HDFS?
Hadoop Distributed File System is a fault-tolerant data storage file system that runs on commodity hardware. It was designed to overcome challenges traditional databases couldn’t. Therefore, its full potential is only utilized when handling big data.

The main issues the Hadoop file system had to solve were speed, cost, and reliability.

### What are the Benefits of HDFS?
The benefits of HDFS are, in fact, solutions that the file system provides for the previously mentioned challenges:

* **It is fast**. It can deliver more than 2 GB of data per second thanks to its cluster architecture.
* **It is free**. HDFS is an open-source software that comes with no licensing or support cost.
* **It is reliable**. The file system stores multiple copies of data in separate systems to ensure it is always accessible.

These advantages are especially significant when dealing with big data and were made possible with the particular way HDFS handles data.
**Note**: Hadoop is just one solution to big data processing. Another popular open-source framework is Spark.

### How Does HDFS Store Data?
HDFS divides files into blocks and stores each block on a DataNode. Multiple DataNodes are linked to the master node in the cluster, the NameNode. The master node distributes replicas of these data blocks across the cluster. It also instructs the user where to locate wanted information.

However, before the NameNode can help you store and manage the data, it first needs to partition the file into smaller, manageable data blocks. This process is called data block splitting.

### Data Block Splitting
By default, a block can be no more than 128 MB in size. The number of blocks depends on the initial size of the file. All but the last block are the same size (128 MB), while the last one is what remains of the file.

For example, an 800 MB file is broken up into seven data blocks. Six of the seven blocks are 128 MB, while the seventh data block is the remaining 32 MB.

Then, each block is replicated into several copies.

![](hadoop/images/data-block-splitting-in-hdfs.png)

### Data Replication
Based on the cluster’s configuration, the NameNode creates a number of copies of each data block using the replication method.

It is recommended to have at least three replicas, which is also the default setting. The master node stores them onto separate DataNodes of the cluster. The state of nodes is closely monitored to ensure the data is always available.

To ensure high accessibility, reliability, and fault-tolerance, developers advise setting up the three replicas using the following topology:

* Store the first replica on the node where the client is located.
* Then, store the second replica on a different rack.
* Finally, store the third replica on the same rack as the second replica, but on a different node.

![](hadoop/images/hdfs-data-replication.png)

### HDFS Architecture: NameNodes and DataNodes
HDFS has a master-slave architecture. The master node is the NameNode, which manages over multiple slave nodes within the cluster, known as DataNodes.

#### NameNodes
Hadoop 2.x introduced the possibility of having multiple NameNodes per rack. This novelty was quite significant since having a single master node with all the information within the cluster posed a great vulnerability.

The usual cluster consists of two NameNodes:

* an active NameNode
* and a stand-by NameNode
While the first one deals with all client-operations within the cluster, the second one keeps in-sync with all its work if there is a need for failover.

The active NameNode keeps track of the metadata of each data block and its replicas. This includes the file name, permission, ID, location, and number of replicas. It keeps all the information in an fsimage, a namespace image stored on the local memory of the file system. Additionally, it maintains transaction logs called EditLogs, which record all changes made on the system.

**Note**:Whenever a new block is added, replicated, or deleted, it gets recorded in the EditLogs.

The main purpose of the Stanby NameNode is to solve the problem of the single point of failure. It reads any changes made to the EditLogs and applies it to its NameSpace (the files and the directories in the data). If the master node fails, the Zookeeper service carries out the failover allowing the standby to maintain an active session.

![](hadoop/images/namenode-and-standby.png)

#### DataNodes
DataNodes are slave daemons that store data blocks assigned by the NameNode. As mentioned above, the default settings ensure each data block has three replicas. You can change the number of replicas, however, it is not advisable to go under three.

The replicas should be distributed in accordance with Hadoop’s Rack Awareness policy which notes that:

* The number of replicas has to be larger than the number of racks.
* One DataNode can store only one replica of a data block.
* One rack cannot store more than two replicas of a data block.

By following these guidelines, you can:

* Maximize network bandwidth.
* Protect against data loss.
* Improve performance and reliability.

![](hadoop/images/rack-placmement-policy-hdfs-e1597777931262.png)

**Note**: Hadoop’s scalability can be fully experienced if run on Bare Metal Cloud infrastructure, which provides hourly billing and the ability to provision thousands of servers with ease. 

### Key Features of HDFS

1. **Manages big data**. HDFS is excellent in handling large datasets and provides a solution that traditional file systems could not. It does this by segregating the data into manageable blocks which allow fast processing times.

2. **Rack-aware**. It follows the guidelines of rack awareness which ensures a system is highly available and efficient.

3. **Fault tolerant**. As data is stored across multiple racks and nodes, it is replicated. This means that if any of the machines within a cluster fails, a replica of that data will be available from a different node.

4. **Scalable**. You can scale resources according to the size of your file system. HDFS includes vertical and horizontal scalability mechanisms.

### HDFS Real Life Usage
Companies dealing with large volumes of data have long started migrating to Hadoop, one of the leading solutions for processing big data because of its storage and analytics capabilities.

* **Financial services**. The Hadoop Distributed File System is designed to support data that is expected to grow exponentially. The system is scalable without the danger of slowing down complex data processing.

* **Retail**. Since knowing your customers is a critical component for success in the retail industry, many companies keep large amounts of structured and unstructured customer data. They use Hadoop to track and analyze the data collected to help plan future inventory, pricing, marketing campaigns, and other projects.

* **Telecommunications**. The telecom industry manages huge amounts of data and has to process on a scale of petabytes. It uses Hadoop analytics to manage call data records, network traffic analytics, and other telecom related processes.

* **Energy industry**. The energy industry is always on the lookout for ways to improve energy efficiency. It relies on systems like Hadoop and its file system to help analyze and understand consumption patterns and practices.

* **Insurance**. Medical insurance companies depend on data analysis. These results serve as the basis for how they formulate and implement policies. For insurance companies, insight into client history is invaluable. Having the ability to maintain an easily accessible database while continually growing is why so many have turned to Apache Hadoop.

**Note**: Data stored in the HDSF is queried, managed, and analyzed by Apache Hive, a data warehouse system built on top of Hadoop.

## What is Hadoop Mapreduce and How Does it Work

MapReduce is a processing module in the Apache Hadoop project. Hadoop is a platform built to tackle big data using a network of computers to store and process data.

What is so attractive about Hadoop is that affordable dedicated servers are enough to run a cluster. You can use low-cost consumer hardware to handle your data.

Hadoop is highly scalable. You can start with as low as one machine, and then expand your cluster to an infinite number of servers. 


Hadoop MapReduce’s programming model facilitates the processing of big data stored on HDFS.

By using the resources of multiple interconnected machines, MapReduce effectively handles a large amount of structured and unstructured data.

![](hadoop/images/mapreduce-hdfs.png)

Before Spark and other modern frameworks, this platform was the only player in the field of distributed big data processing.

MapReduce assigns fragments of data across the nodes in a Hadoop cluster. The goal is to split a dataset into chunks and use an algorithm to process those chunks at the same time. The parallel processing on multiple machines greatly increases the speed of handling even petabytes of data.

### Distributed Data Processing Apps

This framework allows for the writing of applications for distributed data processing. Usually, Java is what most programmers use since Hadoop is based on Java.

However, you can write MapReduce apps in other languages, such as Ruby or Python. No matter what language a developer may use, there is no need to worry about the hardware that the Hadoop cluster runs on.

### Scalability

Hadoop infrastructure can employ enterprise-grade servers, as well as commodity hardware. MapReduce creators had scalability in mind. There is no need to rewrite an application if you add more machines. Simply change the cluster setup, and MapReduce continues working with no disruptions.

What makes MapReduce so efficient is that it runs on the same nodes as HDFS. The scheduler assigns tasks to nodes where the data already resides. Operating in this manner increases available throughput in a cluster.

### How MapReduce Works
At a high level, MapReduce breaks input data into fragments and distributes them across different machines.

The input fragments consist of key-value pairs. Parallel map tasks process the chunked data on machines in a cluster. The mapping output then serves as input for the reduce stage. The reduce task combines the result into a particular key-value pair output and writes the data to HDFS.

The Hadoop Distributed File System usually runs on the same set of machines as the MapReduce software. When the framework executes a job on the nodes that also store the data, the time to complete the tasks is reduced significantly.

### Basic Terminology of Hadoop MapReduce
As we mentioned above, MapReduce is a processing layer in a Hadoop environment. MapReduce works on tasks related to a job. The idea is to tackle one large request by slicing it into smaller units.

#### JobTracker and TaskTracker
In the early days of Hadoop (version 1), JobTracker and TaskTracker daemons ran operations in MapReduce. At the time, a Hadoop cluster could only support MapReduce applications.

A JobTracker controlled the distribution of application requests to the compute resources in a cluster. Since it monitored the execution and the status of MapReduce, it resided on a master node.

A TaskTracker processed the requests that came from the JobTracker. All task trackers were distributed across the slave nodes in a Hadoop cluster.

### YARN
Later in Hadoop version 2 and above, YARN became the main resource and scheduling manager. Hence the name Yet Another Resource Manager. Yarn also worked with other frameworks for the distributed processing in a Hadoop cluster.

### MapReduce Job
A MapReduce job is the top unit of work in the MapReduce process. It is an assignment that Map and Reduce processes need to complete. A job is divided into smaller tasks over a cluster of machines for faster execution.

The tasks should be big enough to justify the task handling time. If you divide a job into unusually small segments, the total time to prepare the splits and create tasks may outweigh the time needed to produce the actual job output.

### MapReduce Task
MapReduce jobs have two types of tasks.

A Map Task is a single instance of a MapReduce app. These tasks determine which records to process from a data block. The input data is split and analyzed, in parallel, on the assigned compute resources in a Hadoop cluster. This step of a MapReduce job prepares the <key, value> pair output for the reduce step.

A Reduce Task processes an output of a map task. Similar to the map stage, all reduce tasks occur at the same time, and they work independently. The data is aggregated and combined to deliver the desired output. The final result is a reduced set of <key, value> pairs which MapReduce, by default, stores in HDFS.

**Note**: The Reduce stage is not always necessary. Some MapReduce jobs do not require the combining of data from the map task outputs. These MapReduce Applications are called map-only jobs.

The Map and Reduce stages have two parts each.

The Map part first deals with the splitting of the input data that gets assigned to individual map tasks. Then, the mapping function creates the output in the form of intermediate key-value pairs.

The Reduce stage has a shuffle and a reduce step. Shuffling takes the map output and creates a list of related key-value-list pairs. Then, reducing aggregates the results of the shuffling to produce the final output that the MapReduce application requested.

### How Hadoop Map and Reduce Work Together
As the name suggests, MapReduce works by processing input data in two stages – Map and Reduce. To demonstrate this, we will use a simple example with counting the number of occurrences of words in each document.

The final output we are looking for is: How many times the words Apache, Hadoop, Class, and Track appear in total in all documents.

For illustration purposes, the example environment consists of three nodes. The input contains six documents distributed across the cluster. We will keep it simple here, but in real circumstances, there is no limit. You can have thousands of servers and billions of documents.


![](hadoop/images/map-reduce-diagram.png)

1. First, in the map stage, the input data (the six documents) is split and distributed across the cluster (the three servers). In this case, each map task works on a split containing two documents. During mapping, there is no communication between the nodes. They perform independently.

2. Then, map tasks create a <key, value> pair for every word. These pairs show how many times a word occurs. A word is a key, and a value is its count. For example, one document contains three of four words we are looking for: Apache 7 times, Class 8 times, and Track 6 times. The key-value pairs in one map task output look like this:

<apache, 7>
<class, 8>
<track, 6>
This process is done in parallel tasks on all nodes for all documents and gives a unique output.

3. After input splitting and mapping completes, the outputs of every map task are shuffled. This is the first step of the Reduce stage. Since we are looking for the frequency of occurrence for four words, there are four parallel Reduce tasks. The reduce tasks can run on the same nodes as the map tasks, or they can run on any other node.

The shuffle step ensures the keys Apache, Hadoop, Class, and Track are sorted for the reduce step. This process groups the values by keys in the form of <key, value-list> pairs.

4. In the reduce step of the Reduce stage, each of the four tasks process a <key, value-list> to provide a final key-value pair. The reduce tasks also happen at the same time and work independently.

In our example from the diagram, the reduce tasks get the following individual results:

<apache, 22>
<hadoop, 20>
<class, 18>
<track, 22>

**Note**: The MapReduce process is not necessarily successive. The Reduce stage does not have to wait for all map tasks to complete. Once a map output is available, a reduce task can begin.

5. Finally, the data in the Reduce stage is grouped into one output. MapReduce now shows us how many times the words Apache, Hadoop, Class, and track appeared in all documents. The aggregate data is, by default, stored in the HDFS.

The example we used here is a basic one. MapReduce performs much more complicated tasks.

Some of the use cases include:

Turning Apache logs into tab-separated values (TSV).
Determining the number of unique IP addresses in weblog data.
Performing complex statistical modeling and analysis.
Running machine-learning algorithms using different frameworks, such as Mahout.

### How Hadoop Partitions Map Input Data
The partitioner is responsible for processing the map output. Once MapReduce splits the data into chunks and assigns them to map tasks, the framework partitions the key-value data. This process takes place before the final mapper task output is produced.

MapReduce partitions and sorts the output based on the key. Here, all values for individual keys are grouped, and the partitioner creates a list containing the values associated with each key. By sending all values of a single key to the same reducer, the partitioner ensures equal distribution of map output to the reducer.

**Note**: The number of map output files depends on the number of different partitioning keys and the configured number of reducers. That amount of reducers is defined in the reducer configuration file.

The default partitioner well-configured for many use cases, but you can reconfigure how MapReduce partitions data.

If you happen to use a custom partitioner, make sure that the size of the data prepared for every reducer is roughly the same. When you partition data unevenly, one reduce task can take much longer to complete. This would slow down the whole MapReduce job.

The benefits of using MapReduce include parallel computing, error handling, fault-tolerance, logging, and reporting. This article provided the starting point in understanding how MapReduce works and its basic concepts.

Ref: https://phoenixnap.com/kb/hadoop-mapreduce



