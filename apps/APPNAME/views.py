# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
    context = {
    "courses":Course.objects.all()
    }
    return render(request, 'APPNAME/index.html', context)

def add(request):
    Course.objects.create(course_name=request.POST['course_name'], description=request.POST['description'])
    return redirect('/')

def remove(request, id):
    course = Course.objects.get(id=id)
    context = {
    "course_name":course.course_name,
    "description":course.description,
    "id":course.id
    }
    return render(request, 'APPNAME/remove.html', context)

def remove_confirm(request, id):
    course = Course.objects.get(pk=id)
    course.delete()
    return redirect('/')
