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
from django.urls import include, path

from common_segments.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('tarot_cards/', include('tarot_cards.urls', namespace='tarot_cards')),
    path('articles/', include('articles.urls', namespace='articles')),
    path('tarot_divinations/', include('tarot_divinations.urls', namespace='tarot_divinations')),
    path('quotes_divination/', include('quotes_divination.urls', namespace='quotes_divination')),
    path('person/', include('person.urls', namespace='person')),
    path('ckeditor/', include('ckeditor_uploader.urls')),


]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls'))),
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
