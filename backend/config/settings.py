from pathlib import Path


VERSION = '1.0.2'  # Меняйте эту версию при каждом деплое


BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = "django-insecure-o(#^8wul$xx1qm5+vxq+mu^vlb&7s8d1%ztf-jamuqi5nt=hef"

DEBUG = True

ALLOWED_HOSTS = ["51.250.51.93", "speakswift.ru", "127.0.0.1", "localhost", "158.160.141.187", "sstestserver.zapto.org"]

INSTALLED_APPS = [
    "speakswift.apps.SpeakswiftConfig",
    "django_user_agents",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django_user_agents.middleware.UserAgentMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR.joinpath(Path("static")).joinpath(Path("templates")),
            BASE_DIR.joinpath(Path("static_dev")).joinpath(Path("templates")),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "speakswift.context_processors.version_context",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"
TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR.joinpath(Path("static_dev")),]
STATIC_ROOT = BASE_DIR.joinpath(Path('static'))

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "speakswift.User"


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR.joinpath(Path('logs')).joinpath(Path('debug.log')),
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {  # пустая строка означает корневой логгер
            'handlers': ['file', 'console'],
            'level': 'INFO',
        },
        'speakswift': {  # логгер для вашего приложения
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}