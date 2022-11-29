# Generated by Django 4.1.3 on 2022-11-29 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DestCommonInfo',
        ),
        migrations.AddField(
            model_name='destination',
            name='country',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='place',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='time',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
