# Generated by Django 5.2.3 on 2025-06-21 10:42

import core_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(upload_to='images/uploads/banner/')),
                ('alt_text', models.CharField(blank=True, max_length=200)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Banner Image',
                'verbose_name_plural': 'Banner Images',
                'ordering': ['order', 'created_at'],
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(upload_to='images/uploads/gallery/')),
                ('alt_text', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Gallery Image',
                'verbose_name_plural': 'Gallery Images',
                'ordering': ['order', 'created_at'],
            },
        ),
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(upload_to=core_app.models.get_upload_path)),
                ('image_type', models.CharField(choices=[('banner', 'Banner'), ('portfolio', 'Portfolio'), ('gallery', 'Gallery'), ('logo', 'Logo'), ('other', 'Other')], default='other', max_length=20)),
                ('alt_text', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Image Upload',
                'verbose_name_plural': 'Image Uploads',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(upload_to='images/uploads/portfolio/')),
                ('alt_text', models.CharField(blank=True, max_length=200)),
                ('category', models.CharField(choices=[('wedding', 'Wedding'), ('engagement', 'Engagement'), ('portrait', 'Portrait'), ('ceremony', 'Ceremony'), ('reception', 'Reception'), ('details', 'Details')], default='wedding', max_length=20)),
                ('description', models.TextField(blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Portfolio Image',
                'verbose_name_plural': 'Portfolio Images',
                'ordering': ['order', 'created_at'],
            },
        ),
    ]
