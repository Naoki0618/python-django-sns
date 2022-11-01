from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.urls import reverse_lazy
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Enter Email')  # エラーメッセージ
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)  # passwordを引数にとってパスワード設定
        user.save(using=self._db)  # データベースへユーザーを保存
        return user
 
    def create_superuser(self, username, email, password=None):
        if not email:
            raise ValueError('Enter Email')  # エラーメッセージ
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)  # passwordを引数にとってパスワード設定
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
 
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # プロフィール画像をavatarとして設定
    avatar = models.ImageField(blank=True, null=True)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_absolute_url(self):
        return reverse_lazy('accounts:home')
