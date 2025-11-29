FROM apache/superset:latest

# Cambiamos a root
USER root

# Instalamos drivers Y AHORA TAMBIÉN flask-cors
RUN pip install --no-cache-dir \
    psycopg2-binary \
    redis \
    pymysql \
    cryptography \
    flask-cors  <-- ¡ESTA ES LA NUEVA!

# Copiamos config
COPY superset_config.py /app/pythonpath/superset_config.py

# Regresamos a usuario seguro
USER superset