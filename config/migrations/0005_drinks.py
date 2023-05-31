# Generated by Django 4.2.1 on 2023-05-22 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_delete_fastfood'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drinks_name', models.CharField(blank=True, max_length=250, null=True)),
                ('drinks_price', models.IntegerField(blank=True, max_length=200, null=True)),
                ('drinks_ingredient', models.TextField(blank=True, null=True)),
                ('drinks_image', models.ImageField(blank=True, null=True, upload_to='soft-drinks')),
                ('drinks_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
