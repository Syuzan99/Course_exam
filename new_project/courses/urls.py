from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_of_the_courses, name='list_of_the_courses'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('<int:course_id>/rate/', views.rate_course, name='rate_course'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
]