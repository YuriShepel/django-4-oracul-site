# Generated by Django 4.1.7 on 2023-02-22 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarot_cards', '0010_alter_tarotsuits_image_4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image_1',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='tarot_cards/cards_images'),
        ),
    ]
