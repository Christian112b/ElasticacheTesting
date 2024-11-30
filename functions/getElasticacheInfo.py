from controllers.cacheController import Redis

def getElasticacheInfo():
    redis_instance = Redis()

    keys = redis_instance.listKeys(redis_instance)

    print(keys)