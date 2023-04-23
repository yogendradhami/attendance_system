from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER = {
        (1, 'HOD'),
        (2, 'STAFF'),
        (3, 'STUDENT'),
    }

    user_type= models.CharField(choices=USER, max_length=1, default=1)
    profile_pic = models.ImageField(upload_to='static/assets/img/profile_pic/')
    