
from django.urls import path
from . import views
urlpatterns = [
    path("write/", views.write_email, name="email_write"),
    path("write/mail/", views.email_send, name="email_send"),
]
