from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User

# Create your models here.
    

class Organization(models.Model):
    title = models.CharField(max_length=255)
    #pub_date = models.DateTimeField()
    description = models.TextField()
    email = models.EmailField()
    registration_number = models.CharField(max_length=10, primary_key=True)
    contact = PhoneField()
    url = models.URLField()
    thumbnail = models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to='images/')
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    hunger = models.BooleanField()
    homeless = models.BooleanField()
    women = models.BooleanField()
    children = models.BooleanField()
    elderly = models.BooleanField()
    cancer = models.BooleanField()
    differently_abled = models.BooleanField()

    def __str__(self):
        return self.title