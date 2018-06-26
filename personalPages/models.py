from django.db import models

class TypeName(models.Model):
    type_name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.type_name

class Technology(TypeName):
    pass

class Language(TypeName):
    pass

class ProjectType(TypeName):
    pass

class Link(models.Model):
    name = models.CharField(max_length=256)
    link = models.URLField()
    description = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name + " (" + self.description + ") [ " + self.link + " ]"


class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    technologies = models.ManyToManyField(Technology, blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    types = models.ManyToManyField(ProjectType, blank=True)
    links = models.ManyToManyField(Link, blank=True)

    def __str__(self):
        return self.title

# user & pages

class PersonLink(Link):
    pass

class Email(models.Model):
    name = models.CharField(max_length=256)
    link = models.CharField(max_length=256)

    def __str__(self):
        return self.name + " (" + self.link + ")"

class Person(models.Model):
    username = models.CharField(max_length=256, unique=True)
    fullname = models.CharField(max_length=256)
    profession = models.CharField(max_length=256)
    email = models.ForeignKey(Email, on_delete=models.SET_NULL, null=True)
    footer_links = models.ManyToManyField(PersonLink, blank=True)
    resume_pdf = models.FileField(upload_to='resume', null=True)

    project_page = models.TextField(blank=True)
    resume_page = models.TextField(blank=True)
    about_page = models.TextField(blank=True)

    def __str__(self):
        return self.username + " (" + self.fullname + ")"
