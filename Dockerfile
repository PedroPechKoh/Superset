FROM apache/superset:latest

USER root

# --- EL TRUCO DE MAGIA ---
# Forzamos a que el sistema use el entorno virtual de Superset
ENV PATH="/app/.venv/bin:$PATH"

# Ahora sí, instalamos los drivers y SE GUARDARÁN donde deben
RUN pip install --no-cache-dir \
    psycopg2-binary \
    redis \
    pymysql \
    cryptography \
    flask-cors

# Copiamos la configuración
COPY superset_config.py /app/pythonpath/superset_config.py

# Regresamos al usuario seguro
USER superset