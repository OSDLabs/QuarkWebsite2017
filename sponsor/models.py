from django.db import models

SPONS = (
    (u'Our Sponsors',u'Our Sponsors'),
    (u'Our Media Partners',u'Our Media Partners'),
    (u'Our Associations',u'Our Associations'),
    )

class Sponsor(models.Model):
    order = models.IntegerField()
    desc = models.CharField(max_length=200, blank = True, null=True)
    link = models.CharField(max_length=100)
    img = models.ImageField(upload_to = "adminuploads/sponsors/")
    types = models.CharField(max_length=100, choices=SPONS)

class FoodFest(models.Model):
    order = models.IntegerField()
    desc = models.CharField(max_length=200, blank = True, null=True)
    link = models.CharField(max_length=100)
    img = models.ImageField(upload_to = "adminuploads/sponsors/")