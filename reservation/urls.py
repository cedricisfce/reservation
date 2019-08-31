from django.urls import path

from reservation import views

urlpatterns = [
    path('shows/', views.shows_list, name='home')
]