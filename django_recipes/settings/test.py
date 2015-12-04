from .base import *

SECRET_KEY="test"
DATABASES = {
          "default": {
                    "ENGINE": "django.db.backends.sqlite3",
                    "NAME": ":memory:",
                    "USER": "",
                    "PASSWORD": "",
                    "HOST": "",
                    "PORT": "",
                    },
}

