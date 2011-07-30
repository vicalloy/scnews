#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.db import models

class Resource(models.Model):
    type = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    site_url = models.URLField()
    res_url = models.URLField()
    interval = models.IntegerField()#seconds
    descn = models.TextField(blank=True, default='')
    updated_on = models.DateTimeField(blank=True, null=True)
    feed_updated = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Topic(models.Model):
    res = models.ForeignKey(Resource)
    title = models.CharField(max_length=999)
    link = models.URLField()#idx
    author = models.CharField(max_length=64)
    date = models.DateTimeField(blank=True, null=True)
    descn = models.TextField(blank=True, default='')
