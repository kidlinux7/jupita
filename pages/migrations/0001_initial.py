# Generated by Django 3.1.1 on 2021-01-08 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200, null=True)),
                ('subheading', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('website_link', models.CharField(max_length=200, null=True)),
                ('blog_pictures', models.ImageField(upload_to='blog/')),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('playstore_link', models.CharField(max_length=200, null=True)),
                ('appstore_link', models.CharField(max_length=200, null=True)),
                ('website_link', models.CharField(max_length=200, null=True)),
                ('product_pictures', models.ImageField(upload_to='products/')),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
