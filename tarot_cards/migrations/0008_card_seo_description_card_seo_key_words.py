# Generated by Django 4.1.6 on 2023-02-17 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarot_cards', '0007_tarotsuits_alternative_names_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='seo_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='seo_key_words',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
