# Generated by Django 4.1.5 on 2023-05-23 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='check_out',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
