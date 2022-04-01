from django.contrib import admin
from main.models import *
from product.models import Category, Product,Image

# admin.site.register(Tours)
admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(Image)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user_id','slug')