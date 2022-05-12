from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home, name='home'),
    path('projects', views.projects, name='projects'),
    path('opportunities', views.opportunities, name='opportunities'),
    path('donate/<int:id>', views.donate, name="donate"),
    path('response', views.payment_response, name='response'),
]