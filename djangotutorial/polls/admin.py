from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):  #
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "was_published_recently"]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
