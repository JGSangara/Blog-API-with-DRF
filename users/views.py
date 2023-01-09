from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse
from .forms import RegistrationForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            email = request.POST.get("email")
            password = request.POST.get("password1")

            user = authenticate(request, email=email, password=password)
            login(request, user)
            return redirect(reverse("/"))
    else:
        form = RegistrationForm()
    args = {"form": form}
    return render(request, "registration/register.html", args)
