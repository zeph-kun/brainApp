from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class User(BaseUserManager):

    def create_user(self, email, first_name, last_name, password, **other_fields):
        if not email:
            raise ValueError("You must provide your email adress")

        email = self.normalize_email(email)

        user = self.model(email=email, first_name=first_name, last_name=last_name, password=password, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('SuperUser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('SuperUser must be assigned to is_superuser=True')

        return self.create_user(email, first_name, last_name, password, **other_fields)


class Catalogue(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Formation(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    thumbnail = models.ImageField()
    price = models.FloatField()
    status = models.BooleanField()
    tag = models.CharField(max_length=50)
    id_catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE, null=False, unique=False)

    def __str__(self):
        return self.name


class CodeFormation(models.Model):
    code = models.IntegerField(null=False, unique=True)
    id_formation = models.ForeignKey(Formation, on_delete=models.CASCADE)


class Section(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=250)
    is_active = models.BooleanField()
    id_formation = models.ForeignKey(Formation, on_delete=models.CASCADE)


class Users(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    photo = models.ImageField(null=True)
    date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    object = User()
    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
