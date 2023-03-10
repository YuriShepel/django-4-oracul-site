# Generated by Django 4.1.7 on 2023-03-09 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person_characteristic', '0002_weekdaycharacter'),
    ]

    operations = [
        migrations.AddField(
            model_name='weekdaycharacter',
            name='color_code',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='colorcharacter',
            name='color_code',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
