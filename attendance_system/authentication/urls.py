from django.urls import path,include
from .views import LoginView,RegisterView,LogoutView, DoLoginView

urlpatterns = [

   path('', LoginView.as_view(), name='login'),
   path('dologin/', DoLoginView.as_view(), name='dologin'),
   path('register/', RegisterView.as_view(), name='register'),
   path('logout/', LogoutView.as_view(), name='logout'),
]