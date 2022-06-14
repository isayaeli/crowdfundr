from django.urls import path
from . import views

urlpatterns = [
    path('login', views.request_login, name="login"),
    path('register', views.register_request, name="register"),
    path('logout', views.logout_request, name="logout"),
    
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    path('confirm/', views.confirm_account, name='confirm'),
    path('confirm-link/', views.confirm_link , name='confirm-link'),

    path('change-password',views.passwordchange, name='changepassword')
]
