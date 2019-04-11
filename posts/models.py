from django.db import models
from django.conf import settings

class Post(models.Model):
    content = models.CharField(max_length=140)
    image = models.ImageField(blank=True)
    # User와 연결
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)