from django import forms
from .models import CreateNewsletter, SignUpLetter


class CreateNewsletterForm(forms.ModelForm):

    class Meta:
        model = CreateNewsletter
        fields = ('subject', 'message', 'image')


class SignUpLetterForm(forms.ModelForm):

    class Meta:
        model = SignUpLetter
        fields = ('email', 'name', 'signed_up')
