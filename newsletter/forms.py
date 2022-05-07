from django import forms
from .models import CreateNewsletter


class CreateNewsletterForm(forms.ModelForm):

    class Meta:
        model = CreateNewsletter
        fields = ('subject', 'message', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
