# Generated by Django 5.0.6 on 2024-06-19 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=5)),
                ('nombre', models.TextField()),
                ('duracion', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='fotos', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
