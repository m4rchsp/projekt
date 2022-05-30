from django.db import models

# Create your models here.

class Item(models.Model):
    type = models.CharField(max_length=30) # 'badge',
    classe = models.CharField(max_length=30) # 'badges',
    name = models.CharField(max_length=30) #  'èlève',
    shortname = models.CharField(max_length=30) # 'bdeleve',
    keyname = models.CharField(max_length=30) #  'bdel1',
    description = models.CharField(max_length=30) # 'Badge d\'èlève',
    image = models.CharField(max_length=120, default='') # 'eleve_badge.png',
    image_thumb = models.CharField(max_length=120, default='') # 'eleve_badge_thumb.png',
    limit = models.IntegerField() # ': 1,
    stack = models.IntegerField() # ': 1,
    obs_1 = models.TextField() # 'Medal d\'èlève.',
    obs_2 = models.TextField() # '1ère medail',
    status = models.CharField(max_length=10, default='inactive') # active /

