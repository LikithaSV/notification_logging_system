from torpedo import Host, CONFIG
from redis_wrapper.register_redis_connection import RegisterRedis
# from app.listeners import listeners
from app.routes import blueprint_group

if __name__ == "__main__":

    # register combined blueprint group here.
    # these blueprints are defined in the routes directory and has to be
    # collected in init file otherwise route will end up with 404 error.
    RegisterRedis.register_redis_cache(CONFIG.config["REDIS_CACHE_HOSTS"])
    # Host._listeners = listeners
    Host._blueprint_group = blueprint_group

    Host.run()
