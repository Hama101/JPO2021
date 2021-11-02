from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index, name='home'),
    path('create-profile/', views.create_profile, name='create_profile'),
    path('profile/<str:CIN>/',views.profile, name='profile'),
]
