# Generated by Django 3.0.8 on 2020-07-26 19:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='matriculas',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
