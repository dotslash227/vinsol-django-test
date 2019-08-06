from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from .models import Deal
from django.contrib.auth.decorators import login_required
from django.contrib import messages

class AuthPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("products:deal")
        else:
            return render(request, "login.html", {})

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        print (username, password)
        errors = []
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("products:deal")
            else:
                errors.append("User not active")
                return render(request, "login.html", {"errors":errors})
        else:
            errors.append("User does not exist")
            return render(request, "login.html", {"errors":errors})

def logoutView(request):
    logout(request)
    return redirect("products:login")

@login_required
def dealPage(request):
    try: 
        deal = Deal.objects.filter(is_published=True, published_date=timezone.now).order_by("-pk")[0]
    except:
        messages.add_message(request, messages.INFO, "No deals published today")
        deal = None

    return render(request, "index.html", {
        "deal": deal
    })