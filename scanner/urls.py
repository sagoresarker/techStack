from django.urls import path
from . import views

urlpatterns = [
    path('scan/', views.scan, name='scan'),
    path('sacn-result', views.scan_result, name='scanner-result'),
]
