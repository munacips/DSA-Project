from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    dob = models.DateField()
    married = models.BooleanField()
    bank_balance = models.FloatField(default=10.89)

    def __str__(self):
        return self.first_name + ' ' +self.last_name