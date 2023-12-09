# Generated by Django 5.0 on 2023-12-09 03:22

import django_cryptography.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_django', '0015_rename_extra_data_new_usersocialauth_extra_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersocialauth',
            name='extra_data',
            field=django_cryptography.fields.encrypt(models.JSONField(default=dict)),
        ),
    ]
