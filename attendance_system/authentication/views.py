from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login,logout

# Create your views here.
class LoginView(View):
    def get(self,request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        return render(request, 'authentication/login.html')

class RegisterView(View):
    def get(self,request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        return render(request, 'authentication/Register.html')
    
class LogoutView(View):
    def get(self,request):
        pass

    def post(self, request):
        pass