from django.db import models
from django.contrib.auth.modelsn import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    class Meta:
        db_table = 'custom_user'

    login_count = models.IntegerField(verbose_name='ログイン回数', default=0)
