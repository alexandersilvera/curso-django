# Generated by Django 3.0.8 on 2020-08-01 14:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clases', '0002_creacion_matricula'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matricula',
            options={'ordering': ['clase', 'data']},
        ),
        migrations.AlterUniqueTogether(
            name='matricula',
            unique_together={('usuario', 'clase')},
        ),
    ]
