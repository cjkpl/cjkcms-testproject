# boot_django.py
#
# This file sets up and configures Django. It's used by scripts that need to
# execute as if running in a Django server.
import os
import django
from django.conf import settings

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "myapp"))
BASE_URL = "http://localhost:8000"


def boot_django():
    settings.configure(
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
            }
        },
        INSTALLED_APPS=(
            "myapp",  # replace with your app name
            # --- wagtail-cjkcms + requirements #
            "cjkcms",
            "wagtailseo",
            "wagtailcache",
            "wagtail.contrib.table_block",
            "wagtail.contrib.settings",
            "wagtail_color_panel",
            "django_bootstrap5",
            # --- end-wagtail-cjkcms #
            "wagtail.contrib.forms",
            "wagtail.contrib.redirects",
            "wagtail.contrib.sitemaps",
            "django.contrib.sitemaps",
            "wagtail.embeds",
            "wagtail.sites",
            "wagtail.users",
            "wagtail.snippets",
            "wagtail.documents",
            "wagtail.images",
            "wagtail.search",
            "wagtail.admin",
            "wagtail",
            "taggit",
            "modelcluster",
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
        ),
        MIDDLEWARE=[
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.middleware.common.CommonMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
            "django.middleware.clickjacking.XFrameOptionsMiddleware",
            "django.middleware.security.SecurityMiddleware",
            "wagtail.contrib.redirects.middleware.RedirectMiddleware",
        ],
        SECRET_KEY="not-important",
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [
                    os.path.join(BASE_DIR, "templates"),
                ],
                "APP_DIRS": True,
                "OPTIONS": {
                    "context_processors": [
                        "django.template.context_processors.debug",
                        "django.template.context_processors.request",
                        "django.contrib.auth.context_processors.auth",
                        "django.contrib.messages.context_processors.messages",
                    ],
                },
            },
        ],
        WAGTAILADMIN_BASE_URL=BASE_URL,
        BASE_URL=BASE_URL,
        ROOT_URLCONF="boot_urls",
        STATIC_ROOT=os.path.join(BASE_DIR, "static"),
        STATIC_URL="/static/",
        MEDIA_ROOT=os.path.join(BASE_DIR, "media"),
        MEDIA_URL="/media/",
        LANGUAGE_CODE="en-us",
        TIME_ZONE="UTC",
        USE_I18N=True,
        USE_L10N=True,
        USE_TZ=True,
    )
    django.setup()
