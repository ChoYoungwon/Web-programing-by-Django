from django.urls import path
from photo import views

app_name = 'photo'
urlpatterns = [

    # /photo/
    path('', views.AlbumLV.as_view(), name='index'),

    # /photo/album
    path('album', views.AlbumLV.as_view(), name='album_list'),

    # /photo/album/99/
    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),

    # /photo/photo/99/
    path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),

    # /photo/album/add/
    path('album/add/', views.AlbumPhotoCV.as_view(), name='album_add'),

    # /photo/album/change/
    path('album/change/', views.AlbumChangeLV.as_view(), name='album_change'),

    # /photo/album/1/update/
    path('album/<int:pk>/update', views.AlbumPhotoUV.as_view(), name='album_update'),

    # /photo/album/1/delete
    path('album/<int:pk>/delete', views.AlbumDelV.as_view(), name='album_delete'),

    # /photo/photo/add/
    path('photo/add/', views.PhotoCV.as_view(), name='photo_add'),

    # /photo/photo/change/
    path('photo/change/', views.PhotoChangeLV.as_view(), name='photo_change'),

    # /photo/photo/1/update/
    path('photo/<int:pk>/update', views.PhotoUV.as_view(), name='photo_update'),

    # /photo/photo/1/delete/
    path('photo/<int:pk>/delete', views.PhotoDelV.as_view(), name='photo_delete'),


]