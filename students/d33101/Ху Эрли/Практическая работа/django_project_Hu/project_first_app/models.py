from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.
class Owner(models.Model):  # 车主-Автовладелец
    # id_owners = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    date_birth = models.DateField(null=True)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Possession(models.Model): # 领地-Владение
    # id_owner_cars = models.AutoField(primary_key=True)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    date_begin = models.DateField()
    date_end = models.DateField(null=True)


class Car(models.Model):
    # id_cars = models.AutoField(null=True)
    number_plate = models.CharField(max_length=15)
    car_brand = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    car_color = models.CharField(max_length=30)
    owners = models.ManyToManyField(Owner, through='Possession')

    def __str__(self):
        return self.car_brand


class License(models.Model):    # 司机的执照-Водительское_удостоверение
    # id_license = models.AutoField(primary_key=True)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    number_license = models.CharField(max_length=10)
    type_license = models.CharField(max_length=10)
    date_out = models.DateField()


# creating a form
class OwnerForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Owner

        # specify fields to be used
        fields = [
            "name",
            "surname",
            "date_birth",
        ]

class User(AbstractUser):
    id_passport = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)



























