from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages, auth

from .models import Account

def signup(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(full_name=full_name, email=email, password=password, username=username)
            messages.success(request,'Signup successfull')
            user.save()
            return redirect("home")
        else:
            messages.error(request, form.errors)
            return redirect("signup")
    context = {
        'f':form,
    }
    return render(request, 'register.html',context)

def login(request):
    if request.method == "POST":
        email = request.POST['Email']
        password = request.POST['password']
        print(email, password)
        user = auth.authenticate(email=email, password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request, "Incorrect username or password!")
            return redirect("login")
    return render(request, 'login.html')
