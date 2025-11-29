FROM apache/superset:latest

USER root

# TÉCNICA DE INSERCIÓN DIRECTA
# El error nos dijo que Superset busca en: /app/.venv/lib/python3.10/site-packages/
# Así que forzamos la instalación EXACTAMENTE ahí.

RUN pip install --target=/app/.venv/lib/python3.10/site-packages/ \
    psycopg2-binary \
    redis \
    pymysql \
    cryptography

# Copiamos tu configuración
COPY superset_config.py /app/pythonpath/superset_config.py

# Volvemos al usuario seguro
USER superset