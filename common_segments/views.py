from django.views.generic import TemplateView

from common_segments.common.mixins import TitleMixin


class IndexView(TitleMixin, TemplateView):
    """Displaying the home page of the site"""
    template_name = 'common_segments/index.html'
    title = 'Гадания онлайн'


class AboutView(TitleMixin, TemplateView):
    """Displaying the about page of the site"""
    template_name = 'common_segments/about.html'
    title = 'О сайте'
