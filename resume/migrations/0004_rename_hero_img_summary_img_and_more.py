# Generated by Django 4.2.6 on 2023-10-29 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_fontfamily_pagestyle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='summary',
            old_name='hero_img',
            new_name='img',
        ),
        migrations.RemoveField(
            model_name='summary',
            name='profile_img',
        ),
    ]