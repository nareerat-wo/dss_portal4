from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='web-home'),
    path('dashboard/', views.dashboard, name='web-dashboard'),
    path('customer/', views.customer, name='web-customer'),
    path('inquiry/', views.inquiry, name='web-inquiry'),
    path('alert/', views.alert, name='web-alert'),
]   