from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Donation, Project, Word_of_support

# Register your models here.
admin.site.unregister(Group)
admin.site.register(Project)
admin.site.register(Donation)
admin.site.register(Word_of_support)