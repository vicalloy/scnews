#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.shortcuts import render

from models import Topic

def index(request, template_name="scnews/index.html"):
    ctx = {}
    ctx['topics'] = Topic.objects.all().order_by('-date').select_related()
    return render(request, template_name, ctx)
