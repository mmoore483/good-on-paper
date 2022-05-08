from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

from .models import CreateNewsletter
from .forms import CreateNewsletterForm


@login_required
def create_newsletter(request):
    """ Create a newsletter to send to the mail list """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        letter_form = CreateNewsletterForm(request.POST, request.FILES)
        if letter_form.is_valid():
            subject = letter_form.cleaned_data['subject']
            message = letter_form.cleaned_data['message']
            image = letter_form.cleaned_data['image']
            letter_form.save()
            messages.success(request, 'Successfully created newsletter!')
            recipients = User.objects.values_list('email', flat=True)
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                recipients,
                fail_silently=False,
            )
        else:
            messages.error(request,
                           ('Failed to create newsletter. '
                            'Please ensure the form is valid.'))
 
        return redirect("create_newsletter")
    
    letter_form = CreateNewsletterForm()
    letters = CreateNewsletter.objects.all()
    template = 'newsletter/create_letter.html'
    context = {
        'letter_form': letter_form,
        'letters': letters
    }

    return render(request, template, context)
