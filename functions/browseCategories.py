import json

#Controllers
from controllers.rdsController import rds
from controllers.cacheController import Redis

def saveCategories(rds_instance):
    rds_instance = rds()
    query = "SELECT name FROM category"
    categories = rds_instance.getQueryData(rds_instance.connection, query)
    rds_instance.closeConnection()

    categories_names = categories['name'].tolist()
    categories_json = json.dumps(categories_names)

    redis_instance = Redis()
    status = redis_instance.setValue(redis_instance.redis_client, "Categorias", categories_json)

    return redis_instance

def browseCategories():

    redis_instance = saveCategories()

    value = redis_instance.getValue(redis_instance.redis_client, "Categorias")
    print(value)

    

    