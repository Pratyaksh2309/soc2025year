# Generated by Django 4.2.6 on 2025-01-02 11:01

from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.TextField(default='')),
                ('user', models.OneToOneField(help_text='The user corresponding to the mentee.', on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('general_category', models.CharField(choices=[('ML', 'ML'), ('Developement', 'Development'), ('Blockchain', 'Blockchain'), ('CP', 'CP'), ('Others', 'Others')], default='Others', max_length=255)),
                ('specific_category', models.CharField(default='NA', max_length=255)),
                ('mentee_max', models.CharField(max_length=255)),
                ('mentor', models.CharField(default='NA', max_length=255)),
                ('description', models.TextField(default='NA')),
                ('timeline', models.TextField(default='NA')),
                ('checkpoints', models.TextField(default='NA')),
                ('prereuisites', models.TextField(default='NA')),
                ('co_mentor_info', models.TextField(default='NA')),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to=projects.models.upload_to)),
                ('banner_image_link', models.URLField(blank=True, null=True)),
                ('code', models.CharField(editable=False, max_length=8, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.TextField(default='')),
                ('user', models.OneToOneField(help_text='The user corresponding to the mentor.', on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='MenteeWishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.mentee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'unique_together': {('mentee', 'project')},
            },
        ),
        migrations.CreateModel(
            name='MenteePreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sop', models.TextField()),
                ('preference', models.IntegerField()),
                ('mentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.mentee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'unique_together': {('mentee', 'project', 'preference'), ('mentee', 'project')},
            },
        ),
    ]
