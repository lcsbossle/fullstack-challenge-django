# Generated by Django 3.1.2 on 2020-10-04 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memberarea', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aula',
            options={'ordering': ['titulo'], 'verbose_name_plural': 'Aulas'},
        ),
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ['titulo'], 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AlterUniqueTogether(
            name='sequencia',
            unique_together={('curso', 'aula')},
        ),
    ]