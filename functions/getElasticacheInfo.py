import time
import random
from controllers.cacheController import Redis

def getElasticacheInfo():
    redis_instance = Redis()
    for i in range(1000):
        key = f"user:{random.randint(1000, 9999)}"  # Genera una clave aleatoria
        value = f"data:{random.randint(1000, 9999)}"  # Genera un valor aleatorio
        redis_instance.set(key, value)  # Ejecuta SET
        time.sleep(0.01)  # Pausa de 10 ms entre cada operación para no sobrecargar el clúster
        