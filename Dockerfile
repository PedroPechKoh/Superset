# Dockerfile
FROM apache/superset:latest

USER root

# Instalamos los conectores para que Superset pueda hablar con PostgreSQL y Redis en la nube
RUN pip install psycopg2-binary redis

# Copiamos la configuración que crearemos en el siguiente paso
COPY superset_config.py /app/pythonpath/superset_config.py

# Volvemos al usuario seguro
USER superset