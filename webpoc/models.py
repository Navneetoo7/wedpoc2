from MyProject.settings import AUTH_PASSWORD_VALIDATORS
from django.db import models
from django.db.models.fields import AutoField, CharField

# Create your models here.
COUNTRY_CHOICES = (
    ('india','INDIA'), ('germany','GERMANY'), ('france', 'FRANCE'), ('russia','RUSSIA'),
)
CITY_CHOICES = (
    ('mumbai','MUMBAI'), ('delhi','DELHI'), ('banglore','BANGLORE'), 
    ('dusseldore','DUSSELDORF'), ('berlin','BERLIN'), ('paris','PARIS'), ('moscow','MOSCOW'),('kazan', 'KAZAN'),
)

class Login(models.Model):
    customer_id = models.AutoField(primary_key=True)
    email_id = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    attempts = models.IntegerField(default=0)
    locked = models.IntegerField(default=0)

    def __str__(self):
        return str(self.customer_id) 



class Customer(models.Model):
    transaction_id = models.AutoField 
    customer_id = models.ForeignKey(Login, on_delete=models.CASCADE)
    transdate = models.DateField(auto_now_add=True)
    cfname = models.CharField(max_length=100)
    clname = models.CharField(max_length=100)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES)
    ccity = models.CharField(max_length=50, choices=CITY_CHOICES)
    ptype = models.CharField(max_length=100)
    product = models.IntegerField(default=0)
    qty = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    active = models.IntegerField(default=0)

    def __str__(self):
        return str(self.customer_id)
   


