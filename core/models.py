from django.db import models
from base.model import BaseModel

from phonenumber_field.modelfields import PhoneNumberField


class Service(BaseModel):
    name = models.CharField(max_length=500)
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.name


class Contact(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField(null=True, blank=True)
    services = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="service")
    subject = models.CharField(max_length=500, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.subject
    

class Review(BaseModel):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    msg = models.TextField()
    on_list = models.BooleanField(default=True)

    def __str__(self):
        return self.msg
    


