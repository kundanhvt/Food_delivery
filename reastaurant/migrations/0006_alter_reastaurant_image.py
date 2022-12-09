# Generated by Django 4.1.3 on 2022-12-08 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reastaurant', '0005_remove_image_path_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reastaurant',
            name='image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reastaurant_image_name', to='reastaurant.image'),
        ),
    ]
