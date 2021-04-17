from django.shortcuts import render
from email_sender.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail

# Create your views here.

def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome To ChillSoup'
        message = 'Hope you are engjoying your stay :))'
        recepient = str(sub['Email'].value())
        send_mail(subject,
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form':sub})
