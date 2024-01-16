# Generated by Django 5.0.1 on 2024-01-16 00:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0020_remove_experience_time_frame_experience_end_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='company',
        ),
        migrations.AddField(
            model_name='experience',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hired_companies', to='resume.company'),
        ),
    ]