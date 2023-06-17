from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_rooms_view, name='rooms'),
    path('<slug:slug>/', views.detail_room_view, name='room_detail'),
]