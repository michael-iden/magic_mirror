from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Weather(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
