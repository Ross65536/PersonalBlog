# Generated by Django 2.0.1 on 2018-06-25 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalPages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='links',
        ),
        migrations.AddField(
            model_name='project',
            name='links',
            field=models.ManyToManyField(to='personalPages.Link'),
        ),
    ]