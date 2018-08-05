# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=140, null=True)
    comment = models.TextField(null=False)
    date = models.DateField(auto_now_add=True, null=True) # probably just date is fine.
    picture = models.ImageField(upload_to='cabinuploads', default='cabinuploads/default.jpg')


class PhotoUpload(models.Model):
    name = models.CharField(max_length=140, null=True)
    date = models.DateField(auto_now_add=True, null=True) # probably just date is fine.
    picture = models.ImageField(upload_to='ronsuploads', default='ronsuploads/default.jpg')
