from django.urls import path
from app_attendance_system import views


urlpatterns = [
    path('', views.Index, name='index'),

    # profile update
    path('profile/', views.Profile, name='profile'),
    path('add-profile/', views.AddProfile, name='add-profile'),
    
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('hod/', views.Hod, name='hod'),
]

