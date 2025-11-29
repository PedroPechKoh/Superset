import os

# ===========================
# 🔐 SEGURIDAD BÁSICA (RAILWAY)
# ===========================

# --- Frame embedding (para React, Preset o front externo) ---
TALISMAN_CONFIG = {
    "content_security_policy": {
        "frame-ancestors": ["*"],  # Permite incrustar desde cualquier dominio
    },
    "force_https": False,
    "session_cookie_secure": False,
}

# --- CORS (para frontend externo como Vite/React) ---
ENABLE_CORS = True
CORS_OPTIONS = {
    "supports_credentials": True,
    "allow_headers": ["*"],
    "resources": [r"/*"],
    "origins": ["*"],  # Permite todo para pruebas → cámbialo después
}

# --- Desactivar CSRF para API Embedding ---
WTF_CSRF_ENABLED = False


# ===========================
# 🗄️ CONEXIONES A SERVICIOS EN RAILWAY
# ===========================

# Base de datos
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

# Redis cache
CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_URL": os.getenv("REDIS_URL"),
}

# Llave secreta
SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "fallback-secret-key")


# ===========================
# 💾 EXTRA – Ajustes recomendados
# ===========================

# Evita warning al usar MySQL
SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_pre_ping": True,
}

# Para evitar fallas de compresión
DATA_CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_REDIS_URL": os.getenv("REDIS_URL"),
}

# ¡ESTO ES LO QUE FALTABA!
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True
}