import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


def create_question(question_text, days):
    """
    Create a question with the given 'question_text' and published
    the given number of 'days' offset to now (negative for questions
    published in the past, positive for questions that have yet to
    be published.
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="pollreader",
            email="pollreader@example.com",
            password="testpass123",
        )

    def test_question_index_view_for_logged_out_user(self):
        response = self.client.get(reverse("polls"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, "%s?next=/polls/" % (reverse("account_login"))
        )
        response = self.client.get(
            "%s?next=/polls/" % (reverse("account_login"))
        )
        self.assertContains(response, "Log In")

    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        self.client.login(
            email="pollreader@example.com", password="testpass123"
        )
        response = self.client.get(reverse("polls"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are currently available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the polls page.
        """
        self.client.login(
            email="pollreader@example.com", password="testpass123"
        )
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't
        displayed on the polls page.
        """
        self.client.login(
            email="pollreader@example.com", password="testpass123"
        )
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        self.client.login(
            email="pollreader@example.com", password="testpass123"
        )
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions polls page may display multiple questions.
        """
        self.client.login(
            email="pollreader@example.com", password="testpass123"
        )
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )


class QuestionDetailViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="pollreader",
            email="pollreader@example.com",
            password="testpass123",
        )

    def test_question_detail_view_for_logged_out_user(self):
        response = self.client.get(reverse("polls"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, "%s?next=/polls/" % (reverse("account_login"))
        )
        response = self.client.get(
            "%s?next=/polls/" % (reverse("account_login"))
        )
        self.assertContains(response, "Log In")

    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the
        future returns a 404 not found.
        """
        self.client.login(
            email="pollreader@example.com", password="testpass123"
        )
        future_question = create_question(
            question_text="Future question.", days=5
        )
        url = reverse("detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        self.client.login(
            email="pollreader@example.com", password="testpass123"
        )
        past_question = create_question(
            question_text="Past question.", days=-5
        )
        url = reverse("detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


class QuestionResultsViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="pollreader",
            email="pollreader@example.com",
            password="testpass123",
        )

    def test_question_results_view_for_logged_out_user(self):
        response = self.client.get(reverse("polls"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, "%s?next=/polls/" % (reverse("account_login"))
        )
        response = self.client.get(
            "%s?next=/polls/" % (reverse("account_login"))
        )
        self.assertContains(response, "Log In")

    def test_future_question(self):
        """
        The results view of a question with a pub_date in the
        future returns a 404 not found.
        """
        self.client.login(
            email="pollreader@example.com", password="testpass123"
        )
        future_question = create_question(
            question_text="Future question.", days=5
        )
        url = reverse("results", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The results view of a question with a pub_date in the past
        displays the question's results.
        """
        self.client.login(
            email="pollreader@example.com", password="testpass123"
        )
        past_question = create_question(
            question_text="Past question.", days=-5
        )
        url = reverse("results", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for
        questions whose pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for
        questions whose pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(
            hours=23, minutes=59, seconds=59
        )
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for
        questions whose pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)

        self.assertIs(future_question.was_published_recently(), False)
