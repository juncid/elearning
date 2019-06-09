from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#def my_first_view(request):
#    return HttpResponse('Hola, Mundo!')


def my_first_view(request, who):
    return render(request, 'courses/hello.html', {
        'who': who,
    })
