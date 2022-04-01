from celery import shared_task
from product.models import Product
from django.utils import timezone
from datetime import timedelta


@shared_task
def check_active_products():
    startdate = timezone.now()
    enddate = startdate - timedelta(days=30)
    products = Product.objects.filter(user_id__is_market=False, updated_at__lte=enddate)
    for product in products:
        product.is_active = False
        product.save()
