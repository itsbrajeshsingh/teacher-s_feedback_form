from django.contrib import admin
from django.urls import path, include
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name = 'home'),
    path('facultyresult/', views.faculty_result_view,name = 'facultyresult'),
    path('success/', views.logout_view, name = 'logout_now'),
    path('login/', views.login_view, name = 'login_now'),
    path('studentform/', views.student_form_view,name = 'studentform'),
]
