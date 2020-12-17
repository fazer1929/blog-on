from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(default=timezone.now)
    user= models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def get_absolute_url(self):
        return reverse('blog-detail',kwargs={"pk":self.pk})