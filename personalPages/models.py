from django.db import models

class TypeName(models.Model):
    type_name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.type_name

class Link(models.Model):
    name = models.CharField(max_length=256)
    link = models.URLField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    technologies = models.ManyToManyField(TypeName)
    links = models.ManyToManyField(Link)

    def __str__(self):
        return self.title
