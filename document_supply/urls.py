
from django.urls import path
from . import views
urlpatterns = [
    path('', views.propose_before, name="propose_before")
]
