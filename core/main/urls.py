from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('home_detail/<int:id>/', views.home_detail, name='home_detail'),
    path('review/', views.review, name= 'review')
]