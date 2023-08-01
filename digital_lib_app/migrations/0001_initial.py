# Generated by Django 3.2.15 on 2023-07-30 13:21

import digital_lib_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='')),
                ('pdf_file', models.FileField(upload_to=digital_lib_app.models.pdf_upload_path)),
                ('author', models.CharField(default='Guest', max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('description', models.TextField(default='Available in Library')),
            ],
        ),
    ]
