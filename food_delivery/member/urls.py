from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('findId/', views.findId),
    path('findPw/', views.findPw),
    path('signup/', views.signup),
    path('signupCheck/', views.signupCheck),
]