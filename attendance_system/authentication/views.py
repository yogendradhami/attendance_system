from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login,logout
from django.contrib import messages


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
        name=request.POST.get('name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        check=request.POST.get('terms')

        try:
            user= User.objects.get(username=username, email=email)
            if user:
                messages.error(request, "Username already exists. Try with new one!")
                return redirect('register')
        except:
            data =User.objects.create_user(name=name, email=email, username=username, password=password,check=check)
            data.save()

            messages.success(request, "Account created successfully!")
            return redirect('login')


class LogoutView(View):
    def get(self,request):
        pass

    def post(self, request):
        pass