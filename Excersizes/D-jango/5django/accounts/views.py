# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView): 
# We are subclassing the generic class-based view  "CreateView" in our 
# SignUpView Class
    form_class = UserCreationForm
    success_url = reverse_lazy('login') # Upon Successful Registration
    template_name = 'signup.html' # The view will populate data for this template