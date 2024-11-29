import json

#Controllers
from controllers.rdsController import rds
from controllers.cacheController import Redis

#Functions
from functions.userInput import userInput

def getData(redis_instance, value, input):
    rds_instance = rds()
    query = f"""
                SELECT 
                    f.title,
                    f.description,
                    f.release_year,
                    f.length,
                    f.rating,
                    c.name AS category_name,
                    l.name AS language,
                    GROUP_CONCAT(DISTINCT CONCAT(a.first_name, ' ', a.last_name) ORDER BY a.last_name) AS actors
                FROM 
                    film f
                JOIN 
                    film_category fc ON f.film_id = fc.film_id
                JOIN 
                    category c ON fc.category_id = c.category_id
                JOIN 
                    language l ON f.language_id = l.language_id
                JOIN 
                    film_actor fa ON f.film_id = fa.film_id
                JOIN 
                    actor a ON fa.actor_id = a.actor_id
                WHERE 
                    c.name = '{value[input]}'
                GROUP BY 
                    f.film_id, f.title, f.description, f.release_year, f.length, f.rating, c.name, l.name
                ORDER BY 
                    f.title;
                """

    data = rds_instance.getQueryData(rds_instance.connection, query)
    rds_instance.closeConnection()

    json_data = data.to_json(orient='records')

    key = f"{value[input]}Data"
    status = redis_instance.setValue(redis_instance.redis_client, key, json_data)

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

    getData(redis_instance=redis_instance, value=value, input=input)

    key = f"{value[input]}Data"
    value = json.loads(redis_instance.getValue(redis_instance.redis_client, key))

    print(key)
    

    