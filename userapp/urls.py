from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    #...
    path('', views.login),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    path('xml_parser/', views.xml_parser),


]