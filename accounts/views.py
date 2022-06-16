from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # Tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"

    template_name = "account/user_detail.html"


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = [
        "name",
        "bio",
    ]
    model = User

    # Send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse(
            "user_detail",
            kwargs={"username": self.request.user.username},
        )

    def get_object(self):
        # Only get the user record for the user making the request
        return User.objects.get(username=self.request.user.username)

    template_name = "account/user_form.html"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(
            "user_detail",
            kwargs={"username": self.request.user.username},
        )
