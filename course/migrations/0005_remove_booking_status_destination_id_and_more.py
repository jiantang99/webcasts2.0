# Generated by Django 4.1.3 on 2022-12-14 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0004_booking_user_rename_place_destination_place_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking_status',
            name='destination_id',
        ),
        migrations.AddField(
            model_name='destination',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/'),
        ),
        migrations.AddField(
            model_name='destination',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationality', models.CharField(blank=True, max_length=250, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=250, null=True)),
                ('wishlist', models.CharField(blank=True, max_length=250, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'UserProfiles',
                'db_table': 'user_profile',
            },
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.userprofile'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
