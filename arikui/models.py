from django.db import models
from django.contrib import auth
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.mail import send_mail
from django.core.validators import MaxValueValidator, MinValueValidator

# from django.db.models.fields import IntegerField

class Videoinfo(models.Model):
    title = models.CharField("タイトル", max_length=100)
    pub_date = models.DateField ("動画投稿時間")
    image = models.ImageField(upload_to='arikui/images/')

    def __str__(self):
        return self.title


# class Users(auth.models.user):
#     u = "a"

# from django.contrib.auth.base_user import AbstractBaseUser