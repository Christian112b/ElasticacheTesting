import config
from rediscluster import RedisCluster

class Redis:
    def __init__(self):
        self.clusterEndpoint = config.ELASTICACHE_CLUSTER_ENDPOINT
        self.port = config.PORT

        self.redis_client = self.getConnection()

    def getConnection(self):
        try:
            redis_client = RedisCluster(
            startup_nodes=[{"host": self.clusterEndpoint, "port": self.port}],
            decode_responses=True,
            skip_full_coverage_check=True
            )

            return redis_client

        except Exception as e:
             print(f"Error al conectar o interactuar con Redis: {e}")
             return None

    def setValue(self, redis_client, key, value, exValue=None):
        try:
            if exValue == None:
                redis_client.set(key, value)
            else:
                redis_client.set(key, value, ex=exValue)

            return "OK"
        except Exception as e:
            print(f"Error al establecer el valor en Redis: {e}")
            return "ERROR"
        

    def getValue(self, redis_client, key):
        try:
            value = redis_client.get(key)
            return value
        except Exception as e:
            print(f"Error al obtener el valor de Redis: {e}")
            return None

    def listKeys(self, redis_client, pattern="*"):
        try:
            keys = redis_client.keys(pattern)
            return keys
        except Exception as e:
            print(f"Error al obtener las claves de Redis: {e}")
            return []