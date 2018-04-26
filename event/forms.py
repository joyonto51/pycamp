from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'phone',
            'address',
            'comments'
        ]


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    phone = forms.CharField(max_length=30, required=True, help_text='Optional.')
    dist_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    about = forms.CharField(max_length=1000, required=False, help_text='Optional')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'dist_name', 'email', 'about', 'password1','password2')
