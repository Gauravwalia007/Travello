from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from . import views
from django.contrib.auth.views import (
    PasswordResetView,PasswordResetDoneView,
    PasswordResetConfirmView,PasswordResetCompleteView
    )


urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('profile',views.profile,name='profile'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('change_password',views.change_password,name='change_password'),
    path('password_reset',PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password_reset_confrim',PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),

]
