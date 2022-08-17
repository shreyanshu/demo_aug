from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=100)
    no_likes = models.IntegerField()
    date_written = models.DateField()
    author = models.CharField(max_length=50, null=True)