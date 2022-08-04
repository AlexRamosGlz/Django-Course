
from django.db import models
from django.forms import CharField, IntegerField

from . import validators

class Address(models.Model):
    address = models.CharField(max_length=100) 

    def __str__(self) -> str:
        return f"{self.address}"


class CreditCard(models.Model):
    credit_card_number = models.IntegerField(null=True)
    expire_date = models.CharField(max_length=5, null=True)
    ccv = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.credit_card_number} / {self.expire_date} / {self.ccv}"

class Token(models.Model):
    token = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return f"{self.token}"


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[validators.validateIsNotLessThan0])
    password = models.CharField(validators=[validators.validatePassword], max_length=30, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, related_name="user")
    credit_card = models.OneToOneField(CreditCard, on_delete=models.CASCADE, null=True)
    token = models.ManyToManyField(Token)

    def __str__(self) -> str:
        return f"{self.name} | {self.age} | {self.address} | {self.credit_card} | {self.token}"


