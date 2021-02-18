curl -X PUT "localhost:9200/_cluster/settings?pretty" -H 'Content-Type: application/json' -d'
{
  "persistent": {
    "action.auto_create_index": "my-index-000001,index10,-index1*,+ind*" 
  }
}
'
curl -X PUT "localhost:9200/_cluster/settings?pretty" -H 'Content-Type: application/json' -d'
{
  "persistent": {
    "action.auto_create_index": "false" 
  }
}
'
curl -X PUT "localhost:9200/_cluster/settings?pretty" -H 'Content-Type: application/json' -d'
{
  "persistent": {
    "action.auto_create_index": "true" 
  }
}
'