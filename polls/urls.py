from django.urls import path

from . import views

urlpatterns = [
    path("", views.PollListView.as_view(), name="poll_list"),
    path("<int:pk>/", views.PollDetailView.as_view(), name="poll_detail"),
    path(
        "<int:pk>/results/",
        views.PollResultsView.as_view(),
        name="poll_results",
    ),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
