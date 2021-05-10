from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User

# Create your models here.
    

class Ngos(models.Model):
    title = models.CharField(max_length=255)
    #pub_date = models.DateTimeField()
    description = models.TextField()
    email = models.EmailField()
    registration_number = models.CharField(max_length=10, primary_key=True)
    contact = PhoneField()
    url = models.URLField()
    thumbnail = models.FileField(upload_to='images/')
    image = models.FileField(upload_to='images/')
    hunger = models.BooleanField()
    homeless = models.BooleanField()
    women = models.BooleanField()
    children = models.BooleanField()
    elderly = models.BooleanField()
    cancer = models.BooleanField()
    differently_abled = models.BooleanField()
    account = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title