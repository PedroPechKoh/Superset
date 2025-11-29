FROM apache/superset:latest

# Cambiamos a root para tener permisos de instalación
USER root

# Instalamos los drivers usando el comando estándar
# Esto los instalará donde sea que Python esté configurado
RUN pip install --no-cache-dir psycopg2-binary redis pymysql cryptography

# Copiamos tu configuración
COPY superset_config.py /app/pythonpath/superset_config.py

# Volvemos al usuario seguro
USER superset