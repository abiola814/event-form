# Generated by Django 5.0.2 on 2024-02-16 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventattendee',
            name='unique_id',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]