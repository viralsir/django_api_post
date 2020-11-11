from django.contrib import admin
from .models import course

class adminmodel(admin.ModelAdmin):
    list_display = ['name','durations']

# Register your models here.
admin.site.register(course,adminmodel)
