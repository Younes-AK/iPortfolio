from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('web_project/', views.web_project, name="web_project"),
    path('game_project/', views.game_project, name="game_project"),
    path('block_project/', views.block_project, name="block_project"),
]
