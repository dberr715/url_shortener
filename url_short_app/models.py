from django.db import models


# Create your models here.
class UserData(models.Model):
    username = models.CharField()
    password = models.CharField()
    token = models.CharField()

    def __str__(self):
        return self.username


class UrlData(models.Model):
    title = models.CharField(max_length=100)
    longUrl = models.CharField(max_length=100)
    shortUrl = models.CharField(max_length=100)
    userId = models.ForeignKey(UserData, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
