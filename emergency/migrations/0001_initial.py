# Generated by Django 5.1.1 on 2024-11-12 07:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emergency_type', models.CharField(choices=[('D', 'Danger Alert'), ('O', 'Offer Help'), ('M', 'Medical Help')], default='O', max_length=1)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='emergency/images')),
                ('emergency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='emergency.emergency')),
            ],
        ),
    ]