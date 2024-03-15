from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/")
    tags = ArrayField(models.CharField(max_length=10), size=5)