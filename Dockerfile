FROM apache/superset:latest

USER root

# 1. Instalamos los drivers en el sistema global (donde root tiene permiso)
RUN pip install --no-cache-dir psycopg2-binary redis pymysql cryptography flask-cors

# 2. EL PUENTE MÁGICO 🌉
# Le decimos a Superset que busque librerías también en la carpeta global
ENV PYTHONPATH="${PYTHONPATH}:/usr/local/lib/python3.10/site-packages"

# Copiamos la configuración
COPY superset_config.py /app/pythonpath/superset_config.py

USER superset