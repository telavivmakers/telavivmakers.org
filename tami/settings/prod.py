from .base import *

from os import environ

ENV = 'prod'

SECRET_KEY = environ.get('DJANGO_SECRET_KEY')
