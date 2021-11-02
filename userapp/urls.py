from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    #...
    path('', views.login_user),
    path('login/', views.login_user),
    path('signup/', views.signUp),
    path('accounts/', include('allauth.urls')),
    path('logout', views.logout_user),
    path('xml_parser/', views.xml_parser),

]