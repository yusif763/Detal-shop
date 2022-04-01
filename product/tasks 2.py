from celery import shared_task
from product.models import Product
from django.utils import timezone
from datetime import timedelta


@shared_task
def check_active_products():
    startdate = timezone.now()
    enddate = startdate - timedelta(days=14)
    products = Product.objects.filter(updated_at__lte=enddate)
    for product in products:
      d
        product.save()
