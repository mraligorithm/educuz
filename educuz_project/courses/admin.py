from django.contrib import admin
from .models import Course, Content, Review

# Register your models here.
admin.site.register(Course)
admin.site.register(Content)
admin.site.register(Review)