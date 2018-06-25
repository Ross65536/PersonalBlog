from django.db import models

class TypeName(models.Model):
    type_name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.type_name

class Technology(TypeName):
    pass

class Language(TypeName):
    pass


class Link(models.Model):
    name = models.CharField(max_length=256)
    link = models.URLField()

    def __str__(self):
        return self.name

    def get_fontawesome(self):
        return "<i class=\"fas fa-envelope\"></i>"

class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    technologies = models.ManyToManyField(Technology, blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    links = models.ManyToManyField(Link, blank=True)

    def __str__(self):
        return self.title
