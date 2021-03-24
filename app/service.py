from torpedo import Host

from .routes import blueprint_group
from .listeners import listeners


if __name__ == '__main__':

    # register combined blueprint group here. these blueprints are defined in the routes directory and has to be
    # collected in init file otherwise route will end up with 404 error.
    Host._listeners = listeners
    Host._blueprint_group = blueprint_group

    Host.run()
