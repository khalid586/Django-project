from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    path("test", views.test, name = 'test'),
    path("", views.index, name = 'home'),
    
    path("about", views.about, name = 'about'),
    path("removePunc",views.removePunc,name = 'removePunc'),
    path("services", views.services, name = 'services'),
    path("contacts", views.contacts, name = 'contacts')
]
 