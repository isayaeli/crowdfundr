from django.urls import path
from .import views

urlpatterns = [
    path('donor-dashboard', views.dashboard, name="donor" ),
     path('donor-profile', views.donor_profile, name='profile' ),
    path('add', views.add_opportunity, name="add_opp" ),
     path('my-opportunities', views.opportunities, name="my_opps" ),
    path('update-opportunity/<int:id>', views.update_opportunity, name="update_opp" ),
    path('delete-opportunity/<int:id>', views.delete_opportunity, name="delete_opp" )
]