from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from . import utils
from .models import Project



def index(request):
    return projects(request)

def resume(request):
    person = utils.get_person()
    context = {
        'person': person,
        'absolute_pdf_url': request.build_absolute_uri(person.resume_pdf.url)
    }
    return render(request, 'personalPages/resume.html', context)

def about(request):
    context = {
        'person': utils.get_person()
    }
    return render(request, 'personalPages/about.html', context)

def projects(request):
    context = {
        'projects': Project.objects.all(),
        'person': utils.get_person()
    }
    return render(request, 'personalPages/projects/projects.html', context)