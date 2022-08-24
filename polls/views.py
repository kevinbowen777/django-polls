from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import DetailView, ListView

from .models import Choice, Question


class PollListView(LoginRequiredMixin, ListView):
    template_name = "polls/poll_list.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including
        those set to be published in the future.
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class PollDetailView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = "polls/poll_detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class PollResultsView(DetailView, LoginRequiredMixin):
    model = Question
    template_name = "polls/poll_results.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/poll_detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        """
        Always return an HttpResponseRedirect after successfully
        dealing with POST data. This prevents data from being posted
        twice if a user hits the Back Button.
        """
        return HttpResponseRedirect(
            reverse("poll_results", args=(question.id,))
        )
