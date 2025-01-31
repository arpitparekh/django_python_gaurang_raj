from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'address', 'img')
    list_filter = ('name', 'age', 'address', 'img')
    search_fields = ('name', 'age', 'address', 'img')
    ordering = ('name', 'age', 'address', 'img')
    filter_horizontal = ()
    fieldsets = ()


# Register your models here.
# admin.site.register(Student)

