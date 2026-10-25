from typing import ClassVar

from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets: ClassVar[list[tuple]] = [
        (None, {"fields": ["question_text"]}),
        (
            "Date information",
            {"fields": ["pub_date"], "classes": ["collapse"]},
        ),
    ]
    inlines: ClassVar[list] = [ChoiceInline]
    list_display = ("question_text", "pub_date", "was_published_recently")
    list_filter: ClassVar[list[str]] = ["pub_date"]
    search_fields: ClassVar[list[str]] = ["question_text"]
