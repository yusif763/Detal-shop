from typing import List
from django.core import paginator
from django.db import models
from django.shortcuts import render, redirect
from django.utils import translation
from main.models import *
from django.views.generic import TemplateView, CreateView, FormView
from django.views.generic import (
    ListView, DetailView
)
from main.forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from product.models import Category, Product
from django.db.models import Q
from django.core.paginator import EmptyPage, Paginator


# class SafePaginator(Paginator):
#     def validate_number(self, number):
#         try:
#             return super(SafePaginator, self).validate_number(number)
#         except EmptyPage:
#             if number > 1:
#                 return self.num_pages
#             else:
#                 raise EmptyPage(
#                     'That page contains no results'
#                 )

# Create your views here.


class SafePaginator(Paginator):
    def validate_number(self, number):
        try:
            return super(SafePaginator, self).validate_number(number)
        except EmptyPage:
            if number > 1:
                return self.num_pages
            else:
                raise EmptyPage(
                    'That page contains no results'
                )


class HomePageView(ListView):
    model = Marka
    template_name = 'lastindex.html'
    context_object_name = 'markalar'

    def get_markalar(self):
        markalar = Marka.objects.all().order_by('-created_at')[:8]
        return markalar

    def get_vip(self):
        vip = Product.objects.filter(is_vip=True).order_by('-created_at')[:8]
        return vip

    def get_sale_products(self):
        sale_products = Product.objects.filter(is_discount=True)
        return sale_products
    
    def get_products(self):
        all_products = Product.objects.all().order_by('-created_at')
        return all_products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reklamlar = Advertisements.objects.filter(pages ='Main Page')
        if self.request.user.is_authenticated: 
            wishlists = WishList.objects.filter(user= self.request.user)
            wish_products = [] 
            for i in wishlists:
                title = i.product.title
                wish_products.append(title)
            context['wishes'] = wish_products
        context['reklamlar'] = reklamlar
        context['markalar'] = self.get_markalar()
        context['vip'] = self.get_vip()
        context['products'] = self.get_products()
        context['box_categories'] = Category.objects.filter(
            is_box_category=True)
        context['long_box_categories'] = Category.objects.filter(
            is_long_box_category=True)
        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reklamlar = Advertisements.objects.filter(pages ='About Page')
        context['reklamlar'] = reklamlar
        return context


class AllBrandsView(ListView):
    model = Marka
    template_name = 'all-brands.html'
    context_object_name = 'markalar'
    queryset = Marka.objects.all().order_by('-created_at')
    paginate_by = 16

    # def get_markalar(self):
    #     markalar = Marka.objects.all().order_by('-created_at')
    #     return markalar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['markalar'] = self.get_markalar()
        reklamlar = Advertisements.objects.filter(pages ='All Brands Page')
        context['reklamlar'] = reklamlar
        return context


class BrandsView(DetailView):
    model = Marka
    template_name = 'brands.html'
    context_object_name = 'marka'

    def get_success_url(self, **kwargs):
        return reverse_lazy('main:brands', kwargs={'slug': self.object.slug})

    def get_modeller(self):
        print(self.object.id, 'buradi')
        marka = Marka.objects.get(slug=self.kwargs.get('slug'))
        modeller = Modell.objects.filter(marka_id=marka.id)
        return modeller

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modeller'] = self.get_modeller()
        reklamlar = Advertisements.objects.filter(pages ='All Models Page')
        context['reklamlar'] = reklamlar
        return context


class CarDetailView(ListView):
    model = Marka
    template_name = 'car_detail.html'
    context_object_name = 'main_categories'

    # def get_success_url(self , **kwargs):
    #     return reverse_lazy('main:car-detail' , kwargs = {'slug': self.marka_slug, "model_slug":self.marka_model.model_slug})

    def get_main_categories(self):
        main_categories = Category.objects.filter(is_parent=True).order_by("category_order")
        return main_categories

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(self.kwargs.get['slug'],'salam')
        context['marka'] = self.kwargs.get('marka_slug')
        context['model'] = self.kwargs.get('model_slug')
        context['main_categories'] = self.get_main_categories()
        reklamlar = Advertisements.objects.filter(pages ='Car Detail Page')
        context['reklamlar'] = reklamlar
        return context


class CarFilterView(TemplateView):
    template_name = 'car-filter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reklamlar = Advertisements.objects.filter(pages ='Car Filter Page')
        context['reklamlar'] = reklamlar
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reklamlar = Advertisements.objects.filter(pages ='Contact Page')
        context['reklamlar'] = reklamlar
        return context


class InnerDetailView(ListView):
    template_name = 'inner-details.html'
    model = Category

    # def get_success_url(self , **kwargs):
    #     return reverse_lazy('main:sub-parts' , kwargs = {'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs.get('subparent_detail_slug'), 'ididi')
        context['model'] = self.kwargs.get('model_slug')
        context['marka'] = self.kwargs.get('marka_slug')
        context['parent_detail'] = self.kwargs.get('parent_detail_slug')
        context['subparent_detail'] = self.kwargs.get('subparent_detail_slug')
        parent_cat = Category.objects.filter(
            slug=self.kwargs.get('subparent_detail_slug'))[0]
        context['parent_cat'] = parent_cat
        context["parts"] = Category.objects.filter(
            parent_category=parent_cat.id).all().order_by('category_order')

        reklamlar = Advertisements.objects.filter(pages ='Inner Details Page')
        context['reklamlar'] = reklamlar

        return context


class ShopsView(ListView):
    template_name = 'shops.html'
    model = User
    queryset = User.objects.filter(is_market=True)
    context_object_name = 'shops'
    paginate_by = 16


class ShopDetailView(ListView):
    model = Product
    template_name = 'shop-detail.html'
    context_object_name = 'products'
    paginate_by = 4
    paginator_class = SafePaginator

    def get_queryset(self, **kwargs):
        return Product.objects.filter(
            user_id__slug=self.kwargs.get('slug')).all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shops"] = User.objects.filter(is_market=True).all()
        reklamlar = Advertisements.objects.filter(pages ='Shops Page')
        context['reklamlar'] = reklamlar

        return context


class SubParts(ListView):
    template_name = 'sub_parts.html'
    model = Category

    # def get_success_url(self , **kwargs):
    #     return reverse_lazy('main:sub-parts' , kwargs = {'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(self.kwargs.get('detail_slug'),'ididi')
        parent_cat = Category.objects.filter(
            slug=self.kwargs.get('parent_detail_slug'))[0]
        context['model'] = self.kwargs.get('model_slug')
        context['marka'] = self.kwargs.get('marka_slug')
        context['parent_detail'] = self.kwargs.get('parent_detail_slug')
        context["subparts"] = Category.objects.filter(
            parent_category=parent_cat.id).all()
        reklamlar = Advertisements.objects.filter(pages ='Sub Parts Page')
        context['reklamlar'] = reklamlar
            

        return context


class SinglePageView(TemplateView):
    template_name = 'singlepage.html'


class WishlistPageView(TemplateView):
    template_name = 'wishlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        wishlists = WishList.objects.filter(user=self.request.user).all()
        print(wishlists)
        context['wishes'] = wishlists
        reklamlar = Advertisements.objects.filter(pages ='Wish List Page')
        context['reklamlar'] = reklamlar
        return context


class SearchedProdsView(ListView):
    template_name = 'searched-products.html'
    model = Product
    paginate_by = 16

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        marka_id = self.request.GET.get('marka')
        model_id = self.request.GET.get('modell')
        years = self.request.GET.get('year')
        banCode = self.request.GET.get('ban_nomresi')
        searchValue = self.request.GET.get('search_value')
        reklamlar = Advertisements.objects.filter(pages ='Searched Products')
        context['reklamlar'] = reklamlar

        if banCode:
            products = Product.objects.filter(
                vin_code=banCode).order_by('-created_at')

        elif marka_id and model_id and searchValue:
            products = Product.objects.filter(
                marka_id=marka_id, modell_id=model_id, title__icontains=searchValue).order_by('-created_at')

        elif marka_id and model_id and years:
            products = Product.objects.filter(
                marka_id__slug=marka_id, modell_id__slug=model_id, year=years).order_by('-created_at')

        elif marka_id and model_id:
            products = Product.objects.filter(
                marka_id__slug=marka_id, modell_id__slug=model_id).order_by('-created_at')

        elif marka_id:
            products = Product.objects.filter(
                marka_id__slug=marka_id).order_by('-created_at')

        elif searchValue:
            products = Product.objects.filter(
                title__icontains=searchValue).order_by('-created_at')

        else:
            products = Product.objects.filter(
                marka_id=marka_id).order_by('-created_at')
        page = self.request.GET.get(
            'page', 1) if self.request.GET.get('page', 1) != '' else 1

        if products:
            paginator = Paginator(products, self.paginate_by)

            results = paginator.page(page)
            print(results, 'hahahaha')
            index = results.number - 1
            max_index = len(paginator.page_range)
            start_index = index - 5 if index >= 5 else 0
            end_index = index + 5 if index <= max_index - 5 else max_index
            context['page_range'] = list(paginator.page_range)[
                start_index:end_index]

            context['products'] = results

        return context


def change_language(request):
    if request.GET.get('lang') == 'en' or request.GET.get('lang') == 'az' or request.GET.get('lang') == 'ru':
        translation.activate(request.GET.get('lang'))
        response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        response.set_cookie('django_language', request.GET['lang'])
        return response
