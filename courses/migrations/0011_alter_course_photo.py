# Generated by Django 3.2.9 on 2021-12-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_alter_course_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/courses/%Y/'),
        ),
    ]
