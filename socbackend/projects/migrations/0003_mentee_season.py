# Generated by Django 4.2.6 on 2024-10-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_delete_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentee',
            name='season',
            field=models.TextField(default=''),
        ),
    ]
