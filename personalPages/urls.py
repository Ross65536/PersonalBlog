from django.urls import path

from . import views

#app_name = 'personalPages'
urlpatterns = [
    path('', views.resume, name='index'),
    path('resume', views.resume, name='resume'),
    path('about', views.about, name='about'),
    path('blog', views.BlogIndexView.as_view(), name='blog_index'),
    path('blog-post/<int:pk>', views.BlogPostView.as_view(), name='blogpost'),
]