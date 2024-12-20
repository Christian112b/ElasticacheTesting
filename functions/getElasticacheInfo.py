import time
import random
from controllers.cacheController import Redis

def getElasticacheInfo():
    redis_instance = Redis()
    for i in range(100000):
        key = f"user:{i}"  # Genera una clave aleatoria
        value = f"data:{random.randint(1000, 99999)}"  # Genera un valor aleatorio
        print(value)
        redis_instance.redis_client.set(key, value)  # Ejecuta SET
        time.sleep(0.0001)  # Pausa de 10 ms entre cada operación para no sobrecargar el clúster
        