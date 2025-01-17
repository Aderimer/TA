# Generated by Django 5.0.6 on 2024-06-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_post_høyde_showcase_post_lengde_showcase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navn', models.CharField(max_length=100)),
                ('tlf', models.CharField(blank=True, default='', max_length=12, null=True)),
                ('bilde', models.ImageField(upload_to='uploads/profil/')),
                ('kamera_navn', models.CharField(blank=True, default='Canon EOS 5D Mark II', max_length=100, null=True)),
                ('kamera_detaljer', models.CharField(blank=True, default='', max_length=1000, null=True)),
            ],
        ),
    ]
