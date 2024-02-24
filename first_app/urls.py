from django.urls import path
from first_app import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('login_form/', views.login_form, name='login_form'),
    path('log_in/', views.log_in, name='log_in'),
    path('logout/', views.logout_user, name='logout'),
    path('accounts/login', views.login_form, name='login_form'),
    path('registration/', views.registration_user, name='registration'),
    path('forgot_password/', views.forgot_password, name='forgot_password')
]
