FROM apache/superset:3.1.0

USER root

# Instalamos drivers
RUN pip install --no-cache-dir psycopg2-binary redis pymysql cryptography flask-cors

# Puente para librerías
ENV PYTHONPATH="${PYTHONPATH}:/usr/local/lib/python3.10/site-packages"

# Copiamos configuración
COPY superset_config.py /app/pythonpath/superset_config.py

USER superset

# --- LA SOLUCIÓN DEFINITIVA ---
# Grabamos el comando de arranque directamente en la imagen.
# Ya no intentará crear usuarios ni instalar nada, solo PRENDERÁ.
CMD gunicorn -w 2 --timeout 120 -b 0.0.0.0:$PORT "superset.app:create_app()"
