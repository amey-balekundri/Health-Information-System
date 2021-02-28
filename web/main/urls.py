
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name='home'),
    path('register',views.register,name='register'),
    path('login',views.login_request,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('dashboard_redirect',views.dashboard_redirect,name='dashboard_redirect'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='main/password_reset.html'),
            name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='main/password_reset_done.html'),
            name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='main/password_reset_confirm.html'),
            name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='main/password_reset_complete.html'),
            name='password_reset_complete'),
]   

