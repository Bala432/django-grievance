from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    roll_number = models.CharField(max_length=15,unique=True)
    mobile_number = models.CharField(max_length=15,unique=True)

    def __str__(self):
        return self.user.username

class Publish(models.Model):

    superpost = models.ForeignKey(UserInfo,on_delete=models.PROTECT,null=True,related_name='publish')
    problem = models.CharField(max_length=50,default=" ")
    details = models.TextField(max_length=512)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.problem

    def get_absolute_url(self):
        return reverse('thanks')


class Post(models.Model):
    userpost = models.ForeignKey(UserInfo, on_delete=models.PROTECT, null=True, related_name='posts')
    uservote = models.ForeignKey(Publish,on_delete=models.PROTECT,null=True,related_name='votes')
    title = models.CharField(max_length=50, default=" ")
    text = models.TextField(max_length=512)
    publish_date = models.DateTimeField(blank=True, null=True)
    upvote = models.PositiveIntegerField(default=0)
    downvote = models.PositiveIntegerField(default=0)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('thankyou')





