# Generated by Django 4.1.3 on 2022-12-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_users_address_delete_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]