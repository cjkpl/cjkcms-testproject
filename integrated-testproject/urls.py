from django.urls import include, path
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf import settings
import os.path

from wagtail import urls as wagtail_urls
from cjkcms import urls as cjkcms_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls


urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("", include(cjkcms_urls)),
    path("", include(wagtail_urls)),
]


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += (
        staticfiles_urlpatterns()
    )  # tell gunicorn where static files are in dev mode
    urlpatterns += static(
        f"{settings.MEDIA_URL}images/",
        document_root=os.path.join(settings.MEDIA_ROOT, "images"),
    )
    urlpatterns += [
        path(
            "favicon.ico",
            RedirectView.as_view(url=f"{settings.STATIC_URL}myapp/images/favicon.ico"),
        )
    ]
