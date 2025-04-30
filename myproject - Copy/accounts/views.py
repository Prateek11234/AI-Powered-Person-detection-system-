from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .models import Enrollment
from django.contrib import messages


# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


# Dashboard view
@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html', {'username': request.user.username})


# Logout view
def logout_view(request):
    logout(request)
    return redirect('accounts:login')


# Registration view
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('accounts:enrollment_data')
        else:
            print(form.errors)  # Debug: Print form errors to the terminal
    else:
        form = RegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})


# Enrollment data view
def enrollment_data(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'accounts/enrollment_data.html', {'enrollments': enrollments})


# Add Face view
def add_face(request):
    return render(request, 'accounts/add_face.html')