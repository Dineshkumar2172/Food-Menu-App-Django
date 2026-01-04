from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from users.forms import RegisterForm

# Create your views here.
def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Welcome {username}, your account has been successfully created")
            return redirect("login")

    form = RegisterForm()
    return render(request, "users/register.html", context={'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required
def profile_view(request):
    return render(request, 'users/profile.html')
