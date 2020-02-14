from django.db import models

class Member(models.Model):
    name = models.CharField(null=True, blank=True, default="", max_length=100)
    race = models.CharField(null=True, blank=True, default="", max_length=100)
    dndclass = models.CharField(null=True, blank=True, default="", max_length=100)
    specialty = models.CharField(null=True, blank=True, default="", max_length=100)
    title = models.CharField(null=True, blank=True, default="", max_length=100)
    interests = models.CharField(null=True, blank=True, default="", max_length=100)
    bio = models.TextField(null=True, blank=True, default="", max_length=300)
