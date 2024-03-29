# Generated by Django 4.2.6 on 2023-10-29 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='FontFamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(blank=True, max_length=200, null=True)),
                ('serif_type', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_name', models.CharField(blank=True, max_length=200, null=True)),
                ('header_font_size', models.CharField(blank=True, max_length=200, null=True)),
                ('header_font_weight', models.CharField(blank=True, max_length=200, null=True)),
                ('font_size', models.CharField(blank=True, max_length=200, null=True)),
                ('font_weight', models.CharField(blank=True, max_length=200, null=True)),
                ('font', models.ManyToManyField(blank=True, related_name='general', to='resume.fontfamily')),
                ('header_font', models.ManyToManyField(blank=True, related_name='headers', to='resume.fontfamily')),
            ],
        ),
    ]
