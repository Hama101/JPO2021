# Generated by Django 3.2.9 on 2021-11-01 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profils', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='verfied',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
