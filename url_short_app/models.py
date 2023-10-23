from django.db import models


# Create your models here.
class UserData(models.Model):
    username = models.CharField()
    password = models.CharField()
    token = models.CharField()

    def __str__(self):
        return self.username


class UrlData(models.Model):
    title = models.CharField()
    longUrl = models.CharField()
    shortUrl = models.CharField()
    userId = models.CharField()

    def __str__(self):
        return self.title
