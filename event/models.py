from django.contrib.auth.models import User
from django.db import models


# class ContactManager(models.Manager):
#
#     def get_user_details(self):
#         return self.filter(
#
#         )


class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default=None)
    email = models.EmailField()
    phone = models.CharField(max_length=100, default=None)
    address = models.CharField(max_length=100, default=None)
    comments = models.TextField()
    print(user)
    def __str__(self):
        return self.name
