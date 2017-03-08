from django.contrib import admin

# Register your models here.

from sqlobj.models import Answer, Question

admin.site.register(Answer)
admin.site.register(Question)