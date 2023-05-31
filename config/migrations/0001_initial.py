# Generated by Django 4.2.1 on 2023-05-22 17:54

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
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FastFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.IntegerField(blank=True, max_length=200, null=True)),
                ('ingredient', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='fast-food')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(blank=True, max_length=250, null=True)),
                ('food_price', models.IntegerField(blank=True, max_length=200, null=True)),
                ('food_ingredient', models.TextField(blank=True, null=True)),
                ('food_image', models.ImageField(blank=True, null=True, upload_to='fast-food')),
                ('prep_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('password', models.IntegerField(blank=True, max_length=150, null=True)),
                ('confirm_password', models.IntegerField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('table', models.CharField(blank=True, max_length=120, null=True)),
                ('food', models.ManyToManyField(blank=True, null=True, to='config.food')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
