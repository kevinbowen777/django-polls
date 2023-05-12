import datetime

import factory
import factory.fuzzy
import pytest

from accounts.tests.factories import UserFactory  # noqa: F401

from ..models import Question


@pytest.fixture
def question():
    return QuestionFactory()


class QuestionFactory(factory.django.DjangoModelFactory):
    question_text = factory.fuzzy.FuzzyText(length=25, prefix="What is the best ")
    pub_date = factory.fuzzy.FuzzyDate(datetime.date(2022, 11, 14))

    class Meta:
        model = Question
