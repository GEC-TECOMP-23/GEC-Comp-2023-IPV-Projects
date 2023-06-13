from django.http import HttpResponse
from django.shortcuts import render
from .forms import Register
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "index.html",{})


def register_user(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data.get("username"),
                form.cleaned_data.get("email"),
                form.cleaned_data.get("passowrd")
                )
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()
            return HttpResponse("Thanks")
    else:
        form = Register()


    return render(request, "register.html", {"form": form})