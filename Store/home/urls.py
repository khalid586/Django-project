from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("ex1",views.ex1,name = "ex1"),
    path("analyze",views.analyze,name = 'analyze'),
    # path("about", views.about, name = 'about'),
    # path("services", views.services, name = 'services'),
    # path("contacts", views.contacts, name = 'contacts')
]
 