from django.urls import path
from app_attendance_system import views
urlpatterns = [
    path('', views.Index, name='index'),
    path('profile/', views.Profile, name='profile'),
    path('dashboard/', views.Dashboard, name='dashboard'),
]
