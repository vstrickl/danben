# Generated by Django 5.0.1 on 2024-01-15 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0017_remove_summary_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
