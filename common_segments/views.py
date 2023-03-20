from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.generic import TemplateView

from common_segments.tasks import send_feedback_email
from common_segments.common.mixins import TitleMixin
from common_segments.forms import FeedbackForm
from common_segments.models import Feedback


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FeedbackForm()
        return context

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            feedback = Feedback(name=name, email=email, message=message)
            feedback.save()
            send_feedback_email.delay(name, email, message)
            return redirect('message_success')  # перенаправление на главную страницу
        else:
            context = self.get_context_data(form=form)
            return self.render_to_response(context)


class MessageSuccessView(TitleMixin, TemplateView):
    """Displaying the about page of the site"""
    template_name = 'common_segments/message_success.html'
    title = 'Сообщение отправлено'


class PrivacyPolicyView(TitleMixin, TemplateView):
    """Displaying the privacy policy page of the site"""
    template_name = 'common_segments/privacy_policy.html'
    title = 'Политика конфиденциальности'
