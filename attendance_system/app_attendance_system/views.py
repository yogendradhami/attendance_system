from django.shortcuts import render

# Create your views here.
def Index(request):

    return render(request, 'layouts/master.html')

def Profile(request):

    return render(request, 'profile/users-profile.html')

def Dashboard(request):

    return render(request, 'components/dashboard.html')

