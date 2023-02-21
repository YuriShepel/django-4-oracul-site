from django.views.generic import TemplateView

from common_segments.common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    """Displaying the home page of the site"""
    template_name = 'common_segments/index.html'
    title = 'Гадания онлайн'
