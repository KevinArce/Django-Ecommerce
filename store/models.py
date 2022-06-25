from django.db import models

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+') # null=True, related_name='+' means that the reverse relationship is not required

class Product(models.Model):
    title = models.CharField(max_length=255) # max_length is the maximum number of characters in the field
    description = models.TextField(blank=True) # blank=True means that the field is optional
    price = models.DecimalField(max_digits=6, decimal_places=2) # max_digits is the maximum number of digits in the field, decimal_places is the number of decimal places
    inventory = models.IntegerField(default=0) # default=0 means that the field will be set to 0 by default
    last_update = models.DateTimeField(auto_now=True) # auto_now=True means that the field will be set to the current date and time whenever the model is saved
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT) # on_delete=models.PROTECT means that the product will not be deleted if the collection is deleted
    promotions = models.ManyToManyField(
    Promotion, blank=True) # blank=True means that the field is optional. 
    # ManyToManyField means that there can be many products in a collection, and there can be many collections in a product.

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
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT) # on_delete=models.PROTECT means that the order will not be deleted if the customer is deleted

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT) # on_delete=models.PROTECT means that the order item will not be deleted if the order is deleted
    product = models.ForeignKey(Product, on_delete=models.PROTECT) # on_delete=models.PROTECT means that the order item will not be deleted if the product is deleted
    quantity = models.PositiveSmallIntegerField() # PositiveSmallIntegerField means that the field will be set to a positive integer
    unit_price = models.DecimalField(max_digits=6, decimal_places=2) # max_digits is the maximum number of digits in the field, decimal_places is the number of decimal places


class Address(models.Model):
    street = models.CharField(max_length=255) # max_length is the maximum number of characters in the field
    city = models.CharField(max_length=255) # max_length is the maximum number of characters in the field
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) # on_delete=models.CASCADE means that the customer will be deleted whenever the address is deleted


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True means that the field will be set to the current date and time whenever the model is saved


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) # on_delete=models.CASCADE means that the cart item will be deleted whenever the cart is deleted
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # on_delete=models.CASCADE means that the cart item will be deleted whenever the product is deleted
    quantity = models.PositiveSmallIntegerField() # PositiveSmallIntegerField means that the field will be set to a positive integer
    
 