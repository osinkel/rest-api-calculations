import socket
import sys
import requests
sys.path.append('../../')
from src.config import HOST, SOCKET_PORT, HTTP_PORT, CLIENT_HOST


def test_http_server_operation_add():
    response = requests.get(f"http://{HOST}:{HTTP_PORT}/add?n1=-0.5&n2=2")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"


def test_http_server_operation_filter_operator_limit_offset():
    response = requests.get(f"http://{HOST}:{HTTP_PORT}/filter/add?limit=10&offset=0")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


def test_http_server_operation_filter_operator_limit():
    response = requests.get(f"http://{HOST}:{HTTP_PORT}/filter/add?limit=10")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


def test_http_server_operation_filter_operator_offset():
    response = requests.get(f"http://{HOST}:{HTTP_PORT}/filter/add?offset=0")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


def test_http_server_operation_filter_operator():
    response = requests.get(f"http://{HOST}:{HTTP_PORT}/filter/add")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


def test_http_server_operation_filter():
    response = requests.get(f"http://{HOST}:{HTTP_PORT}/filter/")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


def test_socket_server_operation():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((CLIENT_HOST, int(SOCKET_PORT)))
        msg = (''.join(str(x) + ' ' for x in ['add', '2', '3'])).encode("UTF-8")
        s.sendall(msg)
        data = str(s.recv(1024), 'utf-8')
    assert data == '5.0'
