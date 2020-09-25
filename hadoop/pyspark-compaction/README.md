# HDFS Compaction using Apache Spark
HDFS is sensitive to the presence of small files. HDFS was developed to store and process large data sets over the range of terabytes and petabytes where data is expected to be stored in larger blocks(> 128MB). Though it may seem very trivial and often overlooked when architecting and deploying Hadoop applications. This often leads to “small files problem” affecting NN scalability , application scalability, and performance. For example - constant need of increasing NN heap, limiting the # of concurrent jobs run datasets with large # of small files etc..
This is a reusable generic HDFS file compaction tool,coded in java, runs on top of Apache Spark can be leveraged to compact HDFS files in Text, Parquet or Avro format.

 Please visit[https://blog.cloudera.com/small-files-big-foils-addressing-the-associated-metadata-and-application-challenges/] for more info. 


## Features

The compaction tool has a few good features which makes it a suitable tool:
- Supports wide variety of file formats - Avro, Parquet and Text 
- Supports various file compressions - bzip2, gzip, snappy and None
- Intelligently calculates the number of output file size to fill the HDFS block efficiently based on the input data, 
file format and compression

    Compression Ratio(assumed) 
    ```SNAPPY_RATIO = 1.7;  // (100 / 1.7) = 58.8 ~ 40% compression rate on text
    LZO_RATIO = 2.0;     // (100 / 2.0) = 50.0 ~ 50% compression rate on text
    GZIP_RATIO = 2.5;    // (100 / 2.5) = 40.0 ~ 60% compression rate on text
    BZ2_RATIO = 3.33;    // (100 / 3.3) = 30.3 ~ 70% compression rate on text
    ```

    Serialization Ratio(assumed) 
    ```AVRO_RATIO = 1.6; // (100 / 1.6) = 62.5 ~ 40% compression rate on text
    PARQUET_RATIO = 2.0;  // (100 / 2.0) = 50.0 ~ 50% compression rate on text
    ```

    Number of output files
    ```Input File Size Inflated = Input Compression Ratio * Input Serialization Ratio * Input File Size 
    Output File Size = Input File Size Inflated / ( Output Compression Ratio * Output Serialization Ratio ) 
    Number of Blocks Filled = Output File Size / Block Size of Output Directory
    Efficient Number of Files to Store = FLOOR( Number of Blocks Filled ) + 1
    ```
-   Can be used interactively as well in batch mode
-   Can employ with repartition or coalesce depending on the need. While repartition guarantees uniform  output file 
    size can perform poorly for vast amounts of data
-   Capability to incorporate a simple DQ check such as row count 
-   Offers a way to overwrite the original data, if needed
-   Has the ability to perform recursive compaction


## Build and Deploy

*   Setup the development environment
    *   Software required
        *   Apache-maven-3.6.1 & above
        *   Spark 2.0 & above
        *   Java 1.8 & above      

*   Clone the git project 
    ```
        git clone https://github.com/manaswinimaharana/spark-compaction.git
    ```
*   [optional] Import the project into IDE e.g. eclipse or Intellij, for making code changes

*   Deploy: Copy the "spark-compaction-0.0.1-SNAPSHOT.jar" to the cluster.e.g.
    ```
    scp -r target/spark-compaction-0.0.1-SNAPSHOT.jar username@<edgenode-hostname>:<target-path>
    ```
    **Note: You can always integrate it with enterprise standards of change control management to build and deploy the jar** 


## Execution

**Main Class Name**: org.cloudera.com.spark_compaction.HdfsCompact

**Input Parameters**

Name  | Description | Values
------------- | ------------- | -------------
input-path  | Path of the input hdfs directory to be compacted. Use “*” for compacting it recursively. But be aware when used recursively all the files within will be compacted and placed into a single output directory. e.g. hdfs:///landing/compaction/partition/date=2016-01-01/hour=*  | parameter type: mandatory
output-path  | Path of the output hdfs directory or temp directory if overwrite flag is set to “true”. e.g. /landing/compaction/partition/output_2016-01-01  | Parameter type: mandatory
input-compression  | Compression type of the input data  | Parameter type: mandatory, Acceptable values: none, snappy,gzip, bz2, lzo, Default: none
input-serialization  | Input serialization format or so called file format  | Parameter type: mandatory; Acceptable values: text, parquet, avro; Default: text
output-compression  | Compression type of the output data  | Parameter type: optional, Acceptable values: none, snappy,gzip, bz2, lzo, Default: none
output-serialization  | Output serialization format or so called file format  | Parameter type: mandatory; Acceptable values: text, parquet, avro; Default: text
partition-mechanism  | The partition function to be used  | Acceptable values: coalesce repartition, Default: coalesce
overwrite-flag  | Flag to determine if the input directory needs to be overwritten  |  Acceptable values: true, false, Default: false


**Batch Mode**

The Jar can be executed using “spark-submit” command 

```vim
spark2-submit \
  --class org.cloudera.com.spark_compaction.HdfsCompact \
  --master local[2] \
  ${JAR_PATH}/spark-compaction-0.0.1-SNAPSHOT.jar \
  --input-path ${INPUT_PATH} \
  --output-path ${OUTPUT_PATH} \
  --input-compression [none snappy gzip bz2 lzo] \
  --input-serialization [text parquet avro] \
  --output-compression [none snappy gzip bz2 lzo] \
  --output-serialization [text parquet avro] \
  --partition-mechanism [repartition coalesce] \
  --overwrite-flag [true false]
```

Example 

```spark2-submit \
  --packages com.databricks:spark-avro_2.11:4.0.0 \
  --conf spark.hadoop.avro.mapred.ignore.inputs.without.extension=false \
  --class org.cloudera.com.spark_compaction.HdfsCompact \
  --master yarn \
  --deploy-mode client \
  /tmp/spark-compaction-0.0.1-SNAPSHOT.jar \
  --input-path /user/hive/warehouse/customers \
  --output-path /user/hive/warehouse/customers_compacted5 \
  --input-compression none \
  --input-serialization parquet \
  --output-compression none \
  --output-serialization parquet \
  --partition-mechanism repartition \
  --overwrite-flag false
  ```
  
  
**Interactive Mode: PySpark Shell**

```vim 
$  pyspark2 --jars <path-to-spark-compaction-0.0.1-SNAPSHOT.jar>
Python 2.7.5 (default, Jun 20 2019, 20:27:34) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
19/09/05 12:38:02 WARN util.Utils: Service 'SparkUI' could not bind on port 4040. Attempting port 4041.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.3.0.cloudera5-SNAPSHOT
      /_/

Using Python version 2.7.5 (default, Jun 20 2019 20:27:34)
SparkSession available as 'spark'.
>>> from py4j.java_gateway import java_import
>>> URI = sc._gateway.jvm.java.net.URI
>>> java_import(sc._gateway.jvm,"org.cloudera.com.spark_compaction.HdfsCompact")
>>> func = sc._gateway.jvm.HdfsCompact()
>>> args= sc._gateway.new_array(sc._gateway.jvm.java.lang.String,12)
>>> args[0]='--input-path'
>>> args[1]='/tmp/compaction_input'
>>> args[2]='--output-path'
>>> args[3]='/tmp/compression_output400 '
>>> args[4]='--input-compression'
>>> args[5]='none'
>>> args[6]='--input-serialization'
>>> args[7]='text'
>>> args[8]='--output-compression'
>>> args[9]='none'
>>> args[10]='--output-serialization'
>>> args[11]='text'
>>> func.compact(args,sc._jsc) 

```

## Multiple Directory Compaction

**Sub Directory Processing**
```vim
$ hdfs dfs -du -h /landing/compaction/partition/
293.4 M  293.4 M  /landing/compaction/partition/date=2016-01-01

$ hdfs dfs -du -h /landing/compaction/partition/date=2016-01-01
48.9 M  48.9 M  /landing/compaction/partition/date=2016-01-01/hour=00
48.9 M  48.9 M  /landing/compaction/partition/date=2016-01-01/hour=01
48.9 M  48.9 M  /landing/compaction/partition/date=2016-01-01/hour=02
48.9 M  48.9 M  /landing/compaction/partition/date=2016-01-01/hour=03
48.9 M  48.9 M  /landing/compaction/partition/date=2016-01-01/hour=04
48.9 M  48.9 M  /landing/compaction/partition/date=2016-01-01/hour=05

$ hdfs dfs -du -h /landing/compaction/partition/date=2016-01-01/* | wc -l
6666
```

**Output Directory**
```vim
$ hdfs dfs -du -h /landing/compaction/partition/output_2016-01-01
293.4 M  293.4 M  /landing/compaction/partition/output_2016-01-01

$ hdfs dfs -du -h /landing/compaction/partition/output_2016-01-01/* | wc -l
3
```

**Wildcard for Multiple Sub Directory Compaction**
```vim
spark2-submit \
  --class com.github.KeithSSmith.spark_compaction.Compact \
  --master local[2] \
  ~/cloudera/jars/spark-compaction-0.0.1-SNAPSHOT.jar \
  --input-path hdfs:///landing/compaction/partition/date=2016-01-01/hour=* \
  --output-path hdfs:///landing/compaction/partition/output_2016-01-01 \
  --input-compression none \
  --input-serialization text \
  --output-compression none \
  --output-serialization text
```

## ASSUMPTIONS/CAVEATS

*   It should also be noted that if Avro is used as the output serialization only uncompressed and snappy compression are supported in the upstream package (spark-avro by Databricks) and the compression type will not be passed as part of the output file name. The other option that is not supported is Parquet + BZ2 and that will result in an execution error.
*   All the files within the directory are of same scheme, files format and compression
*   Input file format needs to be same as output file format, currently the script does not support cross-format compaction

## Future road map 
*   Add efficient logging
*   Add option to compact multiple directories using Multi-threading in Driver . Currently an external wrapper script is used to circumvent this. 
*   Add unit test cases
*   Improve the exception handling 
*   Incorporate advanced  Data quality checks 
*   Tune the code to handle large amount of data


### TL;DR
## Compression Math

At a high level this class will calculate the number of output files to efficiently fill the default HDFS block size on the cluster taking into consideration the size of the data, compression type, and serialization type.

**Compression Ratio Assumptions**
```vim
SNAPPY_RATIO = 1.7;     // (100 / 1.7) = 58.8 ~ 40% compression rate on text
LZO_RATIO = 2.0;        // (100 / 2.0) = 50.0 ~ 50% compression rate on text
GZIP_RATIO = 2.5;       // (100 / 2.5) = 40.0 ~ 60% compression rate on text
BZ2_RATIO = 3.33;       // (100 / 3.3) = 30.3 ~ 70% compression rate on text

AVRO_RATIO = 1.6;       // (100 / 1.6) = 62.5 ~ 40% compression rate on text
PARQUET_RATIO = 2.0;    // (100 / 2.0) = 50.0 ~ 50% compression rate on text
```

**Compression Ratio Formula**
```vim
Input Compression Ratio * Input Serialization Ratio * Input File Size = Input File Size Inflated
Input File Size Inflated / ( Output Compression Ratio * Output Serialization Ratio ) = Output File Size
Output File Size / Block Size of Output Directory = Number of Blocks Filled
FLOOR( Number of Blocks Filled ) + 1 = Efficient Number of Files to Store
```


### Text Compaction

**Text to Text Calculation**
```vim
Read Input Directory Total Size = x
Detect Output Directory Block Size = 134217728 => y

Output Files: FLOOR( x / y ) + 1 = # of Mappers
```

**Text to Text Snappy Calculation**
```vim
Default Block Size = 134217728 => y
Read Input Directory Total Size = x
Compression Ratio = 1.7 => r

Output Files: FLOOR( x / (r * y) ) + 1 = # of Mappers
```
To elaborate further, the following example has an input directory consisting of 9,999 files consuming 440 MB of space.  Using the default block size, the resulting output files are 146 MB in size, easily fitting into a data block.

**Input (Text to Text)**
```vim
$ hdfs dfs -du -h /landing/compaction/input | wc -l
9999
$ hdfs dfs -du -h /landing/compaction
440.1 M  440.1 M  /landing/compaction/input

440.1 * 1024 * 1024 = 461478298 - Input file size.
461478298 / 134217728 = 3.438
FLOOR( 3.438 ) + 1 = 4 files

440.1 MB / 4 files ~ 110 MB
```

**Output (Text to Text)**
```vim
$ hdfs dfs -du -h /landing/compaction/output
110.0 M  110.0 M  /landing/compaction/output/part-00000
110.0 M  110.0 M  /landing/compaction/output/part-00001
110.0 M  110.0 M  /landing/compaction/output/part-00002
110.0 M  110.0 M  /landing/compaction/output/part-00003
```


### Parquet Compaction

**Input (Parquet Snappy to Parquet Snappy)**
```vim
$ hdfs dfs -du -h /landing/compaction/input_snappy_parquet | wc -l
9999
$ hdfs dfs -du -h /landing/compaction
440.1 M  440.1 M  /landing/compaction/input_snappy_parquet

440.1 * 1024 * 1024 = 461478298 - Total input file size.
1.7 * 2 = 3.4 - Total compression ratio.
(3.4 * 461478298) / (3.4 * 134217728) = 3.438
FLOOR( 3.438 ) + 1 = 4 files

440.1 MB / 2 files ~ 110 MB
```

**Output (Parquet Snappy to Parquet Snappy)**
```vim
$ hdfs dfs -du -h /landing/compaction/output_snappy_parquet
110 M  110 M  /landing/compaction/output_snappy_parquet/part-00000.snappy.parquet
110 M  110 M  /landing/compaction/output_snappy_parquet/part-00001.snappy.parquet
110 M  110 M  /landing/compaction/output_snappy_parquet/part-00002.snappy.parquet
110 M  110 M  /landing/compaction/output_snappy_parquet/part-00003.snappy.parquet
```