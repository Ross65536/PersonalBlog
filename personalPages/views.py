from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from . import values
from .models import Article

def index(request):
    return resume(request)

def resume(request):
    context = {
        'resume_pdf_url': values.RESUME_PDF_URL,
        'resume_image_url': values.RESUME_IMAGE_URL,
    }
    context.update(values.BASIC_INFO)
    return render(request, 'personalPages/resume.html', context)

def about(request):
    context = {
        'admin_email': values.ADMINISTRATOR_EMAIL,
    }
    context.update(values.BASIC_INFO)
    return render(request, 'personalPages/about.html', context)

class BlogIndexView(generic.ListView):
    template_name = 'personalPages/blog_index.html'
    context_object_name = 'article_list'
    
    def get_queryset(self):
        return Article.objects.all().order_by('-publish_date')

    def get_context_data(self,**kwargs):
        context = super(BlogIndexView, self).get_context_data(**kwargs)
        context.update(values.BASIC_INFO)
        return context
