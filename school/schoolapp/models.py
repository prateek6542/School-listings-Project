from django.db import models

class Pincode(models.Model):
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.code

class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    pincode = models.ForeignKey(Pincode, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
