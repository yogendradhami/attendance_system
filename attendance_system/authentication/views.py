from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from app_attendance_system.email import EmailBackEnd
from django.contrib.auth.decorators import login_required


# Create your views here.
class LoginView(View):
      def get(self,request):
        return render(request, 'authentication/login.html')
      def post(self,  request):
        return render(request, 'authentication/login.html')

class DoLoginView(View):
    def get(self,request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        if request.method == 'POST':
            user = EmailBackEnd.authenticate(request,
                        username=request.POST.get('email'),
                        password=request.POST.get('password'))
            if user!=None:
                login(request,user)
                user_type = user.user_type
                if user_type =='1':
                    return redirect ("hod")
                
                elif user_type=='2':
                    return redirect ("staff-home")
                
                elif user_type =='3':
                    return redirect("student-home")
                else:
                    messages.success(request, "you're logged In.")
                    return redirect('login')
                
            else:
                messages.error(request, "username and password are invalid.")
                
                return redirect('login')


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
    def get(self, request):
        logout(request)
        messages.success(request, "You're Logged Out !!")
        return redirect('login')