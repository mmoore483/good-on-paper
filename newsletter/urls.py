from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_newsletter, name='create_newsletter'),
    path('mailinglist/', views.signup_newsletter, name='letter_signup'),
]
