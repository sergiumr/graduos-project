# Generated by Django 3.2.9 on 2022-01-01 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/users/%Y/'),
        ),
    ]
