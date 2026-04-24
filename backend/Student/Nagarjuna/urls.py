from django.urls import path
from . import views

urlpatterns=[
    path('nag/',views.added)
]