# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Chapter(models.Model):
	topic = models.CharField(max_length=250)
	subtopic = models.CharField(max_length=250)
	picture = models.CharField(max_length=250)

class Formula(models.Model):
	chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
	file_type = models.CharField(max_length=10)
	formula_name = models.CharField(max_length=250)