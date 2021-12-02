from django.urls import path

from . import views

# This file holds the URLs for the 'main' app
urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
]