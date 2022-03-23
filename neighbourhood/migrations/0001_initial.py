# Generated by Django 4.0.3 on 2022-03-19 17:02

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hood_name', models.CharField(max_length=100)),
                ('hood_location', models.CharField(max_length=100)),
                ('occupants', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
                ('user_location', models.CharField(max_length=200)),
                ('hood_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.neighborhood')),
                ('prof_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_picture', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
                ('post_name', models.CharField(max_length=200)),
                ('post_description', models.TextField()),
                ('date_posted', models.DateField(auto_now=True)),
                ('hood_post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.neighborhood')),
                ('post_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_department', models.CharField(max_length=200)),
                ('police_department', models.CharField(max_length=200)),
                ('hood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=200)),
                ('business_email', models.EmailField(max_length=254)),
                ('business_hood_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.neighborhood')),
                ('business_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]