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


class ContactsView(TitleMixin, TemplateView):
    """Displaying the contacts page of the site"""
    template_name = 'common_segments/contacts.html'
    title = 'Контакты сайта'


class PrivacyPolicyView(TitleMixin, TemplateView):
    """Displaying the privacy policy page of the site"""
    template_name = 'common_segments/privacy_policy.html'
    title = 'Политика конфиденциальности'
