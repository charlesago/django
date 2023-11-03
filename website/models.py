from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    USERNAME_FIELD = 'username'
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Message(models.Model):

    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE, default="missing_author")
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)



class Response(models.Model):
    content = models.CharField(max_length=900)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default="missing_author")


