from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from . import values
from .models import Project



def index(request):
    return projects(request)

def resume(request):
    context = {
        'resume_pdf_url': values.RESUME_PDF_URL,
        'person': values.get_person()
    }
    return render(request, 'personalPages/resume.html', context)

def about(request):
    context = {
        'person': values.get_person()
    }
    return render(request, 'personalPages/about.html', context)

def projects(request):
    context = {
        'projects': Project.objects.all(),
        'person': values.get_person()
    }
    return render(request, 'personalPages/projects/projects.html', context)