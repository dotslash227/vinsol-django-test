from django.db import models
from django.utils import timezone
from products.models import Deal
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    additional_discount = models.FloatField(default=0.00)
    final_price = models.FloatField(default=0.00)
    confirmed = models.CharField(max_length=10, default="No")

    def __str__(self):
        return "Deal bought by %s with user id %s of %s" % (self.user, self.user.pk, self.deal)
