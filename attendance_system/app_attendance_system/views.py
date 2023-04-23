from django.shortcuts import render,redirect
from app_attendance_system.models import CustomUser
from django.contrib import messages

# Create your views here.
def Index(request):

    return render(request, 'layouts/master.html')

def Profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    context ={
        "user":user,
    }
    return render(request, 'profile/users-profile.html',context)

def UpdateProfile(request):
    if request.method=='POST':
        first_name= request.POST.get('first_name')
        last_name=request.POST.get("last_name")
        # email=request.POST.get('email')
        # username=request.POST.get('username')
        password=request.POST.get('password')
        profile_pic=request.FILES.get('profile_pic')
        # print(profile_pic)
        try:
            CustomUser= CustomUser.objects.get(id= request.user.id)
            CustomUser.first_name=first_name
            CustomUser.last_name=last_name

            if password != None and password != "":
                CustomUser.password=password(password)

            CustomUser.profile_pic=profile_pic
            CustomUser.save()
            messages.error(request, "Sorry, Failed To Update You're Profile.")
            return redirect('profile')
        except:
            messages.error(request, "You're Profile Updated Successfully.")
    return render(request, 'profile/users-profile.html')

def Dashboard(request):

    return render(request, 'components/dashboard.html')

# hod views
def Hod(request):
    return render(request, 'hod/hod.html')

# staff views
def staff(request):
    pass

# student view
def student(request):
    pass