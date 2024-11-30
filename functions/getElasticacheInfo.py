from controllers.cacheController import Redis

def getElasticacheInfo():
    redis_instance = Redis()

    #keys = redis_instance.scanKeys(redis_instance)
    for key in redis_instance.scan_iter("user:*"):
        print(key)
        #r.delete(key)
