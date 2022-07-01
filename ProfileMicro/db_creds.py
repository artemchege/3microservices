import os

POSTGRES_USER = os.environ.get('POSTGRES_USER', 'fastapi')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', '1234')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'db')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', '5432')
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'fastapi')
