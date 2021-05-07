from django.shortcuts import render, redirect
from .models import ContactDetails
from .forms import ContactForm
from django.core.mail import BadHeaderError
from django.core.mail import send_mail as sm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def send_mail(request):

    contact_details = ContactDetails.objects.last()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            form_email = contact_form.cleaned_data['form_email'] 
            message = contact_form.cleaned_data['message']

        try:
            sm(subject, message, form_email, ['test@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid Header')
        
        return redirect('contact:success')
    else:
        contact_form = ContactForm

    template = 'contact.html'
    context = {
        'contact_details' : contact_details,
        'contact_form' : contact_form,
    }

    return render(request, template, context)
 
def success(request):
    return HttpResponse('Message Sent Successfully')