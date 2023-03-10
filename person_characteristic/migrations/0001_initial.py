# Generated by Django 4.1.7 on 2023-03-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColorCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('color_code', models.CharField(max_length=20, unique=True)),
                ('text', models.TextField()),
                ('url', models.SlugField(max_length=100, unique=True)),
                ('seo_description', models.TextField(blank=True, null=True)),
                ('seo_keywords', models.CharField(blank=True, max_length=300, null=True)),
                ('moderation', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
    ]
