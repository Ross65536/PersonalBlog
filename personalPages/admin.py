from django.contrib import admin

from .models import *

admin.site.register(Technology)
admin.site.register(Language)
admin.site.register(Project)
admin.site.register(ProjectType)

admin.site.register(PersonLink)
admin.site.register(Person)
admin.site.register(Email)
admin.site.register(Link)