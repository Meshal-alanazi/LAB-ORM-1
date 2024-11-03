# Generated by Django 5.1.2 on 2024-11-03 18:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=2048)),
                ('contant', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
                ('published_at', models.DateTimeField(verbose_name=django.utils.timezone.now)),
            ],
        ),
    ]
