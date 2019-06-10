from django.shortcuts import render
from django.http import HttpResponse

from courses.models import Course

# Create your views here.
#def my_first_view(request):
#    return HttpResponse('Hola, Mundo!')


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'courses/course_detail.html', {
        'course': course,
    })
