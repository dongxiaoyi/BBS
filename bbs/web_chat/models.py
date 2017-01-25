from django.db import models
import sys
sys.path.append('..')
from web.models import UserProfile
# Create your models here.
class QQGroup(models.Model):
    name = models.CharField(max_length=64,unique=True)
    description = models.CharField(max_length=255,default="nothing")
    members = models.ManyToManyField(UserProfile,blank=True)
    admins = models.ManyToManyField(UserProfile,related_name='group_admins')
    max_member_nums = models.IntegerField(default=200)
    def __str__(self):
        return self.name

