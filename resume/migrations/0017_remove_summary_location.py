# Generated by Django 5.0.1 on 2024-01-15 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0016_alter_summary_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summary',
            name='location',
        ),
    ]
