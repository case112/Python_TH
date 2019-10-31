from django.contrib import admin

from . import models

class QuizAdmin(admin.ModelAdmin):
	fields = ['course', 'title', 'description', 'order', 'total_questions']


admin.site.register(models.Course)
admin.site.register(models.Text)
admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.MultipleChoiceQuestion)
admin.site.register(models.TrueFalseQuestion)
admin.site.register(models.Answer)