from django.db import models
from django.db.models.base import Model
from django.db.models.fields import related
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from tools.slug_generator import slugify
from datetime import datetime
from main.models import *


User = get_user_model()


class Category(models.Model):

    parent_category = models.ForeignKey('self', verbose_name='Parent Category', on_delete=models.CASCADE, db_index=True,
                                        related_name='sub_categories', blank=True, null=True)

    title = models.CharField(_('Title'), max_length=120,null=True,blank=True)
    image = models.ImageField(
        _("Image"), upload_to='product_image', null=True, blank=True)
    category_order = models.IntegerField(
        _("Category Order"), null=True, blank=True)
    slug = models.SlugField(('slug'), max_length=255,
                            editable=False, unique=True)
    is_parent = models.BooleanField(_("Is Parent"), default=False)
    is_box_category = models.BooleanField(
        _("Is Box Category"), default=False, null=True, blank=True)
    is_long_box_category = models.BooleanField(
        _("Is Long Box Category"), default=False, null=True, blank=True)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        # ordering = ('-created_at', '-title')

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):

        title = self.title
        self.slug = f"{slugify(self.title)}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        super().save()

# Create your models here.


class Product(models.Model):

    # relation's
    user_id = models.ForeignKey(User, verbose_name="User",
                                on_delete=models.CASCADE, db_index=True, related_name="user_product")
    marka_id = models.ForeignKey('main.Marka', verbose_name="Marka",
                                 on_delete=models.CASCADE, db_index=True, related_name="marka_product")
    modell_id = models.ForeignKey('main.Modell', verbose_name="Modell",
                                  on_delete=models.CASCADE, db_index=True, related_name="model_product")
    category_id = models.ForeignKey(Category, verbose_name=_("Category"),
                                    on_delete=models.CASCADE, db_index=True, related_name="category_product")
    city = models.ForeignKey(
        'City', verbose_name='City', on_delete=models.CASCADE, related_name='category_city',null=True,blank=True)

    title = models.CharField(_('Title'), max_length=120)
    description = models.TextField(_("Description"), null=True, blank=True)
    vin_code = models.CharField(
        _("Vin code"), max_length=120, null=True, blank=True)
    price = models.DecimalField(_('Qiymet'), max_digits=8, decimal_places=2)
    discount = models.IntegerField(
        _('Discount Percentage'), null=True, blank=True)
    main_image = models.ImageField(
        _("Main Image"), upload_to='product_image', null=True, blank=True)
    slug = models.SlugField(('slug'), max_length=255,
                            editable=False, unique=True)
    is_discount = models.BooleanField(_("Is Discount"), default=False)
    year = models.IntegerField(_('Year'))
    is_active = models.BooleanField(_('Is_active'), default=False)
    is_vip = models.BooleanField(_('Is Vip'), default=False)
    is_new =models.BooleanField(_("Is New"), default=False)

    
    watch_count = models.IntegerField(_("Watch Count"), default=0)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        # ordering = ('-created_at', '-title')

    def __str__(self):
        return f"{self.title}"

    @property
    def endirim(self):
        if self.discount:
            son_qiymet = self.price - (self.price * self.discount)/100
            return round(son_qiymet, 2)

    def save(self, *args, **kwargs):

        title = self.title

    #moderations
        self.slug = f"{slugify(self.title)}-{self.created_at}"
        super().save()

    # def get_absolute_url(self):
    #     return reverse_lazy('tours:tour-detail', kwargs={'slug': self.slug})


class Image(models.Model):

    # relation's
    product = models.ForeignKey(Product, verbose_name="Product",
                                on_delete=models.CASCADE, db_index=True, related_name="product_image")

    image = models.ImageField(_('Image'), upload_to='product_image')
    is_main = models.BooleanField(_("Is Main"), default=False)

    class Meta():
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        # ordering = ('-created_at', '-title')

    def __str__(self):
        return f"{self.image}"


class City(models.Model):

    # information
    name = models.CharField('Name', max_length=40)
    slug = models.SlugField('slug', max_length=255,
                            editable=False, unique=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        name = self.name
        self.slug = f"{slugify(self.name)}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        super().save()

    # def get_absolute_url(self):
    #     return reverse_lazy('main:city-detail', kwargs={'slug': self.slug})
