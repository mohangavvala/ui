from django.contrib import admin
from testapp.models import Student

# Register your models here.
class Student_Admin(admin.ModelAdmin):
    list_display=['id','name','rollno','marks','bf','gf']
admin.site.register(Student,Student_Admin)
