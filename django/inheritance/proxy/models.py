from django.db import models
from django.db.models.manager import BaseManager


class User(models.Model):
    name = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_block = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class AdminManager(BaseManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=True)


class Admin(User):
    class Meta:
        proxy = True

    def __str__(self):
        return f'{self.name} (관리자)'

    @staticmethod
    def drop(user):
        user.delete()


class StaffManager(BaseManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=True)


class Staff(User):
    class Meta:
        proxy = True

    def __str__(self):
        return f'{self.name} (스태프)'

    @staticmethod
    def block(user):
        user.in_block = True
        user.save()
