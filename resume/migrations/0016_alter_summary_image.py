# Generated by Django 5.0.1 on 2024-01-15 19:04

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0015_remove_pagestyle_font_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
