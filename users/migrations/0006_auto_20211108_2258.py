# Generated by Django 3.2.9 on 2021-11-08 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_professor_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='accumulated_credits',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='final_grade',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
    ]
