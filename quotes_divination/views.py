import random

from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from common_segments.common.mixins import TitleMixin

from .models import Category, Quote


class CategoryListView(TitleMixin, ListView):
    model = Category
    title = 'Гадание по цитатам'
    template_name = 'quotes_divination/category_quotes_list.html'
    context_object_name = 'categories'


class RandomQuoteView(View):
    title = 'Гадание по цитатам'

    def get(self, request, slug):
        category = Category.objects.get(url=slug)
        quotes = Quote.objects.filter(category=category)
        random_quote = random.choice(quotes)
        context = {
            'quote': random_quote.quote,
            'autor': random_quote.author,
            'image': random_quote.category.image,
            'title': 'Гадание по цитатам',
        }
        return render(request, 'quotes_divination/random_quote_view.html', context=context)
