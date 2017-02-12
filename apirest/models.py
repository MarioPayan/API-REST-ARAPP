from django.db import models


class Comment(models.Model):
    owner = models.CharField(max_length=30)
    body = models.CharField(max_length=180)
    marker = models.CharField(max_length=30)
    date = models.DateField()
    karma = models.IntegerField()