import os

# --- SEGURIDAD ---
# Permitimos que Superset se vea en cualquier sitio (luego lo restringiremos a tu dominio)
TALISMAN_CONFIG = {
    "content_security_policy": {
        "frame-ancestors": ["*"], 
    },
    "force_https": False,
    "session_cookie_secure": False,
}

ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': [r"/*"],
    'origins': ["*"] # Aceptamos todo por ahora para que no te falle al probar
}

WTF_CSRF_ENABLED = False 

# --- CONEXIONES DE NUBE (RAILWAY) ---
# Railway inyectará estos valores automáticamente
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_URL": os.getenv("REDIS_URL"),
}

SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY")