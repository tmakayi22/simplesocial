from django.db import models
from django.utils.text import slugify # adds lower_case n dahes to string with spaces
from django.urls import reverse

import misaka
# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model() # allows calling current User session

from django import template
register = template.Library() # allows use of custom template tags

# Main model
class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    # save slug and description together
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) # fills out spaces in user name with dashes
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE) # allows User membership to a group
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE) # link current User to several groups they belong to

    # Returns current user name
    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')
