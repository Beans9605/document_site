
from django.urls import path
from . import views
urlpatterns = [
    path('', views.propose_before, name="propose_before"),
    path('support/', views.support, name='support'),
    path('upload/', views.propose_data, name="propose_data"),
    path('apply/check/', views.apply_check_all, name="apply_check"),
    path('apply/check/<int:pk>/', views.apply_check_one, name="apply_one")
]
