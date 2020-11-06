from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()
    DoesNotExist = models.Manager()

    class Meta:
        abstract = True


class Users(BaseModel):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20, blank='true', default='user_name')
    surname = models.CharField(max_length=20, blank='true', default='user_surname')
    age = models.SmallIntegerField(blank='true', default='user_age')

    class Meta:
        verbose_name_plural = "user"


class Employment(BaseModel):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30, blank='true', default='employment')
    barcode = models.BigIntegerField(blank='True', default='2998060398046')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default='3')
