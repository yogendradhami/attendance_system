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
    path('hod/delete-staff/<str:admin>/', views.HodDeleteStaff, name='delete-staff'),


    path('hod/add-subject/', views.AddSubject, name='add-subject'),
    path('hod/view-subject/', views.ViewSubject, name='view-subject'),
    path('hod/edit-subject/<str:id>', views.EditSubject, name='edit-subject'),
    path('hod/update-subject/', views.UpdateSubject, name='update-subject'),
    path('hod/delete-subject/<str:id>', views.DeleteSubject, name='delete-subject'),

    path('hod/add-session/', views.AddSession, name='add-session'),
    path('hod/view-session/', views.ViewSession, name='view-session'),
    path('hod/edit-session/<str:id>/', views.EditSession, name='edit-session'),
    path('hod/update-session/', views.UpdateSession, name='update-session'),
    path('hod/delete-session/<str:id>/', views.DeleteSession, name='delete-session'),

    # hod  student feedback pannel
    path('hod/student-feedback/', views.StudentFeedbackSend, name='hod-student-feedback'),
    path('hod/student-save-feedback/', views.StudentFeedbackSave, name='hod-student-save-feedback'),
    
    # hod staff feedback pannel
    path('hod/staff-feedback/', views.StaffFeedbackSend, name='hod-staff-feedback'),
    path('hod/staff-save-feedback/', views.StaffFeedbackSave, name='hod-staff-save-feedback'),


    # staff Notification view
    path("hod/staff/send-notification/", views.StaffSendNotification, name="staff-send-notificatoin"),
    path("hod/staff/save-notification/", views.StaffSaveNotification, name="staff-save-notificatoin"),

    # student notification view
    path("hod/student/send-notification/", views.StudentSendNotification, name="student-send-notificatoin"),
    path("hod/student/save-notification/", views.StudentSaveNotification, name="student-save-notificatoin"),

    
    

    #hod staff Leave View
    path("hod/staff/leave-view/", views.StaffLeaveView, name="staff-leave-view"),
    path("hod/staff/approve-leave/<str:id>/", views.StaffApproveLeave, name="staff-approve-leave"),
    path("hod/staff/diapprove-leave/<str:id>/", views.StaffDisapproveLeave, name="staff-disapprove-leave"),

    # hod student leave url
    path("hod/student/leave-view/", views.StudentLeaveView, name="student-leave-view"),
    path("hod/student/approve-leave/<str:id>/", views.StudentApproveLeave, name="student-approve-leave"),
    path("hod/student/diapprove-leave/<str:id>/", views.StudentDisapproveLeave, name="student-disapprove-leave"),
    


    # this  is staff urls
    path('staff/home/', views.StaffHome,name='staff-home'),
    path('staff/notification/', views.StaffNotification,name='staff-notification'),
    path('staff/mark-as-done/<str:status>/', views.MarkAsDone,name='mark-as-done'),
    path('staff/apply-leave/', views.StaffApplyLeave,name='staff-apply-leave'),
    path('staff/apply-leave-save', views.StaffApplyLeaveSave,name='staff-apply-leave-save'),
    path('staff/feedback/', views.StaffFeedback,name='staff-feedback'),
    path('staff/save-feedback', views.StaffSaveFeedback,name='save-feedback'),

    # for staff attendace
    path('staff/take-attendance', views.StaffTakeAttendance,name='staff-take-attendance'),
    path('staff/save-attendance', views.StaffSaveAttendance,name='staff-save-attendance'),


    # urls for student
    path('student/home', views.StudentHome,name='student-home'),
    
    path('student/notification', views.StudentNotification,name='student-notification'),
    path('student/mark-as-done/<str:status>/', views.StudentMarkAsDone,name='student-mark-as-done'),
    path('student/feedback/', views.StudentFeedback,name='student-feedback'),
    path('student/save-feedback', views.StudentSaveFeedback,name='student-save-feedback'),

    path('student/apply-leave', views.StudentApplyLeave,name='student-apply-leave'),

    path('student/apply-leave-save', views.StudentApplyLeaveSave,name='student-apply-leave-save'),





]

