# Generated by Django 2.2.24 on 2021-11-04 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0003_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='profile_hashtag',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tweet',
            name='profile_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tweet',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photo/'),
        ),
    ]