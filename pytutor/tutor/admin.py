from django.contrib import admin
from .models import Question, Usr, TestCase, CourseMat



# Register your models here.

class TestCaseInline(admin.StackedInline):
    model = TestCase
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['question_content']}),
        ]
    inlines = [TestCaseInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Usr)
admin.site.register(CourseMat)
