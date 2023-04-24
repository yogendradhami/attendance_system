from django.urls import path
from app_attendance_system import views


urlpatterns = [
    path('', views.Index, name='index'),

    # profile update
    path('profile/', views.Profile, name='profile'),
    path('update-profile/', views.UpdateProfile, name='update-profile'),
    
    path('dashboard/', views.Dashboard, name='dashboard'),

    path('hod/', views.Hod, name='hod'),
    path('hod/add-student/', views.HodAddStudent, name='add-student'),
    path('hod/view-student/', views.HodViewStudent, name='view-student'),

    path('hod/edit-student/<str:id>/', views.HodEditStudent, name='edit-student'),
    path('hod/update-student/', views.HodUpdateStudent, name='update-student'),
    path('hod/delete-student/<str:admin>/', views.HodDeleteStudent, name='delete-student'),

    path('hod/add-cource/', views.HodAddCource, name='add-cource'),
    path('hod/view-cource/', views.HodViewCource, name='view-cource'),
    path('hod/edit-cource/<str:id>/', views.HodEditCource, name='edit-cource'),
    path('hod/update-cource/', views.HodUpdateCource, name='update-cource'),
    path('hod/delete-cource/<str:id>/', views.HodDeleteCource, name='delete-cource'),

    path('hod/add-staff/', views.HodAddStaff, name='add-staff'),
    path('hod/view-staff/', views.hodViewStaff, name='view-staff'),
    path('hod/edit-staff/<str:id>/', views.hodEditStaff, name='edit-staff'),
    path('hod/update-staff/', views.hodUpdateStaff, name='update-staff'),
    path('hod/delete-staff/<str:admin>', views.HodDeleteStaff, name='delete-staff'),

]

