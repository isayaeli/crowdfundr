from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Opportunity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='opps_images')
    details = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)
    deadline = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Opportunities'