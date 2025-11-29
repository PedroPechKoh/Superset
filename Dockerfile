FROM apache/superset:latest

USER root

# Instalamos todos los drivers necesarios en una sola linea limpia
RUN pip install --no-cache-dir psycopg2-binary redis pymysql cryptography flask-cors

COPY superset_config.py /app/pythonpath/superset_config.py

USER superset