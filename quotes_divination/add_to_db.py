import csv
import os
import sys

# Добавляем путь к корневой папке вашего проекта Django
sys.path.append('D:\Django_projects\oracul-project\site-server\oracul_site\oracul_site')

# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oracul_site.settings')

# Импортируем Django и настраиваем его
import django

django.setup()

# Импортируем модель Quote
from quotes_divination.models import Category, Quote

with open('categorized_love_quotes.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        # Ищем категорию с указанным именем
        category_name = row[0]
        try:
            category = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            print(f"Category '{category_name}' does not exist")
            continue

        # Создаем новый объект Quote для каждой строки CSV
        author = row[1]
        quote = row[2]
        new_quote = Quote(category=category, author=author, quote=quote)
        new_quote.save()
