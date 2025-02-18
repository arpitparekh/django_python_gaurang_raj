from django.urls import path
from . import views
urlpatterns = [

    path('register/',views.show_register, name='register'),
    path('login/',views.show_login, name='login'),
    path('home/',views.show_home, name='home'),
    path('session/',views.show_session, name='session'),
    path('logout/',views.show_logout, name='logout'),


]
