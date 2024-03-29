from .views import RegisterAPI,LoginAPI,ChangePasswordView, StaffApiView,StaffApiIdView,StudentApiView,StudentApiIdView
from django.urls import path,include
from knox import views as knox_views


urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    # api urls for staff
    path('staff/', StaffApiView.as_view()),
    path('staff/<int:id>/', StaffApiIdView.as_view()),
    path('student/', StudentApiView.as_view()),
    path('student/<int:id>/', StudentApiIdView.as_view()),

]