Elasticsearch tutorial for beginners using Python

**What is Elasticsearch:-**

ElasticSearch (ES) is a distributed and highly available open-source search engine that is built on top of Apache Lucene. 
It’s an open-source which is built in Java thus available for many platforms. You store unstructured data in JSON format which also makes it a 
NoSQL database. So, unlike other NoSQL databases ES also provides search engine capabilities and other related features.

**ElasticSearch Use Cases:-**
You can use ES for multiple purposes, a couple of them given below:
	- You are running a website that provides lots of dynamic content; be it an e-commerce website or a blog. By implementing ES you can not only provide a robust search engine for your web app but can also provide native auto-complete features in your app.
	- You can ingest different kinds of log data and then can use to find trends and statistics.


**Installation/Setup:**

Ref:
[[https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html]{.underline}](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)

\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#

\$docker pull
[[docker.elastic.co/elasticsearch/elasticsearch:7.0.1]{.underline}](http://docker.elastic.co/elasticsearch/elasticsearch:7.0.1)
(To verify \$docker images)

\$docker run -p 9200:9200 -p 9300:9300 -e \"discovery.type=single-node\"
[[docker.elastic.co/elasticsearch/elasticsearch:7.0.1]{.underline}](http://docker.elastic.co/elasticsearch/elasticsearch:7.0.1)

Verify it from the browser: localhosts:9200

\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#

If you want to join the container from another terminal.

\$ docker exec -it beac0962fcdd /bin/bash

Note the use of single-node discovery that allows bypassing the
bootstrap checks in a single-node development cluster.

The following example brings up a cluster comprising two Elasticsearch
nodes. To bring up the cluster, use the
[docker-compose.yml](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-prod-cluster-composefile)
and just type:

\$ docker-compose up

The node es01 listens on localhost:9200 while es02 talks to es01 over a
Docker network.

This example also uses [Docker named
volumes](https://docs.docker.com/engine/tutorials/dockervolumes), called
esdata01 and esdata02 which will be created if not already present.

\#\#\#\#\#\#\#\#docker-compose.yml\#\#\#\#\#\#\#\#\#\#\#

version: \'2.2\'

services:

es01:

image: docker.elastic.co/elasticsearch/elasticsearch:7.0.1

container\_name: es01

environment:

\- node.name=es01

\- discovery.seed\_hosts=es02

\- cluster.initial\_master\_nodes=es01,es02

\- cluster.name=docker-cluster

\- bootstrap.memory\_lock=true

\- \"ES\_JAVA\_OPTS=-Xms512m -Xmx512m\"

ulimits:

memlock:

soft: -1

hard: -1

volumes:

\- esdata01:/usr/share/elasticsearch/data

ports:

\- 9200:9200

networks:

\- esnet

es02:

image: docker.elastic.co/elasticsearch/elasticsearch:7.0.1

container\_name: es02

environment:

\- node.name=es02

\- discovery.seed\_hosts=es01

\- cluster.initial\_master\_nodes=es01,es02

\- cluster.name=docker-cluster

\- bootstrap.memory\_lock=true

\- \"ES\_JAVA\_OPTS=-Xms512m -Xmx512m\"

ulimits:

memlock:

soft: -1

hard: -1

volumes:

\- esdata02:/usr/share/elasticsearch/data

networks:

\- esnet

volumes:

esdata01:

driver: local

esdata02:

driver: local

networks:

esnet:

\$ docker-compose down \# To stop the cluster

Data volumes will persist, so it's possible to start the cluster again
with the same data using docker-compose up.

To destroy the cluster and the data volumes, just type

\$ docker-compose down -v.

**Inspect status of cluster:**

\$ curl http://127.0.0.1:9200/\_cat/health

1472225929 15:38:49 docker-cluster green 2 2 4 2 0 0 0 0 - 100.0%

Log messages go to the console and are handled by the configured Docker
logging driver. By default you can access logs with

\$ docker logs.

Configuring Elasticsearch with Docker

Elasticsearch loads its configuration from files under
/usr/share/elasticsearch/config/. These configuration files are
documented in [Configuring
Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/settings.html)
and [Setting JVM
options](https://www.elastic.co/guide/en/elasticsearch/reference/current/jvm-options.html).

The image offers several methods for configuring Elasticsearch settings
with the conventional approach being to provide customized files, that
is to say elasticsearch.yml, but it's also possible to use environment
variables to set options:

**A. Present the parameters via Docker environment variables**

For example, to define the cluster name with docker run you can pass -e
\"cluster.name=mynewclustername\". Double quotes are required.

**B. Bind-mounted configuration**

Create your custom config file and mount this over the image's
corresponding file. For example, bind-mounting a
custom\_elasticsearch.yml with docker run can be accomplished with the
parameter:

-v
full\_path\_to/custom\_elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml

The container **runs Elasticsearch as user elasticsearch using uid:gid
1000:1000**. Bind mounted host directories and files, such as
custom\_elasticsearch.yml above, **need to be accessible by this user**.
For the [data and log
dirs](https://www.elastic.co/guide/en/elasticsearch/reference/current/path-settings.html),
such as /usr/share/elasticsearch/data, write access is required as well.
Also see note 1 below.

**C. Customized image**

In some environments, it may make more sense to prepare a custom image
containing your configuration. A Dockerfile to achieve this may be as
simple as:

FROM docker.elastic.co/elasticsearch/elasticsearch:7.0.1

COPY \--chown=elasticsearch:elasticsearch elasticsearch.yml
/usr/share/elasticsearch/config/

You could then build and try the image with something like:

\$ docker build \--tag=elasticsearch-custom .

\$ docker run -ti -v /usr/share/elasticsearch/data elasticsearch-custom

Some plugins require additional security permissions. You have to
explicitly accept them either by attaching a tty when you run the Docker
image and accepting yes at the prompts, or inspecting the security
permissions separately and if you are comfortable with them adding the
\--batch flag to the plugin install command.

**D. Override the image's default**
[CMD](https://docs.docker.com/engine/reference/run/#cmd-default-command-or-options)

Options can be passed as command-line options to the Elasticsearch
process by overriding the default command for the image. For example:

docker run \<various parameters\> bin/elasticsearch
-Ecluster.name=mynewclustername


**Installing and running Elasticsearch:**

The only requirement for installing Elasticsearch is a recent version of
Java. To install Elasticsearch, download and extract the archive file
from elastic.co/downlaods/elasticsearch and simply run
bin\\elasticsearch.bat. Test it in browser @ 'http://localhost:9200'.

**Index:-**

An index is like a database in traditional database. It is the place to
store related documents. To retrive any document we would need three
pieces of informantion

Index --- Database

Datatype --- Type of the document

Id --- Id of the document

**Let's start the show...**

\# Import Elasticsearch package

from elasticsearch import Elasticsearch

\# Connect to the elastic cluster

es=Elasticsearch(\[{\'host\':\'localhost\',\'port\':9200}\])

es

\<Elasticsearch(\[{\'host\': \'localhost\', \'port\': 9200}\])\>

Elasticsearch is document oriented, meaning that it stores entire object
or documents. It not only stores them, but also indexes the content of
each document in order to make them searchable. In Elasticsearch you
index, search,sort and filter documents.

Elasticsearch uses JSON as the serialisation format for the documents.

Now let's start by indexing the employee documents.

The act of storing data in Elasticsearch is called indexing. An
Elasticsearch cluster can contain multiple indices, which in turn
contain multiple types. These types hold multiple documents, and each
document has multiple fields.

e1={

\"first\_name\":\"nitin\",

\"last\_name\":\"panwar\",

\"age\": 27,

\"about\": \"Love to play cricket\",

\"interests\": \[\'sports\',\'music\'\],

}

print e1

{\'interests\': \[\'sports\', \'music\'\], \'about\': \'Love to play
cricket\', \'first\_name\': \'nitin\', \'last\_name\': \'panwar\',
\'age\': 27}

**Inserting a document:**

\#Now let\'s store this document in Elasticsearch

res = es.index(index=\'megacorp\',doc\_type=\'employee\',id=1,body=e1)

Simple! There was no need to perform any administrative tasks first,
like creating an index or specifying the type of data that each field
contains. We could just index a document directly. Elasticsearch ships
with defaults for everything, so all the necessary administration tasks
were taken care of in the background, using default values.

\# Let\'s insert some more documents

e2={

\"first\_name\" : \"Jane\",

\"last\_name\" : \"Smith\",

\"age\" : 32,

\"about\" : \"I like to collect rock albums\",

\"interests\": \[ \"music\" \]

}

e3={

\"first\_name\" : \"Douglas\",

\"last\_name\" : \"Fir\",

\"age\" : 35,

\"about\": \"I like to build cabinets\",

\"interests\": \[ \"forestry\" \]

}

res=es.index(index=\'megacorp\',doc\_type=\'employee\',id=2,body=e2)

print res\[\'created\'\]

res=es.index(index=\'megacorp\',doc\_type=\'employee\',id=3,body=e3)

print res\[\'created\'\]

False

True

**Retrieving a Document:**

This is easy in Elasticsearch. We simply execute an HTTP GET request and
specify the address of the document --- the index, type, and ID. Using
those three pieces of information, we can return the original JSON
document.

res=es.get(index=\'megacorp\',doc\_type=\'employee\',id=3)

print res

{u\'\_type\': u\'employee\', u\'\_source\': {u\'interests\':
\[u\'forestry\'\], u\'age\': 35, u\'about\': u\'I like to build
cabinets\', u\'last\_name\': u\'Fir\', u\'first\_name\': u\'Douglas\'},
u\'\_index\': u\'megacorp\', u\'\_version\': 1, u\'found\': True,
u\'\_id\': u\'3\'}

You will get the actual document in '\_source' field

print res\[\'\_source\'\]

{u\'interests\': \[u\'forestry\'\], u\'age\': 35, u\'about\': u\'I like
to build cabinets\', u\'last\_name\': u\'Fir\', u\'first\_name\':
u\'Douglas\'}

**Deleting a document:**

res=es.delete(index=\'megacorp\',doc\_type=\'employee\',id=3)

print res\[\'result\'\]

deleted

Now let's validate it in Elasticsearch

res= es.search(index=\'megacorp\',body={\'query\':{\'match\_all\':{}}})

print(\'Got %d hits:\' %res\[\'hits\'\]\[\'total\'\])

Got 3 hits:

**Search Lite:**

A GET is fairly simple --- you get back the document that you ask for.
Let's try something a little more advanced, like a simple search!

res= es.search(index=\'megacorp\',body={\'query\':{}})

print res\[\'hits\'\]\[\'hits\'\]

\[{u\'\_score\': 1.0, u\'\_type\': u\'employee\', u\'\_id\': u\'4\',
u\'\_source\': {u\'interests\': \[u\'sports\', u\'music\'\], u\'age\':
27, u\'about\': u\'Love to play football\', u\'last\_name\':
u\'pafdfd\', u\'first\_name\': u\'asd\'}, u\'\_index\': u\'megacorp\'},
{u\'\_score\': 1.0, u\'\_type\': u\'employee\', u\'\_id\': u\'2\',
u\'\_source\': {u\'interests\': \[u\'music\'\], u\'age\': 32,
u\'about\': u\'I like to collect rock albums\', u\'last\_name\':
u\'Smith\', u\'first\_name\': u\'Jane\'}, u\'\_index\': u\'megacorp\'},
{u\'\_score\': 1.0, u\'\_type\': u\'employee\', u\'\_id\': u\'1\',
u\'\_source\': {u\'interests\': \[u\'sports\', u\'music\'\], u\'age\':
27, u\'about\': u\'Love to play cricket\', u\'last\_name\': u\'panwar\',
u\'first\_name\': u\'nitin\'}, u\'\_index\': u\'megacorp\'}\]

Now let's search for the user name who has nitin in his first name.

**match operator:**

res=
es.search(index=\'megacorp\',body={\'query\':{\'match\':{\'first\_name\':\'nitin\'}}})

print res\[\'hits\'\]\[\'hits\'\]

\[{u\'\_score\': 0.2876821, u\'\_type\': u\'employee\', u\'\_id\':
u\'1\', u\'\_source\': {u\'interests\': \[u\'sports\', u\'music\'\],
u\'age\': 27, u\'about\': u\'Love to play cricket\', u\'last\_name\':
u\'panwar\', u\'first\_name\': u\'nitin\'}, u\'\_index\':
u\'megacorp\'}\]

**bool operator:**

bool takes a dictionary containing at least one of must, should, and
must\_not, each of which takes a list of matches or other further search
operators.

res= es.search(index=\'megacorp\',body={

\'query\':{

\'bool\':{

\'must\':\[{

\'match\':{

\'first\_name\':\'nitin\'

}

}\]

}

}

})

print res\[\'hits\'\]\[\'hits\'\]

\[{u\'\_score\': 0.2876821, u\'\_type\': u\'employee\', u\'\_id\':
u\'1\', u\'\_source\': {u\'interests\': \[u\'sports\', u\'music\'\],
u\'age\': 27, u\'about\': u\'Love to play cricket\', u\'last\_name\':
u\'panwar\', u\'first\_name\': u\'nitin\'}, u\'\_index\':
u\'megacorp\'}\]

**Filter operator:**

Let's make the search a little more complicated. We still want to find
all employees with a first name of nitin, but we want only employees who
are older than 30. Our query will change a little to accommodate a
filter, which allows us to execute structured searches efficiently:

res= es.search(index=\'megacorp\',body={

\'query\':{

\'bool\':{

\'must\':{

\'match\':{

\'first\_name\':\'nitin\'

}

},

\"filter\":{

\"range\":{

\"age\":{

\"gt\":25

}

}

}

}

}

})

print res\[\'hits\'\]\[\'hits\'\]

\[{u\'\_score\': 0.2876821, u\'\_type\': u\'employee\', u\'\_id\':
u\'1\', u\'\_source\': {u\'interests\': \[u\'sports\', u\'music\'\],
u\'age\': 27, u\'about\': u\'Love to play cricket\', u\'last\_name\':
u\'panwar\', u\'first\_name\': u\'nitin\'}, u\'\_index\':
u\'megacorp\'}\]

res= es.search(index=\'megacorp\',body={

\'query\':{

\'bool\':{

\'must\':{

\'match\':{

\'first\_name\':\'nitin\'

}

},

\"filter\":{

\"range\":{

\"age\":{

\"gt\":27

}

}

}

}

}

})

print res\[\'hits\'\]\[\'hits\'\]

\[\]

**Full text search**

The searches so far have been simple.Let's try more advanced full text
search. Before starting this next type of search let me insert one more
documnt.

e4={

\"first\_name\":\"asd\",

\"last\_name\":\"pafdfd\",

\"age\": 27,

\"about\": \"Love to play football\",

\"interests\": \[\'sports\',\'music\'\],

}

res=es.index(index=\'megacorp\',doc\_type=\'employee\',id=4,body=e4)

print res\[\'created\'\]

False

res= es.search(index=\'megacorp\',doc\_type=\'employee\',body={

\'query\':{

\'match\':{

\"about\":\"play cricket\"

}

}

})

for hit in res\[\'hits\'\]\[\'hits\'\]:

print hit\[\'\_source\'\]\[\'about\'\]

print hit\[\'\_score\'\]

print \'\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\'

Love to play football

0.7549128

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Love to play cricket

0.5753642

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

In above example it is returning two records but scores are differnt.

**Phrase Search**

Finding individual words in a field is all well and good, but sometimes
you want to match exact sequence of words of phrases.

res= es.search(index=\'megacorp\',doc\_type=\'employee\',body={

\'query\':{

\'match\_phrase\':{

\"about\":\"play cricket\"

}

}

})

for hit in res\[\'hits\'\]\[\'hits\'\]:

print hit\[\'\_source\'\]\[\'about\'\]

print hit\[\'\_score\'\]

print \'\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\'

Love to play cricket

0.5753642

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

**Aggregations**

Elasticsearch has functionality called aggregations, which allowed you
to generate sophisticated analytics over your data. It is similar to
Group By in SQL, but much more powerful.

res= es.search(index=\'megacorp\',doc\_type=\'employee\',body={

\"aggs\": {

\"all\_interests\": {

\"terms\": { \"field\": \"interests\" }

}

}

})

Please comment below if you liked the above article on Elasticseach, it
will definitely encourage me to write more or suggest any topic that you
want to read further.
