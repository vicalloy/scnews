#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.contrib import admin

from models import Resource, Topic

class ResourceAdmin(admin.ModelAdmin):
    list_display        = ('type', 'name', 'interval', 'updated_on', 'feed_updated',)

class TopicAdmin(admin.ModelAdmin):
    list_display        = ('res', 'title', 'link', 'author', 'date',)

admin.site.register(Resource, ResourceAdmin)
admin.site.register(Topic, TopicAdmin)
