# Product manager Job
from django_extensions.management.jobs import DailyJob
from products.models import Deal
from django.utils import timezone

class Job(DailyJob):
    help = "deals publisher and unpublisher"

    def execute(self):
        deal = Deal.objects.get(is_published=True)
        try:
            next_deal = Deal.objects.filter(published_date=timezone.now())[0]
        except:
            print ("no deals found for today")
        else:
            print (next_deal)                        
            deal.is_published = False
            deal.save()
            next_deal.is_published = True
            next_deal.save()            