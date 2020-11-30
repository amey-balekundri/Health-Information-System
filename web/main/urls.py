
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('register',views.register,name='register'),
    path('login',views.login_request,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('dashboard_redirect',views.dashboard_redirect,name='dashboard_redirect')
]