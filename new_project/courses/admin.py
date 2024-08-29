from django.contrib import admin

from django.contrib import admin
from .models import Course, Lecture

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_of_courses = ('title', 'rate', 'count')
    

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_of_users = ('user', 'age', 'course')
    
