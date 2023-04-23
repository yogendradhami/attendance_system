from django.shortcuts import render,redirect
from app_attendance_system.models import CustomUser,Cource,Student,Session_Year
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
            if profile_pic != None and profile_pic != "":
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

def HodAddStudent(request):
    cource = Cource.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        last_name=request.POST.get("last_name")
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        cource_id=request.POST.get('cource_id')
        session_year_id=request.POST.get('session_year_id')
        profile_pic=request.FILES.get('profile_pic')
        # print(first_name,last_name,email,username,password,gender, cource_id,session_year,  profile_pic)

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "The Entred Email Is Already Exists.")
            return redirect('add-student')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "The Entred Username Is Already Exists.")
            return redirect('add-student')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3
                
            )
            user.set_password(password)
            user.save()

            cource = Cource.objects.get(id=cource_id)

            session_year= Session_Year.objects.get(id=session_year_id)

            student=Student(
                admin=user,
                address=address,
                session_year_id=session_year,
                cource_id=cource,
                gender=gender

            )
            student.save()
            messages.success(request, user.first_name + '  ' + user.last_name + ' ' + 'is Successfully Saved as a Student.')
            return redirect('add-student')

            

        


    context= {
        'cource':cource,
        'session_year':session_year
    }
    return render(request, 'hod/add_student.html', context)

# staff views
def staff(request):
    pass

# student view
def student(request):
    pass