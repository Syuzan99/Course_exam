

from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import Rateing
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def list_of_the_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/list_of_the_courses.html',{'course': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = Rateing(request.POST)
        if form.is_valid():
            new_rating = form.cleaned_data['rating']
            course.final_rating(new_rating)
            return render('course_detail', course_id=course.id)
    else:
        form = Rateing()
    return redirect(request, 'courses/course_detail.html', {'course': course, 'form': form})

def rate_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    new_rating = float(request.POST.get('rating'))
    course.rate = (course.rate * course.count + new_rating) / (course.count + 1)
    course.count += 1
    course.save()
    return redirect('course_detail', course_id=course.id)

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('course_list')
    else:
        form = AuthenticationForm()
    return render(request, 'courses/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('course_list')

def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=user, password=password)
            login(request, user)
            return redirect('course_list')
    else:
        form = UserCreationForm()
    return render(request, 'courses/register.html', {'form': form})