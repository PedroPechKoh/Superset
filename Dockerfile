FROM apache/superset:latest

# Cambiamos a root para poder instalar cosas
USER root

# Actualizamos pip para evitar errores de compilación
RUN pip install --upgrade pip

# Instalamos los drivers OBLIGATORIOS
# psycopg2-binary -> Para conectar con Railway (PostgreSQL)
# redis -> Para la caché de Railway
# pymysql -> Para conectar con tu base de datos de datos (MySQL)
RUN pip install psycopg2-binary redis pymysql cryptography

# Copiamos tu configuración
COPY superset_config.py /app/pythonpath/superset_config.py

# Regresamos al usuario superset para que corra seguro
USER superset