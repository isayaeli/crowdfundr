from django.urls import path
from . import views
urlpatterns = [
    path('login', views.request_login, name="login")
]