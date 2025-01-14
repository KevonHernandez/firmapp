import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'firmas',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # BASE_DIR / 'templates',

        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {
            'timeout': 20,  # Aumenta el tiempo de espera a 20 segundos
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",

]

#mmodificar antes deponer en produccion
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Evitar que la aplicación sea cargada en un iframe (clickjacking)
X_FRAME_OPTIONS = 'DENY'  # Impide que tu sitio se cargue dentro de un iframe en otro sitio

# Impide que los navegadores intenten adivinar el tipo de contenido (helpful for XSS)
SECURE_CONTENT_TYPE_NOSNIFF = True

# # Impide que los navegadores realicen "sniffing" de los archivos y contenido
# SECURE_BROWSER_XSS_FILTER = True

# Protege las respuestas HTTP para que no se puedan modificar a través de ciertos tipos de ataques.
SECURE_REFERRER_POLICY = 'same-origin'

# Limita la duración de la sesión
SESSION_COOKIE_AGE = 3600  # La sesión expira en 360 seg 

# Impide que la cookie de sesión se envíe a otros dominios
SESSION_COOKIE_DOMAIN = None  # Esto asegura que la cookie solo sea accesible desde el dominio actual.

# Hacer que la cookie de sesión tenga solo acceso HTTP (no accesible a través de JavaScript)
SESSION_COOKIE_HTTPONLY = True  # Esto evita que la cookie sea accesible a través de JavaScript.

# Fuerza el uso de HTTPS
# SECURE_SSL_REDIRECT = True  # Redirige automáticamente todo el tráfico HTTP a HTTPS

# Asegura que la cookie de sesión solo se envíe a través de HTTPS
# SESSION_COOKIE_SECURE = True  # Solo se enviará por HTTPS

# Hacer que las cookies de sesión sean más seguras
# CSRF_COOKIE_SECURE = True  # Solo envía la cookie CSRF en conexiones HTTPS
CSRF_COOKIE_HTTPONLY = True  # Evita que la cookie CSRF sea accesible a través de JavaScript