FROM apache/superset:3.1.0

USER root

# Drivers
RUN pip install --no-cache-dir psycopg2-binary redis pymysql cryptography flask-cors

# Permitir que Superset encuentre librerías del sistema
ENV PYTHONPATH="${PYTHONPATH}:/usr/local/lib/python3.10/site-packages"

# Configuración personalizada
COPY superset_config.py /app/pythonpath/superset_config.py

USER superset
