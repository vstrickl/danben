# Generated by Django 5.0.1 on 2024-01-16 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0019_rename_name_summary_first_name_summary_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='time_frame',
        ),
        migrations.AddField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='present',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
