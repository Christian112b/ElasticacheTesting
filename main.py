import os
import sys
import json

sys.path.append(os.path.join(os.path.dirname(__file__), 'controllers'))

from controllers.rdsController import rds
from controllers.cacheController import Redis
from functions.userInput import userInput

if __name__ == "__main__":

    inputString = "Ingrese una opcion."
    inputOption = ["Buscar Pelicula por categoria"]
    input = userInput(inputString, inputOption)

    print(f"El input fue {input}")

    rds_instance = rds()
    
    # Ejecutar una consulta
    query = "SELECT name FROM category"
    categories = rds_instance.getQueryData(rds_instance.connection, query)
    rds_instance.closeConnection()

    categories_names = categories['name'].tolist()
    categories_json = json.dumps(categories_names)
    

    redis_instance = Redis()
    status = redis_instance.setValue(redis_instance.redis_client, "Categorias", categories_json)

    if status == "OK":
        value = redis_instance.getValue(redis_instance.redis_client, "Categorias")
        print(value)
    
    
    # Cerrar la conexión
    


