# Generated by Django 4.2.6 on 2023-10-30 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0014_pagestyle_template_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagestyle',
            name='font_size',
        ),
        migrations.RemoveField(
            model_name='pagestyle',
            name='font_weight',
        ),
    ]
