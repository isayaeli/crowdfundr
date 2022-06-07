from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home, name='home'),
    path('projects', views.projects, name='projects'),
    path('opportunities', views.opportunities, name='opportunities'),
    path('donate/<int:id>', views.donate, name="donate"),
    path('word/<int:id>', views.word, name="word"),
    path('success', views.payment_response, name='success'),
    path('cancelled', views.payment_cancelled, name='cancel'),
     path('contact', views.contact, name='contact'),
]