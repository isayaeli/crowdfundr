from unicodedata import name
from django.urls import path
from .import views
urlpatterns = [
    path('index', views.index, name='index' ),
    path('sme-profile', views.sme_profile, name='sme_profile'),
    path('my-projects', views.projects, name='my_projects'),
    path('add-projects', views.add_project, name='add_project'),
    path('update-project/<int:id>', views.update_project, name='update_project'),
    path('delete-project/<int:id>', views.delete_project, name='delete_project')
]
