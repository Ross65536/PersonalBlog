# Generated by Django 2.0.1 on 2018-06-26 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalPages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
