

# Create your views here.
# views.py
# ValueError
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

def send_email_view(request):
    subject = 'Test Email'
    message = 'This is a test email sent from Django.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['uggamnagaraju02@gmail.com']

    send_mail(subject, message, from_email, recipient_list)

    return HttpResponse('Email sent successfully!')
