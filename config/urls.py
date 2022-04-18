from django.contrib import admin
from django.urls import include, path

from .views import AboutPageView, HomePageView

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),
    # User management
    path("accounts/", include("django.contrib.auth.urls")),
    # Local applications
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("accounts/", include("accounts.urls")),
    path("polls/", include("polls.urls")),
]
