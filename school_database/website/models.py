from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=60, unique=True)
    country = models.CharField('Country', max_length=150, blank=True)
    nationality = models.CharField('Nationality', max_length=150, blank=True)
    mobile = models.PositiveBigIntegerField('Mobile', null=True, blank=True)
    admin = models.BooleanField('Admin', default=False)
    student = models.BooleanField('Student', default=False)
    staff = models.BooleanField('Staff', default=True)
    editor = models.BooleanField('Editor', default=False)
