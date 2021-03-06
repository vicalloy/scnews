from datetime import datetime

from django.core.management.base import NoArgsCommand

from scnews.models import Resource

from scnews.management.crawl_helper import fetch

class Command(NoArgsCommand):
    help = "do crawl"
    
    def handle_noargs(self, **options):
        reses = Resource.objects.all()
        for res in reses:
            if res.updated_on:
                t = datetime.now() - res.updated_on
                if (t.seconds + t.days * 3600 * 24)< res.interval:
                    continue
            fetch(res)
