# Generated by Django 4.0.3 on 2022-03-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0016_anonypost_image_freepost_image_delete_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
