from django.db import models
from django.contrib.auth.models import User

class Gotweet(models.Model):
    user = models.ForeignKey(User, related_name='gotweets', on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=150)

    class Meta:
        ordering = ('-created_at',)


