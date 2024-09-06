from django.urls import path
from . import views
urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.Login_user, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.Logout, name='logout'),
    path('update/', views.details_change, name='update'),
]