from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()
    DoesNotExist = models.Manager()

    class Meta:
        abstract = True


class Employment(BaseModel):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30, blank='true', default='employment')

    # user = models.ForeignKey('models.Users', related_name='employment', on_delete=models.SET_DEFAULT, default='')


class Users(BaseModel):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20, blank='true', default='user_name')
    surname = models.CharField(max_length=20, blank='true', default='user_surname')
    age = models.SmallIntegerField(blank='true', default='user_age')

    class Meta:
        verbose_name_plural = "user"
