from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import ColorCharacter

from common_segments.common.mixins import TitleMixin


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
