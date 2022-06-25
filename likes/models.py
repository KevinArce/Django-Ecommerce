from django.db import models
from django.contrib.auth.models import User # for generic foreign key to user model (e.g. user)
from django.contrib.contenttypes.models import ContentType # for generic foreign key to content type model (e.g. product) 
from django.contrib.contenttypes.fields import GenericForeignKey # for generic foreign key to content type model (e.g. product) (e.g. product) 

class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete=models.CASCADE means that the liked item will be deleted if the user is deleted
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) # on_delete=models.CASCADE means that the liked item will be deleted if the content type is deleted (e.g. product) or if the content type is deleted (e.g. product)
    object_id = models.PositiveIntegerField() # PositiveIntegerField means that the field will be set to a positive integer
    content_object = GenericForeignKey() # GenericForeignKey is a generic foreign key to content type model (e.g. product)

    