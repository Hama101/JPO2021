# Generated by Django 3.2.9 on 2021-11-01 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profils', '0004_auto_20211101_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fac',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
