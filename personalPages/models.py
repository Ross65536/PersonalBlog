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


# delete file after update 
# modified from https://stackoverflow.com/a/38265603
from django.db.models.signals import post_init, post_save, post_delete
from django.dispatch import receiver

@receiver(post_init, sender= Person)
def backup_path(sender, instance, **kwargs):
    instance._current_resume_pdf_file = instance.resume_pdf

def _delete_file(instance):
    if hasattr(instance, '_current_resume_pdf_file'):
        if instance._current_resume_pdf_file != instance.resume_pdf.path:
            instance._current_resume_pdf_file.delete(save=False)

@receiver(post_save, sender = Person)
def delete_old_file_on_save(sender, instance, **kwargs):
    _delete_file(instance)

@receiver(post_delete, sender = Person)
def delete_old_file_on_delete(sender, instance, **kwargs):
    _delete_file(instance)

        
