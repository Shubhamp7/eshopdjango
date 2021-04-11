from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


def sendemail(request):
    subject="purchase confirmation"
    message="Thank you for purchasing"
    emailfrom=settings.EMAIL_HOST_USER
    recipent=['dishantrathi1@gmail.com',]
    send_mail(subject,message,emailfrom,recipent)
    return HttpResponse('Email sent')

