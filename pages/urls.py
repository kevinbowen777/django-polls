from django.urls import path

from .views import (
    AboutPageView,
    ContactView,
    HomePageView,
    ProfilePageView,
    SuccessView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactView, name="contact"),
    path("success/", SuccessView, name="success"),
    path("profile/", ProfilePageView.as_view(), name="profile"),
]
