# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from paulscabins.models import Testimonial, PhotoUpload

# Register your models here.
admin.site.register(Testimonial)
admin.site.register(PhotoUpload)