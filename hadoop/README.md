# Installing hadoop on mac

### Install HomeBrew
```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Confirm you have the correct version of java (version 8) on your machine. If it returns anything other than 1.8., be sure to install the correct version.

```
$ java -version
$ brew cask install homebrew/cask-versions/adoptopenjdk8
```

### Install Hadoop
`
$ brew install hadoop
`		

### Configure Hadoop

Find java home path

```
$ /usr/libexec/java_home
```

Open the document containing the environment variable settings:

```
$ cd /usr/local/Cellar/hadoop/3.3.0/libexec/etc/hadoop/
$ open hadoop-env.sh
```

and Add the location for export JAVA_HOME

`
$ export JAVA_HOME="/Library/Java/JavaVirtualMachines/jdk-14.0.2.jdk/Contents/Home"
`

Replace information for export HADOOP_OPTS

```
change export HADOOP_OPTS="-Djava.net.preferIPv4Stack=true"
to export HADOOP_OPTS="-Djava.net.preferIPv4Stack=true -Djava.security.krb5.realm= -Djava.security.krb5.kdc="
```

Make changes to core files

```
$ open core-site.xml
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
  </property>
</configuration>
```

Make changes to hdfs files

```
$ open hdfs-site.xml
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
</configuration>
```

Make changes to mapred files

```
$ open mapred-site.xml
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
  <property>
    <name>mapreduce.application.classpath</name>   <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
  </property>
</configuration>
```

Make changes to yarn files

```
$ open yarn-site.xml

<configuration>
<property>
<name>yarn.nodemanager.aux-services</name>
<value>mapreduce_shuffle</value>
</property>
<property>
<name>yarn.nodemanager.env-whitelist</name>
<value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
</property>
</configuration>
```

**Remove password requirement**

Check if you're able to ssh(ssh localhost) without a password before moving to the next step to prevent unexpected results when formatting the NameNode.
If this does not return a last login time, use the following commands to remove the need to insert a password.

```
$ ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
$ chmod 0600 ~/.ssh/authorized_keys
```

Format NameNode

```
$ cd /usr/local/Cellar/hadoop/3.3.0/libexec/bin
$ hdfs namenode -format
```

A warning will tell you that a directory for logs is being created. You will be prompted to re-format filesystem in Storage Directory root. Say Y and press RETURN.

Run Hadoop

```
$ cd /usr/local/cellar/hadoop/3.3.0/libexec/sbin/
$ ./start-all.sh
$ jps
```

After running jps, you should have confirmation that all the parts of Hadoop have been installed and running. 
Open a web browser to see your configurations for the current session.

http://localhost:9870

### Issues:
What if you get the following error?
```
(venv363) Samirs-XYZ $ ./start-all.sh 
WARNING: Attempting to start all Apache Hadoop daemons as samirsahoo in 10 seconds.
WARNING: This is not a recommended production deployment configuration.
WARNING: Use CTRL-C to abort.
Starting namenodes on [localhost]
localhost: sameer_sahoo@localhost: Permission denied (publickey,password,keyboard-interactive).
Starting datanodes
localhost: sameer_sahoo@localhost: Permission denied (publickey,password,keyboard-interactive).
Starting secondary namenodes [Samirs-XYZ]
Samirs-XYZ: sameer_sahoo@samirs-mbp: Permission denied (publickey,password,keyboard-interactive).
2021-05-16 21:20:29,168 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Starting resourcemanager
resourcemanager is running as process 81524.  Stop it first.
Starting nodemanagers
localhost: sameer_sahoo@localhost: Permission denied (publickey,password,keyboard-interactive).
```
**Solution:**
Here the username sameer_sahoo may not have passwordless access that you've set above. If the passwordless setup is correct, then check the user...
e.g. in my case if you'd see, the username for which passwordless access was set is **samirsahoo** not **sameer_sahoo**
```
$ users
samirsahoo
```

So from where this username "sameer_sahoo" is coming from??? Check ~/.ssh/config ...; the username in "User"
Change **User** line from "User sameer_sahoo" to "User samirsahoo" and run ./start-all.sh again.

### Close Hadoop

$ ./stop-all.sh

# How to setup hive?

```
$ docker pull hivemall/latest:20170517      (Check the latest tag first https://hub.docker.com/r/hivemall/latest/tags/)

$ docker run -v /tmp/:/tmp/ -p 8088:8088 -p 50070:50070 -p 19888:19888 -it hivemall/latest:20170517
```

#### Note:

If you are seeing the following error and the container is starting up
```
+ /usr/local/hadoop/sbin/mr-jobhistory-daemon.sh start historyserver
chown: missing operand after ‘/usr/local/hadoop/logs’
Try 'chown --help' for more information.
historyserver running as process 711. Stop it first.
```

then make sure you've nothing like below in the /tmp (or mounted directory) and if it's there then just delete it and run the "docker run..." command again
```
  $ rm -rf /tmp/Jetty_*
  $ rm -rf /tmp/*_resources
  $ rm -rf /tmp/hadoop-root*
  $ rm -rf /tmp/yarn-*
```

## Load data into HDFS (optional) / Run Hivemall on Docker

You can find an example script to load data into HDFS in $HOME/bin/prepare_iris.sh. The script loads iris dataset into iris database:

```
$ cd $HOME && ./bin/prepare_iris.sh
> hive                                  Type hive to run (.hiverc automatically loads Hivemall functions)
hive> use iris;
hive> select * from iris_raw limit 5;
OK
1       Iris-setosa     [5.1,3.5,1.4,0.2]
2       Iris-setosa     [4.9,3.0,1.4,0.2]
3       Iris-setosa     [4.7,3.2,1.3,0.2]
4       Iris-setosa     [4.6,3.1,1.5,0.2]
5       Iris-setosa     [5.0,3.6,1.4,0.2]
```

#### Note:
1>
If you're getting the following error

```
Exception in thread "main" java.lang.RuntimeException: java.net.ConnectException: Call From 6b234181b60e/172.17.0.2 to localhost:9000 failed on connection exception: java.net.ConnectException: Connection refused; For more details see:  http://wiki.apache.org/hadoop/ConnectionRefused
```
then just do the following:

```
$ /usr/local/hadoop/sbin/stop-all.sh
$ hadoop namenode -format
$ /usr/local/hadoop/sbin/start-all.sh
```

2>
The following command(count query) may hang when there are millions of records
```
hive> select count(*) from iris_raw;
WARNING: Hive-on-MR is deprecated in Hive 2 and may not be available in the future versions. Consider using a different execution engine (i.e. tez, spark) or using Hive 1.X releases.
Query ID = root_20201030044544_51a590b9-9bf2-419c-85fe-aa6f10794c8e
Total jobs = 1
Launching Job 1 out of 1
Number of reduce tasks not specified. Estimated from input data size: 3
In order to change the average load for a reducer (in bytes):
  set hive.exec.reducers.bytes.per.reducer=<number>
In order to limit the maximum number of reducers:
  set hive.exec.reducers.max=<number>
In order to set a constant number of reducers:
  set mapreduce.job.reduces=<number>
Starting Job = job_1603988725836_0001, Tracking URL = http://5c1ac3a4d2f2:8088/proxy/application_1603988725836_0001/
Kill Command = /usr/local/hadoop/bin/hadoop job  -kill job_1603988725836_0001
```

It hangs at the line "Kill Command..."
Count query hangs when there are millions of records. We need to make a simple change to resolve this. As we're working on a single node setup let's replace "yarn" with "local" in marred-site.xml(/usr/local/hadoop/etc/hadoop/mapred-site.xml).

Update /usr/local/hadoop/etc/hadoop/mapred-site.xml

from

```
<?xml version="1.0"?>
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
</configuration>
```

to

```
<?xml version="1.0"?>
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>local</value>
  </property>
</configuration>
```

Once you prepared the iris database, you are ready to move on to our multi-class classification tutorial.(https://hivemall.incubator.apache.org/userguide/multiclass/iris_dataset.html)

Ref: https://hivemall.incubator.apache.org/userguide/docker/getting_started.html

## Accessing Hadoop management GUIs

```
YARN http://localhost:8088/
HDFS http://localhost:50070/
MR jobhistory server http://localhost:19888/
```

Note that you need to expose local ports e.g., by -p 8088:8088 -p 50070:50070 -p 19888:19888 on running docker image.

## Build Hivemall (optional)

In the container, Hivemall resource is stored in $HIVEMALL_PATH. You can build Hivemall package by cd $HIVEMALL_PATH && ./bin/build.sh.


## What is a sequence file

Sequence files are binary files containing serialized key/value pairs. You can compress a sequence file at the record (key-value pair) or block levels. This is one of the advantage of using sequence file. Also, sequebce files are binary files, they provide faster read/write than that of text file format.

### Problem With Small Files and Hadoop

Now, one of the main problem that sequence file format solves is the problem of processing too many small files in Hadoop. As you know Hadoop is not good for processing large number of small files as referencing (memory) large amounts of small files generates a lot of overhead for the namenode. Besides this memory overhead, the second problem arises in terms of number of mappers as more number of mappers will be executed for each files (as the file size is smaller than that of block).

### Solution: Sequence File

Sequence files allows you to solve this problem of small files. As sequence files are the files containing key-value pairs. So, you can use it to hold multiple key-value pairs where the key can be unique file metadata, like  filename+timestamp and value is the content of the ingested file. Now, this way you are  able to club too many small files as a single file and then you can use this for processing as an input for MapReduce. This is the reason why sequence files often are used in custom-written map-reduce programs.


# What is bytearray?

A bytearray is very similar to a regular python string (str in python2.x, bytes in python3). There is an important difference though, that is strings are immutable, whereas bytearrays are mutable (like a list of characters).

The Python bytearray() function returns bytearray object which is a mutable sequence of integers in the range 0 <= x < 256. Hence, bytearray() function allows one to manipulate its elements as the numbers in the 0-256 range or one-char strings.

```
bytearray([source[, encoding[, errors]]])
```

1: First parameter is Source (optional)

Source is an optional parameter that can be used to initialize the array in a few different ways:

    If the source is a string, encoding is required. You must also give the encoding (and optionally, errors) parameters; bytearray() then converts the string to bytes using str.encode().
    If the source is an integer, the array will have that size and will be initialized with null bytes.
    If the source is an object conforming to the buffer interface, a read-only buffer of the object will be used to initialize the bytes array.
    If the source is an iterable, it must be an iterable of integers in the range 0 <= x < 256, which are used as the initial contents of the array.
    Without an argument, the bytearray() method will create an array of size 0.

2: Second parameter is Encoding (optional)

Encoding is also optional. However, it is required if the source is a string. Examle: utf-8, ascii etc.

3: Third parameter is Error (optional)

```
>>> bytearray()  #without argument
bytearray(b' ')
>>> bytearray(3)  #array of bytes of given integer
bytearrey(b'\x00\x00\x00')
>>> bytearray([1,2,3])  #bytearray() in iterable list
bytearray(b'\x01\x02\x03') 
>>> bytearray('Python','utf-8')  #bytearray() and string
b'Python'
>>> bytearray('Python', 'ascii')
b'Python'



# Define the list
listdata = [72, 69, 76, 76, 79]
# Print the content of the list
print("\nThe dictionary values are :\n", listdata)
 
# Initialize bytearray object with list
byteArrayObject = bytearray(listdata)
# Print bytearray object value
print("\nThe output of bytearray() method :\n", byteArrayObject)
 
# Convert the bytearray object into  bytes object
byteObject = bytes(byteArrayObject)
# Print bytes object value
print("\nThe output of bytes() method :\n", byteObject)
 
print("\nThe ASCII values of bytes")
# Iterate the bytes object using loop
for val in byteObject:
  print(val,' ', end='')
 
print("\nThe string values of bytes")
# Iterate the bytes object using loop
for val in byteObject:
  print(chr(val),' ', end='')
```

# hiveContext in PySpark and Hive

Hive, as known was designed to run on MapReduce in Hadoopv1 and later it works on YARN and now there is spark on which we can run Hive queries. Hive is nothing but a way through which we implement mapreduce like a sql or atleast near to it.

It needs a execution engine. And Mapreduce, YARN, Spark served the purpose. Query return in Hive is converted to respective framework related code and is executed by that respective engine. Thats what Hive on Spark is. Runnning Hive queries on Spark.

Coming to SparkSQL, It is part of the Spark core framework which also runs on the spark core. Using Sparksql we can create structured data frames that we use in spark and also we can invoke Hive by creating Hivecontext. Once Hivecontext is created, just like a link to the hive metastore, you can access and query tables in Hive.

You can run Spark independently using Spark SQL. Spark SQL uses Hive metadata. So it can be connected to Hive Databases. If none presented then it will create one on the fly.

hive in general is slow, even running with Tez as execution engine. If you already have Spark it might be more interesting to look into using SparkSQL.

Apache spark enables near real time processing while apache hive supports only batch processing.

Apache spark is 100 times faster than map reduce programming which is the backend processing framework for hive.

Spark is more efficient in memory, all intermediate data between tasks is stored in memory. Where as hive uses mapreduce to store intermediate data in disk, which adds lot of overhead in performance.


# HiveContext and SQLContext

HiveContext is a super set of the SQLContext. Additional features include the ability to write queries using the more complete HiveQL parser, access to Hive UDFs, and the ability to read data from Hive tables.

**IMP**: one the key difference is using HiveContext you can use the new window function feature.
https://databricks.com/blog/2015/07/15/introducing-window-functions-in-spark-sql.html



# How to read a csv into pyspark without a java heap memory error

```
pyspark --num-executors 5 --driver-memory 2g --executor-memory 2g
```

If the file is, as you say, 65GB, the above submission tells spark to only use 2GB of available memory.

Try ramping the --driver-memory parameter to be slightly larger than the size of your .csv file.

e.g --driver-memory 70G

To explain why this is necessary:

Without a cluster with a distributed file system, your entire data set sits on your local drive. Spark allows you to split jobs up in an optimised way across a cluster - but without it linked to said cluster of separate machines all of your data will be loaded into your driver's memory. Thus, even though you have higher parallelism here, you need to allow the job to take up as much, or more space than your input file.


# Parquet

Parquet, an open source file format for Hadoop. Parquet stores nested data structures in a flat columnar format. Compared to a traditional approach where data is stored in row-oriented approach(e.g. CSV, TSV), parquet is more efficient in terms of storage and performance.

Parquet can be used in any Hadoop ecosystem like Hive , Impala, Pig, Spark

Parquet uses the record shredding and assembly algorithm which is superior to simple flattening of nested namespaces. Parquet is optimized to work with complex data in bulk and features different ways for efficient data compression and encoding types.  This approach is best especially for those queries that need to read certain columns from a large table. Parquet can only read the needed columns therefore greatly minimizing the IO.

Parquet stores binary data in a column-oriented way, where the values of each column are organized so that they are all adjacent, enabling better compression. It is especially good for queries which read particular columns from a "wide" (with many columns) table since only needed columns are read and IO is minimized. Read this for more details on Parquet.

When we are processing Big data, cost required to store such data is more (Hadoop stores data redundantly i.e. 3 copies of each file to achieve fault tolerance) along with the storage cost processing the data comes with CPU,Network IO, etc costs. As the data increases cost for processing and storage increases. Parquet is the choice of Big data as it serves both needs, efficient and performance in both storage and processing.

We cannot load text file directly into parquet table, we should first create an alternate table to store the text file and use insert overwrite command to write the data in parquet format. In order to test performance, we should run the queries in Multi-node cluster, where jobs are parallelized and run simultaneously.

Parquet file format consists of 2 parts –

> Data

> Metadata

Data is written first in the file and the metadata is written at the end for single pass writing. Let’s see the parquet file format first and then lets us have a look at the metadata.

A sample parquet file format is as below –

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/hadoop/images/Parque-Body.jpg)


## Advantages of using Parquet

There are several advantages to columnar formats.

Organizing by column allows for better compression, as data is more homogeneous. Columnar storage like Apache Parquet is designed to bring efficiency compared to row-based files like CSV. When querying, columnar storage you can skip over the non-relevant data very quickly. As a result, aggregation queries are less time consuming compared to row-oriented databases. This way of storage has translated into hardware savings and minimized latency for accessing data.

As we store data of the same type in each column, we can use encoding better suited to the modern processor's pipeline by making instruction branching more predictable.
e.g.
Columnar file formats store related types in rows, so they're easier to compress. This CSV file is relatively hard to compress.

first_name,age
ken,30
felicia,36
mia,2

This data is easier to compress when the related types are stored in the same row:

ken,felicia,mia
30,36,2

Parquet files are most commonly compressed with the Snappy compression algorithm. Snappy compressed files are splittable and quick to inflate. Big data systems want to reduce file size on disk, but also want to make it quick to inflate the flies and run analytical queries.

Apache Parquet works best with interactive and serverless technologies like AWS Athena, Amazon Redshift Spectrum, Google BigQuery and Google Dataproc.

## Difference Between Parquet and CSV

CSV is a simple and widely spread format that is used by many tools such as Excel, Google Sheets, and numerous others can generate CSV files. Even though the CSV files are the default format for data processing pipelines it has some disadvantages:

Amazon Athena and Spectrum will charge based on the amount of data scanned per query.

Google and Amazon will charge you according to the amount of data stored on GS/S3.

Google Dataproc charges are time-based.

Parquet has helped its users reduce storage requirements by at least one-third on large datasets, in addition, it greatly improved scan and deserialization time, hence the overall costs.

Parquet files are immutable. CSV files are mutable i.e. adding a row to a CSV file is easy. You can't easily add a row to a Parquet file.

```$ spark-shell
Scala> val sqlContext = new org.apache.spark.sql.SQLContext(sc)
Scala> val employee = sqlContext.read.json(“emplaoyee”)
Scala> employee.write.parquet("employee.parquet")
Scala> CTRL D

$ cd employee.parquet/
$ ls
_common_metadata
Part-r-00001.gz.parquet
_metadata
_SUCCESS

$ spark-shell
scala> val sqlContext = new org.apache.spark.sql.SQLContext(sc)
scala> val parqfile = sqlContext.read.parquet(“employee.parquet”)
scala> Parqfile.registerTempTable("employee")
scala> val allrecords = sqlContext.sql("SELeCT * FROM employee")
scala> allrecords.show()
+------+--------+----+
|  id  | name   |age |
+------+--------+----+
| 1201 | satish | 25 |
| 1202 | krishna| 28 |
| 1203 | amith  | 39 |
| 1204 | javed  | 23 |
| 1205 | prudvi | 23 |
+------+--------+----+
```

## Avro

Avro is an open source project with row-based storage format that provides data serialization and data exchange services for Apache Hadoop. ... Avro stores the data definition(schema) in JSON format making it easy to read and interpret; the data itself is stored in binary format making it compact and efficient.


Avro format is supported for the following connectors: Amazon S3, Azure Blob, Azure Data Lake Storage Gen1, Azure Data Lake Storage Gen2, Azure File Storage, File System, FTP, Google Cloud Storage, HDFS, HTTP, and SFTP.

Avro has a JSON like data model, but can be represented as either JSON or in a compact binary form. ... It has a direct mapping to and from JSON. It has a very compact format. The bulk of JSON, repeating every field name with every single record, is what makes JSON inefficient for high-volume usage.
