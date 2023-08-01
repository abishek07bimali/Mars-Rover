from django.contrib import admin
from django.urls import path
from home import views
from django.urls import include

urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('dashboard.html',views.dashboard, name='dashboard'),
    path('control.html',views.control, name='control'),
    path('visualization.html',views.visualization, name='visualization'),
    path('location.html', views.map, name='map'),
    path('run/', views.run_script, name='run_script'),
]
