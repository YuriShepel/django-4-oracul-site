# Generated by Django 4.1.7 on 2023-02-27 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarot_cards', '0011_alter_card_image_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='yes_no',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]