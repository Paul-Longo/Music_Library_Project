from django.urls import path
from . import views

urlpatterns = [
    path('music_app/', views.SongList.as_view()),
]
