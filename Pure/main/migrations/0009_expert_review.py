# Generated by Django 4.0.5 on 2022-08-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_order_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='team_image')),
                ('name', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='review_image')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
        ),
    ]
