INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # test app with models
    'tests.myapp',
    # app being tested
    'reusable_app'
]


# avoid warning
USE_TZ = True


# faster user creation
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]


# no emails
# https://docs.djangoproject.com/en/4.2/topics/testing/tools/#topics-testing-email
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"


# no persistence, speed up tests by avoiding disk access
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.InMemoryStorage"
    }
}

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': ':memory:',
  }
}