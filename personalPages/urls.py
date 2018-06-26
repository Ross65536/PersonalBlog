from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume', views.resume, name='resume'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)