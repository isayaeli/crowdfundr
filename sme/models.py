from datetime import datetime
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
import math
from django.utils import timezone
# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title =  models.CharField(max_length=100)
    project_duration = models.CharField(max_length=100)
    beneficiaries = models.TextField()
    target_area = models.TextField()
    project_overview = models.TextField()
    proposal = models.FileField(upload_to='proposals', null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True,blank=True)
    project_image = models.FileField(upload_to='project_image', default='brief.png')
    goal = models.IntegerField(default=0)
    created_on =  models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    @property
    def get_all_donations(self):
        all_ = Donation.objects.filter(project=self.id, verified=True).order_by('-id')[:2]
        return all_

    @property
    def get_donation_sum(self):
        donations = Donation.objects.filter(project=self.id, verified=True)
        sum_ =  sum(donations.values_list('donation', flat=True))
        return sum_

    @property
    def get_percent(self):
      
        donations = Donation.objects.filter(project=self.id, verified=True)
        sum_ =  sum(donations.values_list('donation', flat=True))
        try:
           percent = round( sum_/ self.goal * 100)
        except ZeroDivisionError:
            percent =  0
        return percent
    
    @property
    def words(self):
        word = Word_of_support.objects.filter(project=self.id)
        return word
        



    @property
    def published(self):
        now = timezone.now()

        diff = now - self.created_on
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds
            if seconds == 1:
                return str(seconds) + " second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        if diff.days >= 1 and diff.days < 30:
            days = diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
                
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years = math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"



class Donation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    name  = models.CharField(max_length=100)
    donation = models.IntegerField(default=0)
    verified =  models.BooleanField(default=False)
    donation_id =  models.CharField(max_length=255)
    donated_on = models.DateTimeField(default=datetime.now())
    

    def __str__(self):
        return str(self.user)


class Word_of_support(models.Model):
    word = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    added_on = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.user)
