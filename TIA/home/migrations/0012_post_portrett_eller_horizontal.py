# Generated by Django 5.0.6 on 2024-06-21 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_post_høyde_alter_post_lengde'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='portrett_eller_horizontal',
            field=models.BooleanField(default=False),
        ),
    ]