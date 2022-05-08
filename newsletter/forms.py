from django import forms
from .models import CreateNewsletter


class CreateNewsletterForm(forms.ModelForm):

    class Meta:
        model = CreateNewsletter
        fields = ('subject', 'message', 'image')

