
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_home, name='home'),
    path('manager/', views.user_page, name='user_page'),
    path('manager/login/', views.user_check, name='user_check'),
    path('manager/logout/', views.user_logout, name='user_logout'),
]
