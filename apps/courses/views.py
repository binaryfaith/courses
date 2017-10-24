from __future__ import unicode_literals
from .models import Course
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def create(request):
    errors = Course.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        
    else:
        Course.objects.create(
            name=request.POST['name'],
            description=request.POST['description']
            )
    return redirect('/')

def edit(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'courses/confirm.html', context)

def destroy(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/')
