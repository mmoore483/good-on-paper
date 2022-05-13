from django.contrib import admin
from .models import CreateNewsletter, SignUpLetter

# Register your models here.
admin.site.register(CreateNewsletter)
admin.site.register(SignUpLetter)
