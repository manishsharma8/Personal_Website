from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.


def HomePage(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        from_email = form.cleaned_data['email']
        message = form.cleaned_data['text'] + '\n' + form.cleaned_data['name']+ '\n' + form.cleaned_data['email']
        send_mail(subject, message, from_email, ['E19CSE053@bennett.edu.in'], fail_silently=False)

    context = {
        'form' : form
    }

    return render(request, 'index.html', context)