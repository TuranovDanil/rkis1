from django.contrib import admin

from .forms import RequiredInlineFormSet
from .models import Question, Choice, AbsUser


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3
    formset = RequiredInlineFormSet
    fields = ('choice_text',)


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
admin.site.register(AbsUser)
