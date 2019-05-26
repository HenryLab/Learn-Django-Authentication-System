from django.urls import path

from . import views

urlpatterns = [
    path('', views.sign_up, name='user_sign'),
    path('dashboard', views.user_dashboard, name='user_dashboard'),
    path('login', views.sign_in, name='login_user'),
]
