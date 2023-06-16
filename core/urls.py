from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_screen_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('rooms/', views.rooms_view, name='rooms')
]