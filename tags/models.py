from django.db import models
from django.contrib.contenttypes.models import ContentType # for generic foreign key to content type model (e.g. product)
from django.contrib.contenttypes.fields import GenericForeignKey # for generic foreign key to content type model (e.g. product)

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) # on_delete=models.CASCADE means that the tagged item will be deleted if the content type is deleted (e.g. product) or if the content type is deleted (e.g. product)
    object_id = models.PositiveIntegerField() # PositiveIntegerField means that the field will be set to a positive integer
    content_object = GenericForeignKey() # GenericForeignKey is a generic foreign key to content type model (e.g. product)
    