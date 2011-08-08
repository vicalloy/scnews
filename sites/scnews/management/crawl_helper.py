#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#rss
#http://bbs.weiphone.com/rss-htm-fid-29.html
#http://bbs.gfan.com/rss.php?fid=23&auth=0
#http://bbs.fengbao.com/forum.php?mod=rss&fid=142
#http://bbs.maxpda.com/rss.php?fid=44&auth=0
#html
#http://bbs.hiapk.com/forumdisplay.php?fid=187&filter=type&orderby=dateline&typeid=201

#第一步，将所有数据都抓回来
#只显示标题
#第二部，增加搜索
#仿照google rss reader增加快速展开功能
#第三部，增加数据分析，加tag等处理
#from scnews.models import Topic
from datetime import datetime
from time import mktime

import feedparser

from scnews.models import Topic

def __fmt_rss_date(dt):
    return datetime.fromtimestamp(mktime(dt))

def __fetch_rss(res):
    d = feedparser.parse(res.res_url)
    for e in  d.entries:
        if Topic.objects.filter(link=e.link).count():#if exist
            continue
        date = __fmt_rss_date(e.date_parsed)
        #if res.feed_updated and res.feed_updated > date:
        #    break
        t = Topic(res=res,
                title = e.title,
                link = e.link,
                author = e.author,
                descn = e.description,
                date = date,
                )
        t.save()
    #res.feed_updated = __fmt_rss_date(d.feed.updated_parsed)

def fetch(res):
    if res.type == 'rss':
        __fetch_rss(res)
    res.updated_on = datetime.now()
    res.save()
