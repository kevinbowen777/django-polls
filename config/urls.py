from django.contrib import admin
from django.urls import include, path
from polls.views import HomePageView

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),
    # User management
    path("accounts/", include("django.contrib.auth.urls")),
    # Local applications
    path("", HomePageView.as_view(), name="home"),
    path("polls/", include("polls.urls")),
]
