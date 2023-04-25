from django.shortcuts import render,redirect
from app_attendance_system.models import CustomUser,Cource,Student,Session_Year,Staff,Subject
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
    student_count= Student.objects.all().count()
    staff_count= Staff.objects.all().count()
    cource_count= Cource.objects.all().count()
    subject_count= Subject.objects.all().count()

    student_gender_male = Student.objects.filter(gender='Male').count()
    student_gender_female= Student.objects.filter(gender='Female').count()
    # print(student_gender_male,student_gender_female)

    context={
        'student_count':student_count,
        'staff_count':staff_count,
        'cource_count':cource_count,
        'subject_count':subject_count,
        'student_gender_male':student_gender_male,
        'student_gender_female':student_gender_female,
    }

    return render(request, 'components/dashboard.html',context)

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

def HodViewStudent(request):
    student = Student.objects.all()
    context= {
        'student':student
    }
    return render(request, 'hod/view_student.html',context)

def HodEditStudent(request,id):
    student= Student.objects.filter(id=id)
    cource= Cource.objects.all()
    session_year=Session_Year.objects.all()
    context= {
        'student':student,
        'cource':cource,
        'session_year':session_year
    }
    return render(request, 'hod/edit_student.html',context)

def HodUpdateStudent(request):
        if request.method== 'POST':
            student_id=request.POST.get('student_id')
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

            user= CustomUser.objects.get(id=student_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            if password != None and password != "":
                user.set_password(password)

            if profile_pic != None and profile_pic !="":
                user.profile_pic = profile_pic
            user.save()
       

            student=Student.objects.get(admin=student_id)
            student.address=address
            student.gender=gender
            
            cource= Cource.objects.get(id=cource_id)
            student.cource_id=cource

            session_year=Session_Year.objects.get(id=session_year_id)
            student.session_year_id=session_year
            student.save()
            messages.success(request, "Records Are Successfully Updated")
            return redirect('view-student')

        return render(request, 'hod/edit_student.html')

def HodDeleteStudent(request, admin):
    student=CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request,'User Deleted Successfully.')
    return redirect('view-student')


def HodAddCource(request):
    # cource=Cource.objects.all()
    if request.method== 'POST':
        cource_name=request.POST.get('cource_name')
        # print(cource_name)
        cource=Cource(name=cource_name)
        cource.save()
        messages.success(request, "Cource Successfully Created.")
        return redirect('add-cource')
    return render(request, 'hod/add_cource.html')

def HodViewCource(request):
    cource=Cource.objects.all()
    print(cource)

    context= {
        'cource':cource
    }

    return render(request, 'hod/view_cource.html',context)

def HodEditCource(request,id):
        cource=Cource.objects.get(id=id)
        context= {
            'cource':cource
        }
        return render(request, 'hod/edit_cource.html',context)
def HodUpdateCource(request):
        if request.method=='POST':
            name=request.POST.get('cource_name')
            cource_id=request.POST.get('cource_id')
            # print(cource_name,cource_id)
            cource=Cource.objects.get(id=cource_id)
            cource.name=name
            cource.save()
            messages.success(request, 'Cource Are Updated Successfully.')
            return redirect('view-cource')
        
        return render(request, 'hod/edit_cource.html')

def HodDeleteCource(request,id):
    cource=Cource.objects.get(id=id)
    cource.delete()
    messages.success(request, "Cource are Successfully Deleted.")
    return redirect('view-cource')
    return render(request, 'hod/edit_cource.html')

# staff views
def HodAddStaff(request):
    if request.method=='POST':
        first_name= request.POST.get('first_name')
        last_name=request.POST.get("last_name")
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        profile_pic=request.FILES.get('profile_pic')
        # print(first_name,last_name,username,email,password,address,gender,profile_pic)

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "The Entered Email Is Already Exists.")
            return redirect('add-staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "The Entered Username Is Already Taken.")
            return redirect('add-staff')
        
        else:
            user= CustomUser(first_name=first_name,last_name=last_name, email=email,username=username, profile_pic=profile_pic,user_type=2)
            user.set_password(password)
            user.save()

            staff = Staff(
                admin=user,
                address=address,
                gender=gender

            )
            staff.save()

            messages.success(request, user.first_name + '  ' + user.last_name + ' ' + 'is Successfully Saved as a Staff.')
            return redirect('view-staff')

    return render(request, 'hod/add_staff.html')

def hodViewStaff(request):
    staff= Staff.objects.all()
    print(staff)
    context={
        'staff':staff
    }

    return render(request, 'hod/view_staff.html', context)

def hodEditStaff(request ,id):
    staff= Staff.objects.get(id=id)
    context={'staff':staff}
 

    return render(request, 'hod/edit_staff.html',context)


def hodUpdateStaff(request):
         if request.method == 'POST':
            staff_id=request.POST.get('staff_id')
            first_name= request.POST.get('first_name')
            last_name=request.POST.get("last_name")
            email=request.POST.get('email')
            username=request.POST.get('username')
            password=request.POST.get('password')
            address=request.POST.get('address')
            gender=request.POST.get('gender')

            profile_pic=request.FILES.get('profile_pic')

            user= CustomUser.objects.get(id=staff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username

            if password != None and password != "":
                user.set_password(password)

            if profile_pic != None and profile_pic !="":
                user.profile_pic = profile_pic
            user.save()

            staff=Staff.objects.get(admin=staff_id)
            staff.address=address
            staff.gender=gender
            
            staff.save()

            messages.success(request, "Staff Records Are Successfully Updated")
            return redirect('view-staff')
            return render(request, 'hod/edit_staff.html')

def HodDeleteStaff(request, admin):
    staff=CustomUser.objects.get(id=admin)
    staff.delete()
    messages.success(request, "Staff Records Are Successfully Deleted.")
    return redirect('view-staff')

    
# student view
def student(request):
    pass

def AddSubject(request):
    cource= Cource.objects.all()
    staff= Staff.objects.all()

    context= {'cource':cource, 'staff':staff}

    if request.method == 'POST':
        subject_name=request.POST.get('subject_name')
        cource_id=request.POST.get('cource_id')
        staff_id=request.POST.get('staff_id')
        cource=Cource.objects.get(id=cource_id)
        staff=Staff.objects.get(id=staff_id)
        subject=Subject(
            name=subject_name,
            cource=cource,
            staff=staff
        )
        subject.save()
        messages.success(request, "Subject Are Added Successfully .")
        return redirect('add-subject')
    return render(request, 'hod/add_subject.html', context)

def ViewSubject(request):
    subject= Subject.objects.all()
    context= {
        'subject':subject
    }
    return render(request, 'hod/view_subject.html', context)

def EditSubject(request, id):
    subject=Subject.objects.get(id=id)
    cource=Cource.objects.all()
    staff=Staff.objects.all()
    context= {
        'subject':subject,
        'cource':cource,
        'staff':staff,
    }

    return render(request, 'hod/edit_subject.html', context)

def UpdateSubject(request):
    if request.method== 'POST':
        subject_id=request.POST.get('subject_id')
        subject_name=request.POST.get('subject_name')
        cource_id= request.POST.get('cource_id')
        staff_id = request.POST.get('staff_id')
        # print(subject_id,cource_id,staff_id)
        cource=Cource.objects.get(id=cource_id)
        staff=Staff.objects.get(id= staff_id)

        subject= Subject(
            id=subject_id,
            name=subject_name,
            cource=cource,
            staff=staff
        )
        subject.save()
        messages.success(request, "Subjects are Updated Successfully.")
        return  redirect('view-subject')

def DeleteSubject(request, id):
    subject=Subject.objects.filter(id=id)
    subject.delete()
    messages.success(request, "Student Records Deleted Successfully.")
    return redirect('view-subject')

def AddSession(request):
    if request.method=='POST':
        session_year_start= request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')
        session= Session_Year(
            session_start= session_year_start,
            session_end= session_year_end
        )
        session.save()
        messages.success(request, "Session Are Successfully Created.")
        return redirect('add-session')
    return render(request,'hod/add_session.html')

def ViewSession(request):
    session = Session_Year.objects.all()

    context={
        'session':session
    }
    return render(request,'hod/view_session.html',context)

def EditSession(request, id):
    session = Session_Year.objects.filter(id=id)
    context={
        'session':session
    }
    return render(request,'hod/edit_session.html',context)

def UpdateSession(request):
    if request.method == 'POST':
        session_id= request.POST.get('session_id')
        session_year_start= request.POST.get('session_year_start')
        session_year_end= request.POST.get('session_year_end')

        session= Session_Year(
            id=session_id,
            session_start= session_year_start,
            session_end=session_year_end,
        )
        session.save()
        messages.success(request, "Session Updated Successfully.")
        return redirect('view-session')

def DeleteSession(request, id):
        session=Session_Year.objects.get(id=id)
        session.delete()
        messages.success(request, "Session Records Deleted Successfully.")
        return redirect('view-session')

