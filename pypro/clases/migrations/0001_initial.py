<<<<<<< HEAD
# Generated by Django 3.0.8 on 2020-07-27 01:55

from django.conf import settings
=======
# Generated by Django 3.0.8 on 2020-07-26 19:50

>>>>>>> 37f9113f5b4019ee76cba69763aab8d0c83c302b
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
>>>>>>> 37f9113f5b4019ee76cba69763aab8d0c83c302b
    ]

    operations = [
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
<<<<<<< HEAD
                ('slug', models.SlugField(max_length=64)),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
                ('matriculas', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
=======
                ('slug', models.CharField(max_length=64)),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
>>>>>>> 37f9113f5b4019ee76cba69763aab8d0c83c302b
            ],
        ),
    ]