# Generated by Django 5.0.6 on 2024-07-09 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_kontakt_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='høyde',
        ),
        migrations.RemoveField(
            model_name='post',
            name='høyde_showcase',
        ),
        migrations.RemoveField(
            model_name='post',
            name='høyde_showcase_auto',
        ),
        migrations.RemoveField(
            model_name='post',
            name='lengde',
        ),
        migrations.RemoveField(
            model_name='post',
            name='lengde_showcase',
        ),
        migrations.RemoveField(
            model_name='post',
            name='lengde_showcase_auto',
        ),
        migrations.RemoveField(
            model_name='post',
            name='portrett_eller_horizontal',
        ),
    ]
