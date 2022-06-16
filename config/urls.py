from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),
    # User management
    path("accounts/", include("allauth.urls")),
    # Local applications
    path("", include("pages.urls")),
    path("polls/", include("polls.urls")),
]

if settings.DEBUG:
    import debug_toolbar  # noqa: F401  # pragma: no cover

    urlpatterns = [  # pragma: no cover
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
