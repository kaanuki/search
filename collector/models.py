import hashlib
from django.db import models
from django.conf import settings


class Collection(models.Model):

    slug = models.CharField(max_length=256, unique=True)
    title = models.CharField(max_length=2048, blank=True)

    users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.slug


class Document(models.Model):

    slug = models.CharField(max_length=256, unique=True)
    title = models.CharField(max_length=2048, blank=True)
    url = models.URLField(max_length=2048)
    text_url = models.URLField(max_length=2048)
    indexed = models.BooleanField(default=False)
    index_time = models.DateTimeField(null=True, blank=True)

    collection = models.ForeignKey('Collection')

    def __unicode__(self):
        return self.slug
