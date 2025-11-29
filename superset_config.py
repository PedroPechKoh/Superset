import os

# ===========================
# 🔐 SEGURIDAD (CORS / EMBEDDING)
# ===========================

TALISMAN_CONFIG = {
    "content_security_policy": {
        "frame-ancestors": ["*"],
    },
    "force_https": False,
    "session_cookie_secure": False,
}

ENABLE_CORS = True
CORS_OPTIONS = {
    "supports_credentials": True,
    "allow_headers": ["*"],
    "resources": [r"/*"],
    "origins": ["*"],
}

# 🔥 Necesario para usar APIs externas
WTF_CSRF_ENABLED = False
WTF_CSRF_EXEMPT_LIST = ["*"]

# ===========================
# 🗄️ CONEXIONES A RAILWAY
# ===========================

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_URL": os.getenv("REDIS_URL"),
}

SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "fallback-secret-key")

SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_pre_ping": True,
}

DATA_CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_REDIS_URL": os.getenv("REDIS_URL"),
}

# ===========================
# 🔥🔥 EMBEDDING Y GUEST TOKEN
# ===========================

FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "EMBEDDED_SUPERSET_API": True,   # ← Faltaba
}

ALLOW_GUEST_TOKEN = True             # ← Faltaba

GUEST_ROLE_NAME = "Public"           # ← Gamma causa 403

# ENLACE FINAL: Asigna el rol "Gamma" a todos los usuarios invitados/guest.
GUEST_ROLE_NAME = "Gamma"