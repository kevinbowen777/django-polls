from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from .views import AboutPageView, HomePageView, ProfilePageView

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),
    # User management
    path("accounts/", include("allauth.urls")),
    # Local applications
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("profile/", ProfilePageView.as_view(), name="profile"),
    path("polls/", include("polls.urls")),
]

if settings.DEBUG:
    import debug_toolbar  # noqa: F401

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
