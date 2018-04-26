from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, ContactForm
from .models import Contact


def home(request):
   return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('dist_name')
            email = form.cleaned_data.get('email')
            about =form.cleaned_data.get('about')
            name = first_name +' '+ last_name

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user_obj = authenticate(username=username, password=raw_password)

            Contact(user=user_obj, name=name, email=email, phone=phone, address=address, comments=about).save()

            login(request, user_obj)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    if request.method == 'GET':
        user = request.user
        user_obj = Contact.objects.filter(user=user)
        print(user_obj)
        return render(request, 'registration/profile.html', {'profile': user_obj})
