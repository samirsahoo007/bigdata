What is Apache Cassandra?

Cassandra is a distributed database management system designed for
handling a high volume of structured data across commodity servers

Cassandra handles the huge amount of data with its distributed
architecture. Data is placed on different machines with more than one
replication factor that provides high availability and no single point
of failure.

In the image below, circles are Cassandra nodes and lines between the
circles shows distributed architecture, while the client is sending data
to the node.

**Cassandra Query Language (CQL)**.

\[hadoop\@linux bin\]\$ cqlsh

cqlsh\> help

Documented shell commands:

===========================

CAPTURE COPY DESCRIBE EXPAND PAGING SOURCE

CONSISTENCY DESC EXIT HELP SHOW TRACING.

CQL help topics:

================

ALTER CREATE\_TABLE\_OPTIONS SELECT

ALTER\_ADD CREATE\_TABLE\_TYPES SELECT\_COLUMNFAMILY

ALTER\_ALTER CREATE\_USER SELECT\_EXPR

ALTER\_DROP DELETE SELECT\_LIMIT

ALTER\_RENAME DELETE\_COLUMNS SELECT\_TABLE

cqlsh\> CAPTURE '/home/hadoop/CassandraProgs/Outputfile\'

When we type any command in the terminal, the output will be captured by
the file given. Given below is the command used and the snapshot of the
output file.

cqlsh:tutorialspoint\> select \* from emp;

Creating a Keyspace using Cqlsh

A keyspace in Cassandra is a namespace that defines data replication on
nodes. A cluster contains one keyspace per node. Given below is the
syntax for creating a keyspace using the statement **CREATE KEYSPACE**.

Syntax

CREATE KEYSPACE \<identifier\> WITH \<properties\>

i.e.

CREATE KEYSPACE "KeySpace Name"

WITH replication = {\'class\': 'Strategy name', \'replication\_factor\'
: 'No.Of replicas'};

CREATE KEYSPACE "KeySpace Name"

WITH replication = {\'class\': 'Strategy name', \'replication\_factor\'
: 'No.Of replicas'}

AND durable\_writes = 'Boolean value';

The CREATE KEYSPACE statement has two properties: **replication** and
**durable\_writes**.

cqlsh.\> CREATE KEYSPACE tutorialspoint

WITH replication = {\'class\':\'SimpleStrategy\',
\'replication\_factor\' : 3};

cqlsh\> DESCRIBE keyspaces;

tutorialspoint system system\_traces

cqlsh\> CREATE KEYSPACE test

\... WITH REPLICATION = { \'class\' : \'NetworkTopologyStrategy\',
\'datacenter1\' : 3 }

\... AND DURABLE\_WRITES = false;

Verification

You can verify whether the durable\_writes property of test KeySpace was
set to false by querying the System Keyspace. This query gives you all
the KeySpaces along with their properties.

cqlsh\> SELECT \* FROM system.schema\_keyspaces;

keyspace\_name \| durable\_writes \| strategy\_class \|
strategy\_options

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

test \| False \| org.apache.cassandra.locator.NetworkTopologyStrategy \|
{\"datacenter1\" : \"3\"}

tutorialspoint \| True \| org.apache.cassandra.locator.SimpleStrategy \|
{\"replication\_factor\" : \"4\"}

system \| True \| org.apache.cassandra.locator.LocalStrategy \| { }

system\_traces \| True \| org.apache.cassandra.locator.SimpleStrategy \|
{\"replication\_factor\" : \"2\"}

(4 rows)

Cassandra History

• Cassandra was first developed at Facebook for inbox search.

• Facebook open sourced it in July 2008.

• Apache incubator accepted Cassandra in March 2009.

• Cassandra is a top level project of
[Apache](https://www.guru99.com/apache.html) since February 2010.

• The latest version of Apache Cassandra is 3.2.1.

First let\'s understand what NoSQL database is.

Nosql Cassandra Database

NoSQL databases are called \"Not Only SQL\" or \"Non-relational\"
databases. NoSQL databases store and retrieve data other than tabular
relations such as relation databases.

NoSQL databases include MongoDB, HBase, and Cassandra.

There are following properties of NoSQL databases.

• Design Simplicity

• Horizontal Scaling

• High Availability

Data structures used in Cassandra are more specified than data
structures used in relational databases. Cassandra data structures are
faster than relational database structures.

NoSQL databases are increasingly used in Big Data and real-time web
applications. NoSQL databases are sometimes called Not Only
[SQL](https://www.guru99.com/sql.html) i.e. they may support SQL-like
query language.

Nosql Cassandra Database Vs Relational databases

Here are the differences between relation databases and NoSQL databases
in a tabular format.

  -------------------------------------------- -----------------------------------------------------------
  Relational Database                          NoSQL Database
  Handles data coming in low velocity          Handles data coming in high velocity
  Data arrive from one or few locations        Data arrive from many locations
  Manages structured data                      Manages structured unstructured and semi-structured data.
  Supports complex transactions (with joins)   Supports simple transactions
  single point of failure with failover        No single point of failure
  Handles data in the moderate volume.         Handles data in very high volume
  Centralized deployments                      Decentralized deployments
  Transactions written in one location         Transaction written in many locations
  Gives read scalability                       Gives both read and write scalability
  Deployed in vertical fashion                 Deployed in Horizontal fashion
  -------------------------------------------- -----------------------------------------------------------

Apache Cassandra Features

There are following features that Cassandra provides.

• Massively Scalable Architecture: Cassandra has a masterless design
where all nodes are at the same level which provides operational
simplicity and easy scale out.

• Masterless Architecture: Data can be written and read on any node.

• Linear Scale Performance: As more nodes are added, the performance of
Cassandra increases.

• No Single point of failure: Cassandra replicates data on different
nodes that ensures no single point of failure.

• Fault Detection and Recovery: Failed nodes can easily be restored and
recovered.

• Flexible and Dynamic Data Model: Supports datatypes with Fast writes
and reads.

• Data Protection: Data is protected with commit log design and build in
security like backup and restore mechanisms.

• Tunable Data Consistency: Support for strong data consistency across
distributed architecture.

• Multi Data Center Replication: Cassandra provides feature to replicate
data across multiple data center.

• Data Compression: Cassandra can compress up to 80% data without any
overhead.

• Cassandra Query language: Cassandra provides query language that is
similar like SQL language. It makes very easy for relational database
developers moving from relational database to Cassandra.

Cassandra Use Cases/Application

Cassandra is a non-relational database that can be used for different
types of applications. Here are some use cases where Cassandra should be
preferred.

• MessagingCassandra is a great database for the companies that provides
[Mobile](https://www.guru99.com/mobile-testing.html) phones and
messaging services. These companies have a huge amount of data, so
Cassandra is best for them.

• Internet of things ApplicationCassandra is a great database for the
applications where data is coming at very high speed from different
devices or sensors.

• Product Catalogs and retail appsCassandra is used by many retailers
for durable shopping cart protection and fast product catalog input and
output.

• Social Media Analytics and recommendation engineCassandra is a great
database for many online companies and social media providers for
analysis and recommendation to their customers.

The problem is that Cassandra's data model is different enough from that
of a traditional database to readily cause confusion, and just as
numerous as the misconceptions are the different ways that well
intentioned people use to correct them.

Some folks will describe the model as a *map of maps*, or in the case of
super columns, a *map of maps of maps*. Often, these explanations are
accompanied by visual aids that use a JSON-like notation to demonstrate.
Others will liken column families to sparse tables, and others still as
containers that hold collections of column objects. Columns are even
sometimes referred to as 3-tuples. All of these fall short in my
opinion.

The problem is that it's difficult to explain something new without
using analogies, but confusing when the comparisons don't hold up.

**Twitter**

Despite being an [actual
use-case](http://nosql.mypopescu.com/post/407159447/cassandra-twitter-an-interview-with-ryan-king)
for Cassandra, [Twitter](http://twitter.com/) is also an excellent
vehicle for discussion since it is well known and easily conceptualized.
We know for example that, like most sites, user information (screen
name, password, email address, etc), is kept for everyone and that those
entries are linked to one another to map friends and followers. And, it
wouldn't be Twitter if it weren't storing tweets, which in addition to
the 140 characters of text are also associated with meta-data like
timestamp and the unique id that we see in the URLs.

Were we modelling this in a relational database the approach would be
pretty straight-forward, we'd need a table to store our users.

CREATE TABLE user (

id INTEGER PRIMARY KEY,

username VARCHAR(64),

password VARCHAR(64)

);

We'd need tables we could use to perform the one-to-many joins to return
followers and followees.

CREATE TABLE followers (

user INTEGER REFERENCES user(id),

follower INTEGER REFERENCES user(id)

);

CREATE TABLE following (

user INTEGER REFERENCES user(id),

followed INTEGER REFERENCES user(id)

);

And of course we'd need a table to store the tweets themselves.

CREATE TABLE tweets (

id INTEGER,

user INTEGER REFERENCES user(id),

body VARCHAR(140),

timestamp TIMESTAMP

);

I've greatly oversimplified things here for the purpose of
demonstration, but even with a trivial model like this, there is much to
be taken for granted. For example, to accomplish data normalization like
this in a practical way we need foreign-key constraints, and since we
need to perform joins to combine data from multiple tables, we'll need
to be able to arbitrarily create indices on the appropriate attributes
to make that efficient.

But getting distributed systems right is a real challenge, and it never
comes without trade-offs. This is true of Cassandra and is why the data
model above won't work for us. For starters, there is no referential
integrity, and the lack of support for secondary indexing makes it
difficult to efficiently perform joins, so you must denormalize. Put
another way, you're forced to think in terms of the queries you'll
perform and the results you expect since this is likely what the model
will look like.

**============== Another Example ========**

To create the example, we want to use something that is complex enough
to show the various data structures and basic API operations, but not
something that will bog you down with details. In order to get enough
data in the database to make our searches work right (by finding stuff
we're looking for and leaving out stuff we're not looking for), there's
a little redundancy in the prepopulation of the database. Also, I wanted
to use a domain that's familiar to everyone so we can concentrate on how
to work with Cassandra, not on what the application domain is all about.

NOTE

The code in this chapter has been tested against the 0.7 beta 1 release,
and works as shown. It is possible that API changes may necessitate
minor tuning on your part, depending on your version.

Data Design

When you set out to build a new data-driven application that will use a
relational database, you might start by modeling the domain as a set of
properly normalized tables and use foreign keys to reference related
data in other tables. Now that we have an understanding of how Cassandra
stores data, let's create a little domain model that is easy to
understand in the relational world, and then see how we might map it
from a relational to a distributed hashtable model in Cassandra.

Relational modeling, in simple terms, means that you start from the
conceptual domain and then represent the nouns in the domain in tables.
You then assign primary keys and foreign keys to model relationships.
When you have a many-to-many relationship, you create the join tables
that represent just those keys. The join tables don't exist in the real
world, and are a necessary side effect of the way relational models
work. After you have all your tables laid out, you can start writing
queries that pull together disparate data using the relationships
defined by the keys. The queries in the relational world are very much
secondary. It is assumed that you can always get the data you want as
long as you have your tables modeled properly. Even if you have to use
several complex subqueries or join statements, this is usually true.

By contrast, in Cassandra you don't start with the data model; you start
with the query model.

For this example, let's use a domain that is easily understood and that
everyone can relate to: a hotel that wants to allow guests to book a
reservation.

Our conceptual domain includes hotels, guests that stay in the hotels, a
collection of rooms for each hotel, and a record of the reservation,
which is a certain guest in a certain room for a certain period of time
(called the "stay"). Hotels typically also maintain a collection of
"points of interest," which are parks, museums, shopping galleries,
monuments, or other places near the hotel that guests might want to
visit during their stay. Both hotels and points of interest need to
maintain geolocation data so that they can be found on maps for mashups,
and to calculate distances.

NOTE

Obviously, in the real world there would be many more considerations and
much more complexity. For example, hotel rates are notoriously dynamic,
and calculating them involves a wide array of factors. Here we're
defining something complex enough to be interesting and touch on the
important points, but simple enough to maintain the focus on learning
Cassandra.

Here's how we would start this application design with Cassandra. First,
determine your queries. We'll likely have something like the following:

▪ Find hotels in a given area.

▪ Find information about a given hotel, such as its name and location.

▪ Find points of interest near a given hotel.

▪ Find an available room in a given date range.

▪ Find the rate and amenities for a room.

▪ Book the selected room by entering guest information.

Hotel App RDBMS Design

[Figure 4-1](https://www.oreilly.com/library/view/cassandra-the-definitive/9781449399764/ch04.html#fig-sa.rdbmshotel)
shows how we might represent this simple hotel reservation system using
a relational database model. The relational model includes a couple of
"join" tables in order to resolve the many-to-many relationships of
hotels-to-points of interest, and for rooms-to-amenities.

![](media/image1.png){width="6.688888888888889in"
height="3.962209098862642in"}

*Figure 4-1. A simple hotel search system using RDBMS*

Hotel App Cassandra Design

Although there are many possible ways to do it, we could represent the
same logical data model using a Cassandra physical model such as that
shown in
[Figure 4-2](https://www.oreilly.com/library/view/cassandra-the-definitive/9781449399764/ch04.html#fig-sa.casshotel).

![](media/image2.png){width="6.688888888888889in"
height="6.786457786526684in"}

*Figure 4-2. The hotel search represented with Cassandra's model*

In this design, we're doing all the same things as in the relational
design. We have transferred some of the tables, such as Hotel and Guest,
to column families. Other tables, such as PointOfInterest, have been
denormalized into a super column family. In the relational model, you
can look up hotels by the city they're in using a SQL statement. But
because we don't have SQL in Cassandra, we've created an index in the
form of the HotelByCity column family.

NOTE

I'm using a stereotype notation here, so \<\<CF\>\> refers to a column
family, \<\<SCF\>\> refers to a super column family, and so on.

We have combined room and amenities into a single column family, Room.
The columns such as type and rate will have corresponding values; other
columns, such as hot tub, will just use the presence of the column name
itself as the value, and be otherwise empty.

Hotel Application Code

In this section we walk through the code and show how to implement the
given design. This is useful because it illustrates several different
API functions in action.

WARNING

The purpose of this sample application is to show how different ideas in
Cassandra can be combined. It is by no means the only way to transfer
the relational design into this model. There is a lot of low-level
plumbing here that uses the Thrift API. Thrift is (probably) changing to
Avro, so although the basic ideas here work, you don't want to follow
this example in a real application. Instead, check out
[Chapter 8](https://www.oreilly.com/library/view/cassandra-the-definitive/9781449399764/ch08.html)
and use one of the many available third-party clients for Cassandra,
depending on the language that your application uses and other needs
that you have.

The application we're building will do the following things:

1 Create the database structure.

2 Prepopulate the database with hotel and point of interest data. The
hotels are stored in standard column families, and the points of
interest are in super column families.

3 Search for a list of hotels in a given city. This uses a secondary
index.

4 Select one of the hotels returned in the search, and then search for a
list of points of interest near the chosen hotel.

5 Booking the hotel by doing an insert into the Reservation column
family should be straightforward at this point, and is left to the
reader.

Space doesn't permit implementing the entire application. But we'll walk
through the major parts, and finishing the implementation is just a
matter of creating a variation of what is shown.

Creating the Database

The first step is creating the schema definition. For this example,
we'll define the schema in YAML and then load it, although you could
also use client code to define it.

The YAML file shown in
[Example 4-1](https://www.oreilly.com/library/view/cassandra-the-definitive/9781449399764/ch04.html#ex-sa.schema)
defines the necessary keyspace and column families.

*Example 4-1. Schema definition in cassandra.yaml*

keyspaces:

\- name: Hotelier

replica\_placement\_strategy:
org.apache.cassandra.locator.RackUnawareStrategy

replication\_factor: 1

column\_families:

\- name: Hotel

compare\_with: UTF8Type

\- name: HotelByCity

compare\_with: UTF8Type

\- name: Guest

compare\_with: BytesType

\- name: Reservation

compare\_with: TimeUUIDType

\- name: PointOfInterest

column\_type: Super

compare\_with: UTF8Type

compare\_subcolumns\_with: UTF8Type

\- name: Room

column\_type: Super

compare\_with: BytesType

compare\_subcolumns\_with: BytesType

\- name: RoomAvailability

column\_type: Super

compare\_with: BytesType

compare\_subcolumns\_with: BytesType

This definition provides all of the column families to run the example,
and a couple more that we don't directly reference in the application
code, because it rounds out the design as transferred from RDBMS.

Loading the schema

Once you have the schema defined in YAML, you need to load it. To do
this, open a console, start the jconsole application, and connect to
Cassandra via JMX. Then, execute the operation loadSchemaFromYAML, which
is part of the org.apache.cassandra.service.StorageService MBean. Now
Cassandra knows about your schema and you can start using it. You can
also use the API itself to create keyspaces and column families.

Data Structures

The application requires some standard data structures that will just
act as transfer objects for us. These aren't particularly interesting,
but are required to keep things organized. We'll use a Hotel data
structure to hold all of the information about a hotel, shown in
[Example 4-2](https://www.oreilly.com/library/view/cassandra-the-definitive/9781449399764/ch04.html#ex-sa.hotel).

*Example 4-2. Hotel.java*

package com.cassandraguide.hotel;

//data transfer object

public class Hotel {

public String id;

public String name;

public String phone;

public String address;

public String city;

public String state;

public String zip;

}

This structure just holds the column information for convenience in the
application.

We also have a POI data structure to hold information about points of
interest. This is shown in
[Example 4-3](https://www.oreilly.com/library/view/cassandra-the-definitive/9781449399764/ch04.html#ex-sa.poi).

*Example 4-3. POI.java*

package com.cassandraguide.hotel;

//data transfer object for a Point of Interest

public class POI {

public String name;

public String desc;

public String phone;

}

We also have a Constants class, which keeps commonly used strings in one
easy-to-change place, shown in
[Example 4-4](https://www.oreilly.com/library/view/cassandra-the-definitive/9781449399764/ch04.html#ex-sa.const).

*Example 4-4. Constants.java*

package com.cassandraguide.hotel;

import org.apache.cassandra.thrift.ConsistencyLevel;

public class Constants {

public static final String CAMBRIA\_NAME = \"Cambria Suites Hayden\";

public static final String CLARION\_NAME= \"Clarion Scottsdale Peak\";

public static final String W\_NAME = \"The W SF\";

public static final String WALDORF\_NAME = \"The Waldorf=Astoria\";

public static final String UTF8 = \"UTF8\";

public static final String KEYSPACE = \"Hotelier\";

public static final ConsistencyLevel CL = ConsistencyLevel.ONE;

public static final String HOST = \"localhost\";

public static final int PORT = 9160;

}

Holding these commonly used strings make the code clearer and more
concise, and you can easily change these values to reflect what makes
sense in your environment.

Getting a Connection

For convenience, and to save repeating a bunch of boilerplate code,
let's put the connection code into one class, called Connector, shown in
[Example 4-5](https://www.oreilly.com/library/view/cassandra-the-definitive/9781449399764/ch04.html#ex-sa.clientget).

*Example 4-5. A connection client convenience class, Connector.java*

package com.cassandraguide.hotel;

import static com.cassandraguide.hotel.Constants.KEYSPACE;

import org.apache.cassandra.thrift.Cassandra;

import org.apache.cassandra.thrift.InvalidRequestException;

import org.apache.thrift.TException;

import org.apache.thrift.protocol.TBinaryProtocol;

import org.apache.thrift.protocol.TProtocol;

import org.apache.thrift.transport.TFramedTransport;

import org.apache.thrift.transport.TSocket;

import org.apache.thrift.transport.TTransport;

import org.apache.thrift.transport.TTransportException;

//simple convenience class to wrap connections, just to reduce repeat
code

public class Connector {

TTransport tr = new TSocket(\"localhost\", 9160);

// returns a new connection to our keyspace

public Cassandra.Client connect() throws TTransportException,

TException, InvalidRequestException {

TFramedTransport tf = new TFramedTransport(tr);

TProtocol proto = new TBinaryProtocol(tf);

Cassandra.Client client = new Cassandra.Client(proto);

tr.open();

client.set\_keyspace(KEYSPACE);

return client;

}

public void close() {

tr.close();

}

}

When we need to execute a database operation, we can use this class to
open a connection and then close the connection once we're done.

Prepopulating the Database

The Prepopulate class, shown in
[Example 4-6](https://www.oreilly.com/library/view/cassandra-the-definitive/9781449399764/ch04.html#ex-sa.prepop),
does a bunch of inserts and batch\_mutates in order to prepopulate the
database with the hotel information and points of interest information
that users will search for.

*Example 4-6. Prepopulate.java*

package com.cassandraguide.hotel;

import static com.cassandraguide.hotel.Constants.CAMBRIA\_NAME;

import static com.cassandraguide.hotel.Constants.CL;

import static com.cassandraguide.hotel.Constants.CLARION\_NAME;

import static com.cassandraguide.hotel.Constants.UTF8;

import static com.cassandraguide.hotel.Constants.WALDORF\_NAME;

import static com.cassandraguide.hotel.Constants.W\_NAME;

import java.io.UnsupportedEncodingException;

import java.util.ArrayList;

import java.util.HashMap;

import java.util.List;

import java.util.Map;

import org.apache.cassandra.thrift.Cassandra;

import org.apache.cassandra.thrift.Clock;

import org.apache.cassandra.thrift.Column;

import org.apache.cassandra.thrift.ColumnOrSuperColumn;

import org.apache.cassandra.thrift.ColumnParent;

import org.apache.cassandra.thrift.ColumnPath;

import org.apache.cassandra.thrift.Mutation;

import org.apache.cassandra.thrift.SuperColumn;

import org.apache.log4j.Logger;

/\*\*

\* Performs the initial population of the database.

\* Fills the CFs and SCFs with Hotel, Point of Interest, and index data.

\* Shows batch\_mutate and insert for Column Families and Super Column
Families.

\*

\* I am totally ignoring exceptions to save space.

\*/

public class Prepopulate {

private static final Logger LOG = Logger.getLogger(Prepopulate.class);

private Cassandra.Client client;

private Connector connector;

//constructor opens a connection so we don\'t have to

//constantly recreate it

public Prepopulate() throws Exception {

connector = new Connector();

client = connector.connect();

}

void prepopulate() throws Exception {

//pre-populate the DB with Hotels

insertAllHotels();

//also add all hotels to index to help searches

insertByCityIndexes();

//pre-populate the DB with POIs

insertAllPointsOfInterest();

connector.close();

}

//also add hotels to lookup by city index

public void insertByCityIndexes() throws Exception {

String scottsdaleKey = \"Scottsdale:AZ\";

String sfKey = \"San Francisco:CA\";

String newYorkKey = \"New York:NY\";

insertByCityIndex(scottsdaleKey, CAMBRIA\_NAME);

insertByCityIndex(scottsdaleKey, CLARION\_NAME);

insertByCityIndex(sfKey, W\_NAME);

insertByCityIndex(newYorkKey, WALDORF\_NAME);

}

//use Valueless Column pattern

private void insertByCityIndex(String rowKey, String hotelName)

throws Exception {

Clock clock = new Clock(System.nanoTime());

Column nameCol = new Column(hotelName.getBytes(UTF8),

new byte\[0\], clock);

ColumnOrSuperColumn nameCosc = new ColumnOrSuperColumn();

nameCosc.column = nameCol;

Mutation nameMut = new Mutation();

nameMut.column\_or\_supercolumn = nameCosc;

//set up the batch

Map\<String, Map\<String, List\<Mutation\>\>\> mutationMap =

new HashMap\<String, Map\<String, List\<Mutation\>\>\>();

Map\<String, List\<Mutation\>\> muts =

new HashMap\<String, List\<Mutation\>\>();

List\<Mutation\> cols = new ArrayList\<Mutation\>();

cols.add(nameMut);

String columnFamily = \"HotelByCity\";

muts.put(columnFamily, cols);

//outer map key is a row key

//inner map key is the column family name

mutationMap.put(rowKey, muts);

//create representation of the column

ColumnPath cp = new ColumnPath(columnFamily);

cp.setColumn(hotelName.getBytes(UTF8));

ColumnParent parent = new ColumnParent(columnFamily);

//here, the column name IS the value (there\'s no value)

Column col = new Column(hotelName.getBytes(UTF8), new byte\[0\], clock);

client.insert(rowKey.getBytes(), parent, col, CL);

LOG.debug(\"Inserted HotelByCity index for \" + hotelName);

} //end inserting ByCity index

//POI

public void insertAllPointsOfInterest() throws Exception {

LOG.debug(\"Inserting POIs.\");

insertPOIEmpireState();

insertPOICentralPark();

insertPOIPhoenixZoo();

insertPOISpringTraining();

LOG.debug(\"Done inserting POIs.\");

}

private void insertPOISpringTraining() throws Exception {

//Map\<byte\[\],Map\<String,List\<Mutation\>\>\>

Map\<byte\[\], Map\<String, List\<Mutation\>\>\> outerMap =

new HashMap\<byte\[\], Map\<String, List\<Mutation\>\>\>();

List\<Mutation\> columnsToAdd = new ArrayList\<Mutation\>();

Clock clock = new Clock(System.nanoTime());

String keyName = \"Spring Training\";

Column descCol = new Column(\"desc\".getBytes(UTF8),

\"Fun for baseball fans.\".getBytes(\"UTF-8\"), clock);

Column phoneCol = new Column(\"phone\".getBytes(UTF8),

\"623-333-3333\".getBytes(UTF8), clock);

List\<Column\> cols = new ArrayList\<Column\>();

cols.add(descCol);

cols.add(phoneCol);

Map\<String, List\<Mutation\>\> innerMap =

new HashMap\<String, List\<Mutation\>\>();

Mutation columns = new Mutation();

ColumnOrSuperColumn descCosc = new ColumnOrSuperColumn();

SuperColumn sc = new SuperColumn();

sc.name = CAMBRIA\_NAME.getBytes();

sc.columns = cols;

descCosc.super\_column = sc;

columns.setColumn\_or\_supercolumn(descCosc);

columnsToAdd.add(columns);

String superCFName = \"PointOfInterest\";

ColumnPath cp = new ColumnPath();

cp.column\_family = superCFName;

cp.setSuper\_column(CAMBRIA\_NAME.getBytes());

cp.setSuper\_columnIsSet(true);

innerMap.put(superCFName, columnsToAdd);

outerMap.put(keyName.getBytes(), innerMap);

client.batch\_mutate(outerMap, CL);

LOG.debug(\"Done inserting Spring Training.\");

}

private void insertPOIPhoenixZoo() throws Exception {

Map\<byte\[\], Map\<String, List\<Mutation\>\>\> outerMap =

new HashMap\<byte\[\], Map\<String, List\<Mutation\>\>\>();

List\<Mutation\> columnsToAdd = new ArrayList\<Mutation\>();

long ts = System.currentTimeMillis();

String keyName = \"Phoenix Zoo\";

Column descCol = new Column(\"desc\".getBytes(UTF8),

\"They have animals here.\".getBytes(\"UTF-8\"), new Clock(ts));

Column phoneCol = new Column(\"phone\".getBytes(UTF8),

\"480-555-9999\".getBytes(UTF8), new Clock(ts));

List\<Column\> cols = new ArrayList\<Column\>();

cols.add(descCol);

cols.add(phoneCol);

Map\<String, List\<Mutation\>\> innerMap =

new HashMap\<String, List\<Mutation\>\>();

String cambriaName = \"Cambria Suites Hayden\";

Mutation columns = new Mutation();

ColumnOrSuperColumn descCosc = new ColumnOrSuperColumn();

SuperColumn sc = new SuperColumn();

sc.name = cambriaName.getBytes();

sc.columns = cols;

descCosc.super\_column = sc;

columns.setColumn\_or\_supercolumn(descCosc);

columnsToAdd.add(columns);

String superCFName = \"PointOfInterest\";

ColumnPath cp = new ColumnPath();

cp.column\_family = superCFName;

cp.setSuper\_column(cambriaName.getBytes());

cp.setSuper\_columnIsSet(true);

innerMap.put(superCFName, columnsToAdd);

outerMap.put(keyName.getBytes(), innerMap);

client.batch\_mutate(outerMap, CL);

LOG.debug(\"Done inserting Phoenix Zoo.\");

}

private void insertPOICentralPark() throws Exception {

Map\<byte\[\], Map\<String, List\<Mutation\>\>\> outerMap =

new HashMap\<byte\[\], Map\<String, List\<Mutation\>\>\>();

List\<Mutation\> columnsToAdd = new ArrayList\<Mutation\>();

Clock clock = new Clock(System.nanoTime());

String keyName = \"Central Park\";

Column descCol = new Column(\"desc\".getBytes(UTF8),

\"Walk around in the park. It\'s pretty.\".getBytes(\"UTF-8\"), clock);

//no phone column for park

List\<Column\> cols = new ArrayList\<Column\>();

cols.add(descCol);

Map\<String, List\<Mutation\>\> innerMap =

new HashMap\<String, List\<Mutation\>\>();

Mutation columns = new Mutation();

ColumnOrSuperColumn descCosc = new ColumnOrSuperColumn();

SuperColumn waldorfSC = new SuperColumn();

waldorfSC.name = WALDORF\_NAME.getBytes();

waldorfSC.columns = cols;

descCosc.super\_column = waldorfSC;

columns.setColumn\_or\_supercolumn(descCosc);

columnsToAdd.add(columns);

String superCFName = \"PointOfInterest\";

ColumnPath cp = new ColumnPath();

cp.column\_family = superCFName;

cp.setSuper\_column(WALDORF\_NAME.getBytes());

cp.setSuper\_columnIsSet(true);

innerMap.put(superCFName, columnsToAdd);

outerMap.put(keyName.getBytes(), innerMap);

client.batch\_mutate(outerMap, CL);

LOG.debug(\"Done inserting Central Park.\");

}

private void insertPOIEmpireState() throws Exception {

Map\<byte\[\], Map\<String, List\<Mutation\>\>\> outerMap =

new HashMap\<byte\[\], Map\<String, List\<Mutation\>\>\>();

List\<Mutation\> columnsToAdd = new ArrayList\<Mutation\>();

Clock clock = new Clock(System.nanoTime());

String esbName = \"Empire State Building\";

Column descCol = new Column(\"desc\".getBytes(UTF8),

\"Great view from 102nd floor.\".getBytes(\"UTF-8\"), clock);

Column phoneCol = new Column(\"phone\".getBytes(UTF8),

\"212-777-7777\".getBytes(UTF8), clock);

List\<Column\> esbCols = new ArrayList\<Column\>();

esbCols.add(descCol);

esbCols.add(phoneCol);

Map\<String, List\<Mutation\>\> innerMap = new HashMap\<String,
List\<Mutation\>\>();

Mutation columns = new Mutation();

ColumnOrSuperColumn descCosc = new ColumnOrSuperColumn();

SuperColumn waldorfSC = new SuperColumn();

waldorfSC.name = WALDORF\_NAME.getBytes();

waldorfSC.columns = esbCols;

descCosc.super\_column = waldorfSC;

columns.setColumn\_or\_supercolumn(descCosc);

columnsToAdd.add(columns);

String superCFName = \"PointOfInterest\";

ColumnPath cp = new ColumnPath();

cp.column\_family = superCFName;

cp.setSuper\_column(WALDORF\_NAME.getBytes());

cp.setSuper\_columnIsSet(true);

innerMap.put(superCFName, columnsToAdd);

outerMap.put(esbName.getBytes(), innerMap);

client.batch\_mutate(outerMap, CL);

LOG.debug(\"Done inserting Empire State.\");

}

//convenience method runs all of the individual inserts

public void insertAllHotels() throws Exception {

String columnFamily = \"Hotel\";

//row keys

String cambriaKey = \"AZC\_043\";

String clarionKey = \"AZS\_011\";

String wKey = \"CAS\_021\";

String waldorfKey = \"NYN\_042\";

//conveniences

Map\<byte\[\], Map\<String, List\<Mutation\>\>\> cambriaMutationMap =

createCambriaMutation(columnFamily, cambriaKey);

Map\<byte\[\], Map\<String, List\<Mutation\>\>\> clarionMutationMap =

createClarionMutation(columnFamily, clarionKey);

Map\<byte\[\], Map\<String, List\<Mutation\>\>\> waldorfMutationMap =

createWaldorfMutation(columnFamily, waldorfKey);

Map\<byte\[\], Map\<String, List\<Mutation\>\>\> wMutationMap =

createWMutation(columnFamily, wKey);

client.batch\_mutate(cambriaMutationMap, CL);

LOG.debug(\"Inserted \" + cambriaKey);

client.batch\_mutate(clarionMutationMap, CL);

LOG.debug(\"Inserted \" + clarionKey);

client.batch\_mutate(wMutationMap, CL);

LOG.debug(\"Inserted \" + wKey);

client.batch\_mutate(waldorfMutationMap, CL);

LOG.debug(\"Inserted \" + waldorfKey);

LOG.debug(\"Done inserting at \" + System.nanoTime());

}

//set up columns to insert for W

private Map\<byte\[\], Map\<String, List\<Mutation\>\>\>
createWMutation(

String columnFamily, String rowKey)

throws UnsupportedEncodingException {

Clock clock = new Clock(System.nanoTime());

Column nameCol = new Column(\"name\".getBytes(UTF8),

W\_NAME.getBytes(\"UTF-8\"), clock);

Column phoneCol = new Column(\"phone\".getBytes(UTF8),

\"415-222-2222\".getBytes(UTF8), clock);

Column addressCol = new Column(\"address\".getBytes(UTF8),

\"181 3rd Street\".getBytes(UTF8), clock);

Column cityCol = new Column(\"city\".getBytes(UTF8),

\"San Francisco\".getBytes(UTF8), clock);

Column stateCol = new Column(\"state\".getBytes(UTF8),

\"CA\".getBytes(\"UTF-8\"), clock);

Column zipCol = new Column(\"zip\".getBytes(UTF8),

\"94103\".getBytes(UTF8), clock);

ColumnOrSuperColumn nameCosc = new ColumnOrSuperColumn();

nameCosc.column = nameCol;

ColumnOrSuperColumn phoneCosc = new ColumnOrSuperColumn();

phoneCosc.column = phoneCol;

ColumnOrSuperColumn addressCosc = new ColumnOrSuperColumn();

addressCosc.column = addressCol;

ColumnOrSuperColumn cityCosc = new ColumnOrSuperColumn();

cityCosc.column = cityCol;

ColumnOrSuperColumn stateCosc = new ColumnOrSuperColumn();

stateCosc.column = stateCol;

ColumnOrSuperColumn zipCosc = new ColumnOrSuperColumn();

zipCosc.column = zipCol;

Mutation nameMut = new Mutation();

nameMut.column\_or\_supercolumn = nameCosc;

Mutation phoneMut = new Mutation();

phoneMut.column\_or\_supercolumn = phoneCosc;

Mutation addressMut = new Mutation();

addressMut.column\_or\_supercolumn = addressCosc;

Mutation cityMut = new Mutation();

cityMut.column\_or\_supercolumn = cityCosc;

Mutation stateMut = new Mutation();

stateMut.column\_or\_supercolumn = stateCosc;

Mutation zipMut = new Mutation();

zipMut.column\_or\_supercolumn = zipCosc;

//set up the batch

Map\<byte\[\], Map\<String, List\<Mutation\>\>\> mutationMap =

new HashMap\<byte\[\], Map\<String, List\<Mutation\>\>\>();

Map\<String, List\<Mutation\>\> muts =

new HashMap\<String, List\<Mutation\>\>();

List\<Mutation\> cols = new ArrayList\<Mutation\>();

cols.add(nameMut);

cols.add(phoneMut);

cols.add(addressMut);

cols.add(cityMut);

cols.add(stateMut);

cols.add(zipMut);

muts.put(columnFamily, cols);

//outer map key is a row key

//inner map key is the column family name

mutationMap.put(rowKey.getBytes(), muts);

return mutationMap;

}

//add Waldorf hotel to Hotel CF

private Map\<byte\[\], Map\<String, List\<Mutation\>\>\>
createWaldorfMutation(

String columnFamily, String rowKey)

throws UnsupportedEncodingException {

Clock clock = new Clock(System.nanoTime());

Column nameCol = new Column(\"name\".getBytes(UTF8),

WALDORF\_NAME.getBytes(\"UTF-8\"), clock);

Column phoneCol = new Column(\"phone\".getBytes(UTF8),

\"212-555-5555\".getBytes(UTF8), clock);

Column addressCol = new Column(\"address\".getBytes(UTF8),

\"301 Park Ave\".getBytes(UTF8), clock);

Column cityCol = new Column(\"city\".getBytes(UTF8),

\"New York\".getBytes(UTF8), clock);

Column stateCol = new Column(\"state\".getBytes(UTF8),

\"NY\".getBytes(\"UTF-8\"), clock);

Column zipCol = new Column(\"zip\".getBytes(UTF8),

\"10019\".getBytes(UTF8), clock);

ColumnOrSuperColumn nameCosc = new ColumnOrSuperColumn();

nameCosc.column = nameCol;

ColumnOrSuperColumn phoneCosc = new ColumnOrSuperColumn();

phoneCosc.column = phoneCol;

ColumnOrSuperColumn addressCosc = new ColumnOrSuperColumn();

addressCosc.column = addressCol;

ColumnOrSuperColumn cityCosc = new ColumnOrSuperColumn();

cityCosc.column = cityCol;

ColumnOrSuperColumn stateCosc = new ColumnOrSuperColumn();

stateCosc.column = stateCol;

ColumnOrSuperColumn zipCosc = new ColumnOrSuperColumn();

zipCosc.column = zipCol;

Mutation nameMut = new Mutation();

nameMut.column\_or\_supercolumn = nameCosc;

Mutation phoneMut = new Mutation();

phoneMut.column\_or\_supercolumn = phoneCosc;

Mutation addressMut = new Mutation();

addressMut.column\_or\_supercolumn = addressCosc;

Mutation cityMut = new Mutation();

cityMut.column\_or\_supercolumn = cityCosc;

Mutation stateMut = new Mutation();

stateMut.column\_or\_supercolumn = stateCosc;

Mutation zipMut = new Mutation();

zipMut.column\_or\_supercolumn = zipCosc;

//set up the batch

Map\<byte\[\], Map\<String, List\<Mutation\>\>\> mutationMap =

new HashMap\<byte\[\], Map\<String, List\<Mutation\>\>\>();

Map\<String, List\<Mutation\>\> muts =

new HashMap\<String, List\<Mutation\>\>();

List\<Mutation\> cols = new ArrayList\<Mutation\>();

cols.add(nameMut);

cols.add(phoneMut);

cols.add(addressMut);

cols.add(cityMut);

cols.add(stateMut);

cols.add(zipMut);

muts.put(columnFamily, cols);

//outer map key is a row key

//inner map key is the column family name

mutationMap.put(rowKey.getBytes(), muts);

return mutationMap;

}

//set up columns to insert for Clarion

private Map\<byte\[\], Map\<String, List\<Mutation\>\>\>
createClarionMutation(

String columnFamily, String rowKey)

throws UnsupportedEncodingException {

Clock clock = new Clock(System.nanoTime());

Column nameCol = new Column(\"name\".getBytes(UTF8),

CLARION\_NAME.getBytes(\"UTF-8\"), clock);

Column phoneCol = new Column(\"phone\".getBytes(UTF8),

\"480-333-3333\".getBytes(UTF8), clock);

Column addressCol = new Column(\"address\".getBytes(UTF8),

\"3000 N. Scottsdale Rd\".getBytes(UTF8), clock);

Column cityCol = new Column(\"city\".getBytes(UTF8),

\"Scottsdale\".getBytes(UTF8), clock);

Column stateCol = new Column(\"state\".getBytes(UTF8),

\"AZ\".getBytes(\"UTF-8\"), clock);

Column zipCol = new Column(\"zip\".getBytes(UTF8),

\"85255\".getBytes(UTF8), clock);

ColumnOrSuperColumn nameCosc = new ColumnOrSuperColumn();

nameCosc.column = nameCol;

ColumnOrSuperColumn phoneCosc = new ColumnOrSuperColumn();

phoneCosc.column = phoneCol;

ColumnOrSuperColumn addressCosc = new ColumnOrSuperColumn();

addressCosc.column = addressCol;

ColumnOrSuperColumn cityCosc = new ColumnOrSuperColumn();

cityCosc.column = cityCol;

ColumnOrSuperColumn stateCosc = new ColumnOrSuperColumn();

stateCosc.column = stateCol;

ColumnOrSuperColumn zipCosc = new ColumnOrSuperColumn();

zipCosc.column = zipCol;

Mutation nameMut = new Mutation();

nameMut.column\_or\_supercolumn = nameCosc;

Mutation phoneMut = new Mutation();

phoneMut.column\_or\_supercolumn = phoneCosc;

Mutation addressMut = new Mutation();

addressMut.column\_or\_supercolumn = addressCosc;

Mutation cityMut = new Mutation();

cityMut.column\_or\_supercolumn = cityCosc;

Mutation stateMut = new Mutation();

stateMut.column\_or\_supercolumn = stateCosc;

Mutation zipMut = new Mutation();

zipMut.column\_or\_supercolumn = zipCosc;

//set up the batch

Map\<byte\[\], Map\<String, List\<Mutation\>\>\> mutationMap =

new HashMap\<byte\[\], Map\<String, List\<Mutation\>\>\>();

Map\<String, List\<Mutation\>\> muts =

new HashMap\<String, List\<Mutation\>\>();

List\<Mutation\> cols = new ArrayList\<Mutation\>();

cols.add(nameMut);

cols.add(phoneMut);

cols.add(addressMut);

cols.add(cityMut);

cols.add(stateMut);

cols.add(zipMut);

muts.put(columnFamily, cols);

//outer map key is a row key

//inner map key is the column family name

mutationMap.put(rowKey.getBytes(), muts);

return mutationMap;

}

//set up columns to insert for Cambria

private Map\<byte\[\], Map\<String, List\<Mutation\>\>\>
createCambriaMutation(

String columnFamily, String cambriaKey)

throws UnsupportedEncodingException {

//set up columns for Cambria

Clock clock = new Clock(System.nanoTime());

Column cambriaNameCol = new Column(\"name\".getBytes(UTF8),

\"Cambria Suites Hayden\".getBytes(\"UTF-8\"), clock);

Column cambriaPhoneCol = new Column(\"phone\".getBytes(UTF8),

\"480-444-4444\".getBytes(UTF8), clock);

Column cambriaAddressCol = new Column(\"address\".getBytes(UTF8),

\"400 N. Hayden\".getBytes(UTF8), clock);

Column cambriaCityCol = new Column(\"city\".getBytes(UTF8),

\"Scottsdale\".getBytes(UTF8), clock);

Column cambriaStateCol = new Column(\"state\".getBytes(UTF8),

\"AZ\".getBytes(\"UTF-8\"), clock);

Column cambriaZipCol = new Column(\"zip\".getBytes(UTF8),

\"85255\".getBytes(UTF8), clock);

ColumnOrSuperColumn nameCosc = new ColumnOrSuperColumn();

nameCosc.column = cambriaNameCol;

ColumnOrSuperColumn phoneCosc = new ColumnOrSuperColumn();

phoneCosc.column = cambriaPhoneCol;

ColumnOrSuperColumn addressCosc = new ColumnOrSuperColumn();

addressCosc.column = cambriaAddressCol;

ColumnOrSuperColumn cityCosc = new ColumnOrSuperColumn();

cityCosc.column = cambriaCityCol;

ColumnOrSuperColumn stateCosc = new ColumnOrSuperColumn();

stateCosc.column = cambriaStateCol;

ColumnOrSuperColumn zipCosc = new ColumnOrSuperColumn();

zipCosc.column = cambriaZipCol;

Mutation nameMut = new Mutation();

nameMut.column\_or\_supercolumn = nameCosc;

Mutation phoneMut = new Mutation();

phoneMut.column\_or\_supercolumn = phoneCosc;

Mutation addressMut = new Mutation();

addressMut.column\_or\_supercolumn = addressCosc;

Mutation cityMut = new Mutation();

cityMut.column\_or\_supercolumn = cityCosc;

Mutation stateMut = new Mutation();

stateMut.column\_or\_supercolumn = stateCosc;

Mutation zipMut = new Mutation();

zipMut.column\_or\_supercolumn = zipCosc;

//set up the batch

Map\<byte\[\], Map\<String, List\<Mutation\>\>\> cambriaMutationMap =

new HashMap\<byte\[\], Map\<String, List\<Mutation\>\>\>();

Map\<String, List\<Mutation\>\> cambriaMuts =

new HashMap\<String, List\<Mutation\>\>();

List\<Mutation\> cambriaCols = new ArrayList\<Mutation\>();

cambriaCols.add(nameMut);

cambriaCols.add(phoneMut);

cambriaCols.add(addressMut);

cambriaCols.add(cityMut);

cambriaCols.add(stateMut);

cambriaCols.add(zipMut);

cambriaMuts.put(columnFamily, cambriaCols);

//outer map key is a row key

//inner map key is the column family name

cambriaMutationMap.put(cambriaKey.getBytes(), cambriaMuts);

return cambriaMutationMap;

}

}

This is a rather long example, but it attempts to show something more
than "hello, world"---there are a number of insert and batch\_mutate
operations shown with standard column families and super column
families. I have also included multiple rows for each type so that more
sophisticated queries are required.

This class is the first to execute in our sample application, and once
the prepopulate method is complete, your database will have all the data
that the search functions need to work with.

The Search Application

[Example 4-7](https://www.oreilly.com/library/view/cassandra-the-definitive/9781449399764/ch04.html#ex_4_7)
is the Java class with the main method that you should execute. It
relies on Log4J, so you'll want to point to your *log4j.properties* file
when you run it. All you have to do is run this class, and the database
gets prepopulated with all of the hotel and point of interest
information; then, it allows the user to search for hotels in a given
city. The user picks one hotel, and the application fetches the nearby
points of interest. You can then implement the remaining parts of the
application to book a reservation if you like.

*Example 4-7. HotelApp.java*

package com.cassandraguide.hotel;

import static com.cassandraguide.hotel.Constants.CL;

import static com.cassandraguide.hotel.Constants.UTF8;

import java.util.ArrayList;

import java.util.List;

import org.apache.cassandra.thrift.Cassandra;

import org.apache.cassandra.thrift.Column;

import org.apache.cassandra.thrift.ColumnOrSuperColumn;

import org.apache.cassandra.thrift.ColumnParent;

import org.apache.cassandra.thrift.KeyRange;

import org.apache.cassandra.thrift.KeySlice;

import org.apache.cassandra.thrift.SlicePredicate;

import org.apache.cassandra.thrift.SliceRange;

import org.apache.cassandra.thrift.SuperColumn;

import org.apache.log4j.Logger;

/\*\*

\* Runs the hotel application. After the database is pre-populated,

\* this class mocks a user interaction to perform a hotel search based
on

\* city, selects one, then looks at some surrounding points of interest
for

\* that hotel.

\*

\* Shows using Materialized View pattern, get, get\_range\_slices, key
slices.

\*

\* These exceptions are thrown out of main to reduce code size:

\* UnsupportedEncodingException,

InvalidRequestException, UnavailableException, TimedOutException,

TException, NotFoundException, InterruptedException

Uses the Constants class for some commonly used strings.

\*/

public class HotelApp {

private static final Logger LOG = Logger.getLogger(HotelApp.class);

public static void main(String\[\] args) throws Exception {

//first put all of the data in the database

new Prepopulate().prepopulate();

LOG.debug(\"\*\* Database filled. \*\*\");

//now run our client

LOG.debug(\"\*\* Starting hotel reservation app. \*\*\");

HotelApp app = new HotelApp();

//find a hotel by city\--try Scottsdale or New York\...

List\<Hotel\> hotels = app.findHotelByCity(\"Scottsdale\", \"AZ\");

//List\<Hotel\> hotels = app.findHotelByCity(\"New York\", \"NY\");

LOG.debug(\"Found hotels in city. Results: \" + hotels.size());

//choose one

Hotel h = hotels.get(0);

LOG.debug(\"You picked \" + h.name);

//find Points of Interest for selected hotel

LOG.debug(\"Finding Points of Interest near \" + h.name);

List\<POI\> points = app.findPOIByHotel(h.name);

//choose one

POI poi = points.get(0);

LOG.debug(\"Hm\... \" + poi.name + \". \" + poi.desc + \"\--Sounds
fun!\");

LOG.debug(\"Now to book a room\...\");

//show availability for a date

//left as an exercise\...

//create reservation

//left as an exercise\...

LOG.debug(\"All done.\");

}

//use column slice to get from Super Column

public List\<POI\> findPOIByHotel(String hotel) throws Exception {

///query

SlicePredicate predicate = new SlicePredicate();

SliceRange sliceRange = new SliceRange();

sliceRange.setStart(hotel.getBytes());

sliceRange.setFinish(hotel.getBytes());

predicate.setSlice\_range(sliceRange);

// read all columns in the row

String scFamily = \"PointOfInterest\";

ColumnParent parent = new ColumnParent(scFamily);

KeyRange keyRange = new KeyRange();

keyRange.start\_key = \"\".getBytes();

keyRange.end\_key = \"\".getBytes();

List\<POI\> pois = new ArrayList\<POI\>();

//instead of a simple list, we get a map whose keys are row keys

//and the values the list of columns returned for each

//only row key + first column are indexed

Connector cl = new Connector();

Cassandra.Client client = cl.connect();

List\<KeySlice\> slices = client.get\_range\_slices(

parent, predicate, keyRange, CL);

for (KeySlice slice : slices) {

List\<ColumnOrSuperColumn\> cols = slice.columns;

POI poi = new POI();

poi.name = new String(slice.key);

for (ColumnOrSuperColumn cosc : cols) {

SuperColumn sc = cosc.super\_column;

List\<Column\> colsInSc = sc.columns;

for (Column c : colsInSc) {

String colName = new String(c.name, UTF8);

if (colName.equals(\"desc\")) {

poi.desc = new String(c.value, UTF8);

}

if (colName.equals(\"phone\")) {

poi.phone = new String(c.value, UTF8);

}

}

LOG.debug(\"Found something neat nearby: \" + poi.name +

\". \\nDesc: \" + poi.desc +

\". \\nPhone: \" + poi.phone);

pois.add(poi);

}

}

cl.close();

return pois;

}

//uses key range

public List\<Hotel\> findHotelByCity(String city, String state)

throws Exception {

LOG.debug(\"Seaching for hotels in \" + city + \", \" + state);

String key = city + \":\" + state.toUpperCase();

///query

SlicePredicate predicate = new SlicePredicate();

SliceRange sliceRange = new SliceRange();

sliceRange.setStart(new byte\[0\]);

sliceRange.setFinish(new byte\[0\]);

predicate.setSlice\_range(sliceRange);

// read all columns in the row

String columnFamily = \"HotelByCity\";

ColumnParent parent = new ColumnParent(columnFamily);

KeyRange keyRange = new KeyRange();

keyRange.setStart\_key(key.getBytes());

keyRange.setEnd\_key((key+1).getBytes()); //just outside lexical range

keyRange.count = 5;

Connector cl = new Connector();

Cassandra.Client client = cl.connect();

List\<KeySlice\> keySlices =

client.get\_range\_slices(parent, predicate, keyRange, CL);

List\<Hotel\> results = new ArrayList\<Hotel\>();

for (KeySlice ks : keySlices) {

List\<ColumnOrSuperColumn\> coscs = ks.columns;

LOG.debug(new String(\"Using key \" + ks.key));

for (ColumnOrSuperColumn cs : coscs) {

Hotel hotel = new Hotel();

hotel.name = new String(cs.column.name, UTF8);

hotel.city = city;

hotel.state = state;

results.add(hotel);

LOG.debug(\"Found hotel result for \" + hotel.name);

}

}

///end query

cl.close();

return results;

}

}

I interspersed the code with comments to illustrate the purpose of the
different statements.

The output of running the application is shown in
[Example 4-8](https://www.oreilly.com/library/view/cassandra-the-definitive/9781449399764/ch04.html#ex-sa.output).

*Example 4-8. Output of running the hotel application*

DEBUG 09:49:50,858 Inserted AZC\_043

DEBUG 09:49:50,861 Inserted AZS\_011

DEBUG 09:49:50,863 Inserted CAS\_021

DEBUG 09:49:50,864 Inserted NYN\_042

DEBUG 09:49:50,864 Done inserting at 6902368219815217

DEBUG 09:49:50,873 Inserted HotelByCity index for Cambria Suites Hayden

DEBUG 09:49:50,874 Inserted HotelByCity index for Clarion Scottsdale
Peak

DEBUG 09:49:50,875 Inserted HotelByCity index for The W SF

DEBUG 09:49:50,877 Inserted HotelByCity index for The Waldorf=Astoria

DEBUG 09:49:50,877 Inserting POIs.

DEBUG 09:49:50,880 Done inserting Empire State.

DEBUG 09:49:50,881 Done inserting Central Park.

DEBUG 09:49:50,885 Done inserting Phoenix Zoo.

DEBUG 09:49:50,887 Done inserting Spring Training.

DEBUG 09:49:50,887 Done inserting POIs.

DEBUG 09:49:50,887 \*\* Database filled. \*\*

DEBUG 09:49:50,889 \*\* Starting hotel reservation app. \*\*

DEBUG 09:49:50,889 Seaching for hotels in Scottsdale, AZ

DEBUG 09:49:50,902 Using key \[B\@15e9756

DEBUG 09:49:50,903 Found hotel result for Cambria Suites Hayden

DEBUG 09:49:50,903 Found hotel result for Clarion Scottsdale Peak

DEBUG 09:49:50,904 Found hotels in city. Results: 2

DEBUG 09:49:50,904 You picked Cambria Suites Hayden

DEBUG 09:49:50,904 Finding Points of Interest near Cambria Suites Hayden

DEBUG 09:49:50,911 Found something neat nearby: Phoenix Zoo.

Desc: They have animals here..

Phone: 480-555-9999

DEBUG 09:49:50,911 Found something neat nearby: Spring Training.

Desc: Fun for baseball fans..

Phone: 623-333-3333

DEBUG 09:49:50,911 Hm\... Phoenix Zoo. They have animals here.\--Sounds
fun!

DEBUG 09:49:50,911 Now to book a room\...

DEBUG 09:49:50,912 All done.

Again, you typically don't want to write against Thrift or Avro
yourself, but instead should use one of the clients listed in
[Chapter 8](https://www.oreilly.com/library/view/cassandra-the-definitive/9781449399764/ch08.html).
The purpose here is to give you an idea of how the plumbing works, and
to show a complete, working application that performs inserts and
various searches and that resembles real-world usage.

Twissandra

When you start thinking about how to design for Cassandra, take a look
at Twissandra, written by Eric Florenzano. Visit
[http://www.twissandra.com](http://www.twissandra.com/) to see a fully
working Twitter clone that you can download and try out. The source is
all in Python, and it has a few dependencies on Django and a JSON
library to sort out, but it's a great place to start. You can use what's
likely a familiar data model (Twitter's) and see how users, time lines,
and tweets all fit into a simple Cassandra data model.

There is also a helpful post by Eric Evans explaining how to use
Twissandra, which is available at
[[https://github.com/samirsahoo007/twissandra.git]{.underline}](https://github.com/samirsahoo007/twissandra.git)
or <http://www.rackspacecloud.com/blog/2010/05/12/cassandra-by-example>.
