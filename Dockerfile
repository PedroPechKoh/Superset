FROM apache/superset:latest

USER root

# 1. ACTUALIZAR PIP
RUN /app/.venv/bin/pip install --upgrade pip

# 2. INSTALACIÓN DE DRIVERS (TÉCNICA FRANCOTIRADOR)
# Usamos la ruta completa al pip del entorno virtual (/app/.venv/bin/pip)
# Agregamos --force-reinstall para asegurar que se instale sí o sí.
RUN /app/.venv/bin/pip install --no-cache-dir --force-reinstall psycopg2-binary redis pymysql cryptography

# 3. CONFIGURACIÓN
COPY superset_config.py /app/pythonpath/superset_config.py

# 4. VOLVER A USUARIO SEGURO
USER superset