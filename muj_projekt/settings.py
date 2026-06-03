import os
from pathlib import Path

# Základní adresář projektu
BASE_DIR = Path(__file__).resolve().parent.parent

# Tajný klíč (pro produkci by měl být skrytý, ale pro funkčnost ho necháváme)
SECRET_KEY = 'django-insecure-t#)@m%u0!_k5_@91^1g(ef0vzkf46m(1j-w-83hfj9(sjwsh+%'

# Debug režim necháme zapnutý, abychom viděli případné chyby
DEBUG = True

# BEZPEČNOST: Povolení domén pro lokální PC i PythonAnywhere
ALLOWED_HOSTS = ['makousek1.eu.pythonanywhere.com', '127.0.0.1', 'localhost']

# Definice nainstalovaných aplikací
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'skins',  # Tvoje aplikace se skiny
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

ROOT_URLCONF = 'muj_projekt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'muj_projekt.wsgi.application'


# --- DYNAMICKÉ NASTAVENÍ DATABÁZE ---
# Pokud proměnná 'PYTHONANYWHERE_SITE' existuje, znamená to, že kód běží online na serveru.
ON_PYTHONANYWHERE = 'PYTHONANYWHERE_SITE' in os.environ

if ON_PYTHONANYWHERE:
    # NASTAVENÍ PRO SERVER: Použije samostatný soubor SQLite (nepotřebuje XAMPP)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # NASTAVENÍ PRO TVŮJ POČÍTAČ: Připojí se k tvému XAMPP panelu (MySQL)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'blabla',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }


# Validace hesel
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


# Jazyk a časové pásmo
LANGUAGE_CODE = 'cs'
TIME_ZONE = 'Europe/Prague'
USE_I18N = True
USE_TZ = True


# Statické soubory (CSS, JS, obrázky)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Přesměrování po přihlášení a odhlášení
LOGIN_REDIRECT_URL = 'prehled_skinu'
LOGOUT_REDIRECT_URL = 'login'