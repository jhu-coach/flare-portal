# Most of the settings are set in base.py, that's why this file appears fairly
# empty.
from .base import *  # noqa

# Explicitly disable debug mode in production
DEBUG = False

# Security configuration

# Ensure that the session cookie is only sent by browsers under an HTTPS connection.
# https://docs.djangoproject.com/en/stable/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True

# Ensure that the CSRF cookie is only sent by browsers under an HTTPS connection.
# https://docs.djangoproject.com/en/stable/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True

CORS_ALLOW_ALL_ORIGINS = True

# CORS and CSRF settings
INSTALLED_APPS += ["corsheaders"]
MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

CORS_ALLOWED_ORIGINS = [
    "https://flare-portal-4cd977e0207e.herokuapp.com",  # Replace with your real URL
]

CSRF_TRUSTED_ORIGINS = [
    "https://flare-portal-4cd977e0207e.herokuapp.com",
]

# Optional: Recommended HTTPS security settings
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

DEFAULT_FILE_STORAGE = 'storages.backends.b2.B2Storage'
B2_APPLICATION_KEY_ID = os.environ.get('B2_APPLICATION_KEY_ID')
B2_APPLICATION_KEY = os.environ.get('B2_APPLICATION_KEY')
B2_BUCKET_NAME = os.environ.get('B2_BUCKET_NAME')


