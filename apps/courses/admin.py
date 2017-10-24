from __future__ import absolute_import
from django.contrib import admin
from django import forms

from . models import Course

admin.site.register(Course)
