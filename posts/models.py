from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.conf import settings

import misaka # allows users to write mark down inside their own posts

from groups.models import Group
# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model() # connects current post to current logged in User (i.e. who's posting)

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True) # autogenerate date-time of post
    message = models.TextField() # capture current message
    message_html = models.TextField(editable=False) # current message not editable
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True, on_delete=models.CASCADE) # featres of foreign key

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # use primary key to relate to posts
        return reverse('posts:single', kwargs={'username':self.user.username, 'pk':self.pk})

    class Meta:
        ordering = ['-created_at'] #view posts in descending order
        unique_together = ['user', 'message'] # uniquely link every message to a User
