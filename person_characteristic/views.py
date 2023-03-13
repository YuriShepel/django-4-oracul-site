import locale
from datetime import datetime

from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from common_segments.common.mixins import TitleMixin

from .forms import BirthdayForm
from .models import ColorCharacter, MonthDayCharacter, WeekDayCharacter


class ColorDescriptionListView(TitleMixin, ListView):
    """Displays the welcome text of the Color characteristic"""
    model = ColorCharacter
    context_object_name = 'colors'
    template_name = 'person_characteristic/color_description_view.html'
    title = 'Описание человека по любимому цвету'

    def get_context_data(self, **kwargs):
        context = super(ColorDescriptionListView, self).get_context_data()
        colors = ColorCharacter.objects.all().order_by('id')
        context['colors'] = colors
        return context


class ColorDescriptionDetailView(DetailView):
    model = ColorCharacter
    context_object_name = 'color'
    template_name = 'person_characteristic/color_description_detail.html'
    slug_field = 'url'


class WeekDayDescriptionView(TitleMixin, TemplateView):
    template_name = 'person_characteristic/week_day_description_view.html'
    title = 'Описание человека по дню рождения'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BirthdayForm()
        context['days'] = WeekDayCharacter.objects.all().order_by('id')
        return context

    def post(self, request, *args, **kwargs):
        form = BirthdayForm(request.POST)
        if form.is_valid():
            birthday = form.cleaned_data['birthday']
            locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
            day_of_week = datetime.strftime(birthday, '%A')
            days = WeekDayCharacter.objects.all().order_by('id')
            return self.render_to_response({'day_of_week': day_of_week, 'days': days, 'form': form})
        else:
            return self.render_to_response({'form': form})


class WeekDayDescriptionDetailView(DetailView):
    model = WeekDayCharacter
    context_object_name = 'day'
    template_name = 'person_characteristic/week_day_description_detail.html'
    slug_field = 'url'


class MonthDayDescriptionListView(TitleMixin, ListView):
    """Displays the welcome text of the Month Day characteristic"""
    model = MonthDayCharacter
    context_object_name = 'day_numbers'
    template_name = 'person_characteristic/month_day_description_view.html'
    title = 'Описание человека по числу дня рождения'

    def get_context_data(self, **kwargs):
        context = super(MonthDayDescriptionListView, self).get_context_data()
        day_numbers = MonthDayCharacter.objects.all().order_by('id')
        context['day_numbers'] = day_numbers
        return context


class MonthDayDescriptionDetailView(DetailView):
    model = MonthDayCharacter
    context_object_name = 'day_number'
    template_name = 'person_characteristic/month_day_description_detail.html'
    slug_field = 'url'
