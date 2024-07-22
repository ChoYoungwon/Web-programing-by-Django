from django.urls import path
from . import views

app_name = 'bookmark'


urlpatterns = [
    path('', views.BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail')
]