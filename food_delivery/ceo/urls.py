from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order),
    path('progress/', views.progress),
    path('completion/', views.completion),
    path('detail/', views.detail),
    path('manage/', views.manage),
]