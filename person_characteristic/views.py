from django.shortcuts import render
from django.views.generic import TemplateView

from common_segments.common.mixins import TitleMixin


# Create your views here.
class ColorDescriptionView(TitleMixin, TemplateView):
    """Displays the welcome text of the Finance Situation divination"""
    template_name = 'person_characteristic/color_description_view.html'
    title = 'Описание человека по любимому цвету'
