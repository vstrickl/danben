# Generated by Django 4.2.6 on 2023-10-29 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_skill_remove_summary_intro_skillgroup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skillgroup',
            old_name='skill',
            new_name='skills',
        ),
    ]
