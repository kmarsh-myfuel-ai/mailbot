from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("grab", views.grab, name="grab"),
]