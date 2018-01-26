from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return resume(request)

def resume(request):
    context = {
        'fullname': 'Rostyslav'
    }
    return render(request, 'personalPages/resume.html', context)