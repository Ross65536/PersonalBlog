# Generated by Django 2.0.1 on 2018-06-25 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalPages', '0005_auto_20180625_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='languages',
            field=models.ManyToManyField(blank=True, to='personalPages.Language'),
        ),
        migrations.AlterField(
            model_name='project',
            name='links',
            field=models.ManyToManyField(blank=True, to='personalPages.Link'),
        ),
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(blank=True, to='personalPages.Technology'),
        ),
    ]
