from elasticsearch import Elasticsearch


# Configura el cliente Elasticsearch
es = Elasticsearch('localhost:9200')


# trae el primer usuario
res = es.get(index="usuarios", id=1)
print(res['_source'])

print()

# traer todos los usuarios
res = es.search(index="usuarios")
print(res)
