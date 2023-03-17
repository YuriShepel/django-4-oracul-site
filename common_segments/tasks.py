# from celery import shared_task
# from django.core.mail import send_mail
# from django.conf import settings
#
#
# @shared_task
# def send_feedback_email(name, email, message):
#     send_mail(
#         f'Новый отзыв на сайте от {name} | {email}',
#         message,
#         email,
#         [settings.EMAIL_HOST_USER],
#         fail_silently=False,
#     )
#
