from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("about", views.about, name = 'about'),
    path("services", views.services, name = 'services'),
    path('login',views.login, name = "login"),
    path('logout', views.logoutUser, name = "logout"), 
    path("contacts", views.contacts, name = 'contacts')
]
