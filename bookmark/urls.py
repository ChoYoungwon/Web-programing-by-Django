from django.urls import path
from . import views

app_name = 'bookmark'


urlpatterns = [
    path('', views.BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),

    # /bookmark/add
    path('add/', views.BookmarkCreateView.as_view(), name="add",),

    # /bookmark/change/
    path('change/', views.BookmarkChangeLV.as_view(), name="change",),

    # /bookmark/1/update
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name="update",),

    # /bookmark/1/delete
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name="delete",),
]