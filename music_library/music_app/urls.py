from django.urls import path
from . import views

urlpatterns = [
    path('music_app/', views.SongList.as_view()),
    path('music_app/<int:pk>', views.SongDetail.as_view()),
    path('music_app/<int:pk>likes', views.SongLikes.as_view()),
]
