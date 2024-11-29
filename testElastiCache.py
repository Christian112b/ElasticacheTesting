from rediscluster import RedisCluster
import mysql.connector
from mysql.connector import Error

# Configuración de ElastiCache
ELASTICACHE_CLUSTER_ENDPOINT = "sakila-cluster.lsysnh.clustercfg.use2.cache.amazonaws.com"
PORT = 6379

# Configuración de RDS (MySQL)
RDS_HOST = "sakiladb.c5s22mos0ltq.us-east-2.rds.amazonaws.com"
RDS_USER = "admin"
RDS_PASSWORD = "passwordsakila"
RDS_DATABASE = "sakila"

# Conexión a ElastiCache
try:
    redis_client = RedisCluster(
        startup_nodes=[{"host": ELASTICACHE_CLUSTER_ENDPOINT, "port": PORT}],
        decode_responses=True,
        skip_full_coverage_check=True
    )

    # Ejemplo: Almacenar en Redis
    redis_client.set("prueba_clave", "Hola desde Python", ex=30)
    print("Valor almacenado correctamente en Redis.")
    
    # Recuperar el valor de Redis
    valor = redis_client.get("prueba_clave")
    print(f"Valor recuperado de Redis: {valor}")

except Exception as e:
    print(f"Error al conectar o interactuar con Redis: {e}")


# Conexión a RDS MySQL
try:
    # Conectar a la base de datos MySQL en RDS
    connection = mysql.connector.connect(
        host=RDS_HOST,
        user=RDS_USER,
        password=RDS_PASSWORD,
        database=RDS_DATABASE
    )

    if connection.is_connected():
        print("Conexión a la base de datos RDS exitosa.")

        # Realizar una consulta a la base de datos (Ejemplo: Seleccionar datos)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM actor")  # Asume que tienes una tabla llamada 'clientes'
        rows = cursor.fetchall()

        # Mostrar los resultados
        for row in rows:
            print(row)

except Error as e:
    print(f"Error al conectar a RDS: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión a RDS cerrada.")
