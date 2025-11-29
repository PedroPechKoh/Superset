# --- BASE IMAGE ---
FROM apache/superset:3.1.0

# --- USUARIO ROOT PARA INSTALACIÓN ---
USER root

# --- INSTALAMOS DRIVERS ---
RUN pip install --no-cache-dir psycopg2-binary redis pymysql cryptography flask-cors

# --- PUENTE PARA LIBRERÍAS ---
ENV PYTHONPATH="${PYTHONPATH}:/usr/local/lib/python3.10/site-packages"

# --- COPIAMOS CONFIGURACIÓN ---
COPY superset_config.py /app/pythonpath/superset_config.py

# --- VOLVEMOS A USUARIO superset ---
USER superset

# --- PUERTO POR DEFECTO (si Railway no lo inyecta automáticamente) ---
ENV PORT=8088

# --- COMANDO DE ARRANQUE CORRECTO ---
CMD gunicorn -w 2 --timeout 120 -b 0.0.0.0:$PORT "superset.app:create_app()"
