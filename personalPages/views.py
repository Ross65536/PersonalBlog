from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from . import values
from .models import Project

def index(request):
    return resume(request)

def resume(request):
    context = {
        'resume_pdf_url': values.RESUME_PDF_URL,
    }
    context.update(values.BASIC_INFO)
    return render(request, 'personalPages/resume.html', context)

def about(request):
    context = {
        'admin_email': values.ADMINISTRATOR_EMAIL,
    }
    context.update(values.BASIC_INFO)
    return render(request, 'personalPages/about.html', context)

def projects(request):
    context = {
        'projects': Project.objects.all()
    }
    context.update(values.BASIC_INFO)
    return render(request, 'personalPages/projects.html', context)