If you perform a GET operation you we notice the new field was truly added:
Request:
$ curl -XGET 'localhost:9200/novels/authors/2?pretty'
Response:
{
  "_index" : "novels",
  "_type" : "authors",
  "_id" : "2",
  "_version" : 2,
  "found" : true,
  "_source" : {
    "name" : "Charles Dickens",
    "novels_count" : 16,
    "Years" : "1812-1870"
  }
}
