import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from ..models import Choice, Question


def create_question(question_text, days):
    """
    Create a question with the given 'question_text' and published
    the given number of 'days' offset to now (negative for questions
    published in the past, positive for questions that have yet to
    be published.
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


def create_choice(question, choice_text, votes):
    return Choice.objects.create(
        question=question, choice_text=choice_text, votes=votes
    )


class ChoiceTests(TestCase):
    def setUp(self):
        self.question = create_question(question_text="Current question.", days=0)
        self.choice = create_choice(
            question=self.question, choice_text="Seven logs", votes=3
        )

    def test___str__(self):
        assert self.choice.__str__() == self.choice.choice_text
        assert str(self.choice) == self.choice.choice_text


class QuestionTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="johndoe",
            email="johndoe@example.com",
            password="secret",
        )
        self.question = create_question(question_text="Current question.", days=0)

        """
        self.question = Question.objects.create(
            question_text="How much wood can a woodchuck chuck?",
            pub_date=timezone.now(),
        )
        """

    def test___str__(self):
        assert self.question.__str__() == self.question.question_text
        assert str(self.question) == self.question.question_text

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
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
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
