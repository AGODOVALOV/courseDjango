from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from django.shortcuts import render, get_object_or_404
from django.http import Http404


def index(request):
    courses = Course.objects.all()

    return render(request, "shop/courses.html", {"courses": courses})
    # return HttpResponse(content="Hello from the shop app")
    # return HttpResponse([f"{course.title} <br>" for course in courses])


def single_course(request, course_id):
    # Option1
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(request, "single_course.html", {"course": course})
    # except Course.DoesNotExist:
    #     raise Http404()

    # # Option 2
    course = get_object_or_404(Course, pk=course_id)
    return render(request, "shop/single_course.html", {"course": course})
