# Generated by Django 3.0.5 on 2020-08-15 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20200815_0547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.AddField(
            model_name='project',
            name='long_description',
            field=models.TextField(null=True, verbose_name='Descripción larga'),
        ),
        migrations.AddField(
            model_name='project',
            name='short_description',
            field=models.TextField(null=True, verbose_name='Descripción corta'),
        ),
    ]
