from django.contrib import admin
from .models import Student


# Register your models here.
@admin.register(Student)
class StudentRegistration(admin.ModelAdmin):
    list_display = ['id', 'roll', 'full_name', 'email', 'password']
