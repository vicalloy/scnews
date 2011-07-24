#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='scnews_index'),
)
