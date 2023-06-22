from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("about", views.about, name = 'about'),
    path("analyze",views.analyze,name = 'analyze'),
    path("services", views.services, name = 'services'),
    path("contacts", views.contacts, name = 'contacts')
]
 