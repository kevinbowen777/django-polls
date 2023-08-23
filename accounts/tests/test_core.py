from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from ..views import SignupPageView


class SignupPageTests(TestCase):
    username = "newuser"
    email = "newuser@example.com"

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Does not belong here.")

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(  # noqa:F841
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)


"""
class ProfilePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("user_detail")
        self.response = self.client.get(url)

    def test_profilepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_profilepage_url_name(self):
        response = self.client.get(reverse("user_detail"))
        self.assertEqual(response.status_code, 200)

    def test_profilepage_template(self):
        self.assertTemplateUsed(self.response, "account/user_detail.html")

    def test_profilepage_contains_correct_html(self):
        self.assertContains(self.response, "Profile Page")

    def test_profilepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "This text does not belong")

    def test_profilepage_url_resolves_profilepageview(self):
        view = resolve("/profile/")
        self.assertEqual(
            view.func.__name__,
            ProfilePageView.as_view().__name__,
        )
"""
