# Generated by Django 4.2.9 on 2024-02-17 11:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_post_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Username',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('login_data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
