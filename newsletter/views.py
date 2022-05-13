from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

from .models import CreateNewsletter, SignUpLetter
from .forms import CreateNewsletterForm, SignUpLetterForm


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
            email_message = f'{message} <br> {image}'
            send_mail(
                subject,
                email_message,
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


def signup_newsletter(request):
    """ sign up/unsubscribe to the mailing list """
    if request.method == 'POST':
        signup_form = SignUpLetterForm(request.POST, request.FILES)
        if signup_form.is_valid():
            email = signup_form.cleaned_data['email']
            name = signup_form.cleaned_data['name']
            signbool = signup_form.cleaned_data['signed_up']
            signup_form.save()
            if signbool is True:
                messages.success(request, 'Successfully signed up!')
                email_message = (
                    f"Hi {name}."
                    f"Thank you for signing up to the Good On Paper Newsletter!"
                    f"We'll keep you update with all the latest offers and books!"
                )
                send_mail(
                    "Good On Paper Newsletter",
                    email_message,
                    settings.EMAIL_HOST_USER,
                    email,
                    fail_silently=False,
                )
            else:
                messages.success(request, 'Successfully removed from the mailing list')
        else:
            messages.error(request,
                           ('Failed to sign up to the newsletter '
                            'Please ensure the form is valid.'))

        return redirect("letter_signup.html")

    signup_form = SignUpLetterForm()
    signup = SignUpLetter.objects.all()
    template = 'newsletter/letter_signup.html'
    context = {
        'signup_form': signup_form,
        'signup': signup
    }

    return render(request, template, context)
