from django.db import models

from . import choices

class Party(models.Model):
    title = models.CharField(null=True, blank=True, default="", max_length=100)
    who = models.TextField(null=True, blank=True, default="", max_length=300)
    what = models.TextField(null=True, blank=True, default="", max_length=300)
    why = models.TextField(null=True, blank=True, default="", max_length=500)

    def __str__(self):
        return self.title


class Member(models.Model):
    party = models.ForeignKey('Party', related_name='p', on_delete=models.CASCADE)
    name = models.CharField(null=True, blank=True, default="", max_length=100)
    race = models.CharField(null=True, blank=True, default="", max_length=100)
    dndclass = models.CharField(null=True, blank=True, default="", max_length=100)
    icon = models.CharField(max_length=50,choices=choices.icon,default="1")
    theme = models.CharField(max_length=50,choices=choices.theme,default="1")
    specialty = models.CharField(null=True, blank=True, default="", max_length=100)
    title = models.CharField(null=True, blank=True, default="", max_length=100)
    interests = models.CharField(null=True, blank=True, default="", max_length=100)
    bio = models.TextField(null=True, blank=True, default="", max_length=300)

    def __str__(self):
        return self.name
