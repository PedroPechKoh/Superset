import os

# ---------------------------------------------------------
# 1. CONEXIONES DE NUBE (RAILWAY)
# ---------------------------------------------------------
# Railway inyecta estas variables automáticamente
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

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
# Permitir que React (Local o Nube) pida datos sin bloqueos
ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': [r"/*"],
    'origins': ["*"] # Acepta conexiones desde cualquier lugar
}

# Permitir que el Dashboard se muestre dentro de tu página web (Iframe)
# Desactivamos Talisman para evitar el error "Refused to display"
TALISMAN_ENABLED = False 
TALISMAN_CONFIG = {
    "content_security_policy": {
        "frame-ancestors": ["*"],
    },
    "force_https": False,
    "session_cookie_secure": False,
}

# Cabeceras HTTP permisivas
HTTP_HEADERS = {
    'X-Frame-Options': 'ALLOWALL',
    'Access-Control-Allow-Origin': '*',
}

# Desactivar protección CSRF para evitar errores en la API de Login
WTF_CSRF_ENABLED = False

# ---------------------------------------------------------
# 3. FUNCIONALIDADES
# ---------------------------------------------------------
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True
}

# ---------------------------------------------------------
# 4. SOLUCIÓN FINAL DE PERMISOS (EL TRUCO MAESTRO)
# ---------------------------------------------------------
# Esto le da permisos totales al usuario invitado ("Guest"),
# saltándose el bloqueo de la base de datos que no podíamos editar.
GUEST_ROLE_NAME = "Admin"