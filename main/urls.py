from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit-contact/', views.submit_contact, name='submit_contact'),
    path('submit-review/', views.submit_review, name='submit_review'),
    
    # Authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
    # User Dashboard and Profile
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    
    # Villa Reports (User)
    path('villa-reports/', views.villa_reports, name='villa_reports'),
    path('villa-report/<int:report_id>/', views.villa_report_detail, name='villa_report_detail'),
    
    # Admin Routes
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-panel/create-report/', views.admin_create_report, name='admin_create_report'),
    path('admin-panel/edit-report/<int:report_id>/', views.admin_edit_report, name='admin_edit_report'),
    path('admin-panel/report/<int:report_id>/', views.admin_report_detail, name='admin_report_detail'),
]
