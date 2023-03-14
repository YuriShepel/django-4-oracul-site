"""oracul_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic import TemplateView

from common_segments.views import IndexView, AboutView, ContactsView, PrivacyPolicyView
from common_segments.sitemaps import (
    StaticPagesSitemap,
    ArticleSitemap,
    TarotCardSitemap,
    SuitDescriptionSitemap,
    ColorCharacterSitemap,
    BirthdayDescriptionSitemap,
    MonthDayDescriptionSitemap,
)

sitemaps = {
    'static': StaticPagesSitemap,
    'articles': ArticleSitemap,
    'tarot_cards': TarotCardSitemap,
    'tarot_suits': SuitDescriptionSitemap,
    'color_description': ColorCharacterSitemap,
    'birthday_description': BirthdayDescriptionSitemap,
    'month_day_description': MonthDayDescriptionSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('privacy_policy/', PrivacyPolicyView.as_view(), name='privacy_policy'),

    path('tarot_cards/', include('tarot_cards.urls', namespace='tarot_cards')),
    path('articles/', include('articles.urls', namespace='articles')),
    path('tarot_divinations/', include('tarot_divinations.urls', namespace='tarot_divinations')),
    path('quotes_divination/', include('quotes_divination.urls', namespace='quotes_divination')),
    path('person/', include('person_characteristic.urls', namespace='person_characteristic')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls'))),
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
