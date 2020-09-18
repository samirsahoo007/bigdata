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

Remove password requirement

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

### Close Hadoop

$ ./stop-all.sh


## What is a sequence file

Sequence files are binary files containing serialized key/value pairs. You can compress a sequence file at the record (key-value pair) or block levels. This is one of the advantage of using sequence file. Also, sequebce files are binary files, they provide faster read/write than that of text file format.

### Problem With Small Files and Hadoop

Now, one of the main problem that sequence file format solves is the problem of processing too many small files in Hadoop. As you know Hadoop is not good for processing large number of small files as referencing (memory) large amounts of small files generates a lot of overhead for the namenode. Besides this memory overhead, the second problem arises in terms of number of mappers as more number of mappers will be executed for each files (as the file size is smaller than that of block).

### Solution: Sequence File

Sequence files allows you to solve this problem of small files. As sequence files are the files containing key-value pairs. So, you can use it to hold multiple key-value pairs where the key can be unique file metadata, like  filename+timestamp and value is the content of the ingested file. Now, this way you are  able to club too many small files as a single file and then you can use this for processing as an input for MapReduce. This is the reason why sequence files often are used in custom-written map-reduce programs.
