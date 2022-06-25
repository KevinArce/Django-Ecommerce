from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255) # max_length is the maximum number of characters in the field
    description = models.TextField(blank=True) # blank=True means that the field is optional
    price = models.DecimalField(max_digits=6, decimal_places=2) # max_digits is the maximum number of digits in the field, decimal_places is the number of decimal places
    inventory = models.IntegerField(default=0) # default=0 means that the field will be set to 0 by default
    last_update = models.DateTimeField(auto_now=True) # auto_now=True means that the field will be set to the current date and time whenever the model is saved


class Customer(models.Model):

    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
    (MEMBERSHIP_BRONZE, 'Bronze'), 
    (MEMBERSHIP_SILVER, 'Silver'), 
    (MEMBERSHIP_GOLD, 'Gold')]

    first_name = models.CharField(max_length=255) # max_length is the maximum number of characters in the field
    last_name = models.CharField(max_length=255) # max_length is the maximum number of characters in the field
    email = models.EmailField(max_length=255, unique=True) # unique=True means that the field must be unique 
    phone = models.CharField(max_length=255) # max_length is the maximum number of characters in the field
    birth_date = models.DateField(null=True) # null=True means that the field is optional
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE) # default=MEMBERSHIP_BRONZE means that the field will be set to MEMBERSHIP_BRONZE by default

class Order(models.Model):

    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
    (PAYMENT_STATUS_PENDING, 'Pending'),
    (PAYMENT_STATUS_COMPLETE, 'Complete'),
    (PAYMENT_STATUS_FAILED, 'Failed')]

    placed_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True means that the field will be set to the current date and time whenever the model is saved
    payment_status = models.CharField(
    max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING) # default=PAYMENT_STATUS_PENDING means that the field will be set to PAYMENT_STATUS_PENDING by default

class Address(models.Model):
    street = models.CharField(max_length=255) # max_length is the maximum number of characters in the field
    city = models.CharField(max_length=255) # max_length is the maximum number of characters in the field
    customer = models.OneToOneField( # OneToOneField means that there can only be one address per customer
    Customer, on_delete=models.CASCADE, # on_delete=models.CASCADE means that the address will be deleted when the customer is deleted (on_delete=models.CASCADE is the default value)
    primary_key=True) # primary_key=True means that the field will be the primary key of the model
    