from elasticsearch import Elasticsearch


# Configura el cliente Elasticsearch
es = Elasticsearch('localhost:9200')

print("haciendo ping al servidor Elasticsearch...")


# Verifica el estado de la conexión
if es.ping():
    print("Conexión exitosa con Elasticsearch.")
else:
    print("No se pudo establecer conexión con Elasticsearch.")
