FROM python:3 as base-py
WORKDIR /app

COPY requirments.txt .

RUN pip install -r requirments.txt


FROM base-py as socket-server

WORKDIR /app/src/

COPY src/. .

WORKDIR /app/src/socket

CMD ["python", "math_socket_server.py"]


FROM base-py as http-server

WORKDIR /app/src/

COPY src/. .

WORKDIR /app/src/http

CMD ["python", "math_http.py"]


FROM base-py as unit-tests

WORKDIR /app/src/logic

COPY src/logic .

WORKDIR /app/tests/unit

COPY tests/unit .

CMD ["python","-m",  "pytest", "tests.py"]


FROM base-py as integr-tests

WORKDIR /app/src/

COPY src/config.py .

WORKDIR /app/tests/integrational

COPY tests/integrational .

CMD ["python","-m",  "pytest", "tests.py"]


FROM base-py as alembic

COPY src .

WORKDIR /app/migration

COPY migration .

WORKDIR /app

COPY alembic.ini .

FROM alembic as alembic-tests

COPY tests/migrations/tests.py .