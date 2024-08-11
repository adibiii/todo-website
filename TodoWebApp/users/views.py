from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# from django.urls import reverse
from django.views import View

# Create your views here.
from .forms import CustomUserCreationForm
from .models import CustomUser


class Login(LoginView):
    template_name = 'users/login.html'
    next_page = 'todohome'


class Register(View):

    def get(self, *args, **kwargs):
        form = CustomUserCreationForm
        return render(self.request, 'users/signin.html', {"form": form})

    def post(self, *args, **kwargs):
        form = CustomUserCreationForm(self.request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(self.request, email=email, password=password)
            login(self.request, user)
            return redirect('userhome')
        return render(self.request, 'users/signin.html', {"form": form})


def home(request):
    print(request.user.id)
    users = CustomUser.objects.all()
    return render(request, 'users/home.html', {'users': users})


def logout_view(request):
    logout(request)
    return redirect('userhome')

