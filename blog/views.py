from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# HOME PAGE
def home_page(request):

    if not request.user.is_authenticated:
        return redirect('/login/')

    return render(request, 'home.html')


# REGISTER PAGE
def register_page(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('/login/')

    return render(request, 'register.html')


# LOGIN PAGE
def login_page(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')


# LOGOUT
def logout_page(request):

    logout(request)
    return redirect('/login/')