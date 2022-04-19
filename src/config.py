import os

HOST = os.getenv('HOST', '127.0.0.1')
POSTGRES_HOST = os.getenv('POSTGRES_HOST') or os.getenv('HOST') or '127.0.0.1'
USER = os.getenv('POSTGRES_USER', 'postgres')
PASSWORD = os.getenv('POSTGRES_PASSWORD', 'admin')
POSTGRES_NAME = os.getenv('POSTGRES_DB', 'math_operations')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', 5432)
CLIENT_HOST = os.getenv('CLIENT_HOST') or os.getenv('HOST') or '127.0.0.1'
HTTP_PORT = os.getenv('HTTP_PORT', 65433)
SOCKET_PORT = os.getenv('SOCKET_PORT', 65432)

URL_DB = f'postgresql://{USER}:{PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}'
