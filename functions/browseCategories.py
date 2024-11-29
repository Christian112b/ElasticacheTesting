import json

#Controllers
from controllers.rdsController import rds
from controllers.cacheController import Redis

#Functions
from functions.userInput import userInput

def getData(value, input):
    rds_instance = rds()
    query = f"""
            SELECT f.title
            FROM film f
            JOIN film_category fc ON f.film_id = fc.film_id
            JOIN category c ON fc.category_id = c.category_id
            WHERE c.name = {value[input]};
        """
    
    print(query)

    data = rds_instance.getQueryData(rds_instance.connection, query)
    return data

def saveCategories():
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

    value = json.loads(redis_instance.getValue(redis_instance.redis_client, "Categorias"))

    inputString = f"Seleccione una categoria (0-{len(value)-1})."
    input = userInput(inputString, value)

    data = getData(value, input)
    

    