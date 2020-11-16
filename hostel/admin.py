from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Room')
    ordering = ('Name',)
    search_fields = ('Room',)

admin.site.register(Student, StudentAdmin)