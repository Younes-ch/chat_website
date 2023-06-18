from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_rooms_view, name='rooms'),
    path('create/', views.create_room_view, name='room_create'),
    path('<slug:slug>/', views.detail_room_view, name='room_detail'),
    path('delete/<slug:slug>/', views.delete_room_view, name='room_delete')

]