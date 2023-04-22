from django.shortcuts import render

# Create your views here.
def Index(request):

    return render(request, 'layouts/master.html')

def Profile(request):

    return render(request, '/user-profile.html')