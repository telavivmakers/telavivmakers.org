from os import environ

if 'PROD' in environ:
    from .prod import *
else:
    from .local import *
