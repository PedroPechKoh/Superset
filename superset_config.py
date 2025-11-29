import os

# ---------------------------------------------------------
# 1. CONEXIONES DE NUBE (RAILWAY)
# ---------------------------------------------------------
# Usamos la variable pública si existe, si no, la privada.
# Esto asegura que siempre encuentre el camino.
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_PUBLIC_URL") or os.getenv("DATABASE_URL")

CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_URL": os.getenv("REDIS_URL"),
}

SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY")

# ---------------------------------------------------------
# 2. SEGURIDAD Y REDES (CORS & IFRAME)
# ---------------------------------------------------------
ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': [r"/*"],
    'origins': ["*"] 
}

TALISMAN_ENABLED = False 
WTF_CSRF_ENABLED = False

# ---------------------------------------------------------
# 3. FUNCIONALIDADES
# ---------------------------------------------------------
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True
}

# ---------------------------------------------------------
# 4. EL TRUCO MAESTRO (ADIÓS ERROR 403)
# ---------------------------------------------------------
# Al poner esto en "Admin", el usuario invitado tendrá acceso TOTAL
# a todas las bases de datos sin necesidad de configurar nada en el menú.
GUEST_ROLE_NAME = "Admin"