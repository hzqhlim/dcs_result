from django.contrib import admin
from .models import Lecture, Lecturer, Student, Status, Result

# Register your models here.
admin.site.register(Lecture)
admin.site.register(Lecturer)
admin.site.register(Student)
admin.site.register(Status)
admin.site.register(Result)

