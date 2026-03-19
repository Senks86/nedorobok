from django.urls import path
from . import views

urlpatterns = [
    path('', views.games_list, name="games_list"),
    #path("snake/", views.snake, name="snake"),
    path("circle/", views.circle, name="circle"),
    #path("flappy/", views.flappy, name="flappy"),
]