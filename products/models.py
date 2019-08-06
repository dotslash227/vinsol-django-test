from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Deal(models.Model):
    date_added = models.DateField(default=timezone.now)
    is_published = models.BooleanField(choices=(
        (True, "Yes"),
        (False, "No")
    ), default=False)
    published_date = models.DateField(default=None)
    title = models.CharField(max_length=100)
    description = models.TextField(default="Add some description")
    price = models.FloatField(default=0)
    discounted_price = models.FloatField(default=0)
    quantity = models.IntegerField(default=10)    
    image = models.FileField(upload_to="deals", max_length=150, default=None)

    def __str__(self):
        return self.title
