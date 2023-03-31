from django.urls import path

from . import views
urlpatterns = [
    path('', views.natal),
    path('tiradentes', views.tiradentes),
    path('orlando', views.orlando),
]