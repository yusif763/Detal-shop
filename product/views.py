from main.views import SafePaginator
from django.contrib.auth.models import AnonymousUser
from django.db import models
from django.template.response import TemplateResponse

from product.models import Category, Product
from django.http import request
from django.shortcuts import render,redirect
from main.models import Advertisements, WishList 

from django.views.generic import TemplateView
from django.views.generic import (
    ListView, DetailView
)
from main.models import *
from django.core.paginator import Paginator
from main.views import SafePaginator

class SingleProductView(DetailView):
    model = Product 
    template_name = 'single-product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # user = User.objects.filter(context['object'].user_id)
        context['user'] = context['object'].user_id
        reklamlar = Advertisements.objects.filter(pages ='Single Produt')
        context['reklamlar'] = reklamlar
        product = context['product']
        product.watch_count +=1
        product.save()
        print(product.watch_count,'salaaaam')
        return context


# Create your views here.
class AddProductPageView(TemplateView):
    template_name = 'add-product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reklamlar = Advertisements.objects.filter(pages ='Add Product')
        context['reklamlar'] = reklamlar
        return context



class UpdateProduct(DetailView):
    template_name = 'update-product.html'
    context_object_name = "product"
    model = Product


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reklamlar = Advertisements.objects.filter(pages ='Update Product')
        context['reklamlar'] = reklamlar
        return context

    

   

# class SingleProductView(TemplateView):
#     template_name = 'single-product.html'


class ProductPageView(TemplateView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'all-products'
    paginator_class = SafePaginator
    paginate_by = 2

    def get_products(self):
        all_products = Product.objects.all().order_by('-created_at')
        return all_products


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.get_products()
        reklamlar = Advertisements.objects.filter(pages ='Products Page')
        context['reklamlar'] = reklamlar
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

        if self.request.user.is_authenticated: 
            print('wawawawawawaawaw')
            wishlists = WishList.objects.filter(user= self.request.user)
            print(wishlists)
            wish_products = []
            
            for i in wishlists:
                title = i.product.title
                wish_products.append(title)
            # print(wish_products)
            context['wishes'] = wish_products
        return context



class FilteredProducts(ListView):
    template_name = 'filtered_products.html'
    model = Product
    paginate_by = 16

    # def get_success_url(self , **kwargs):
    #     return reverse_lazy('main:sub-parts' , kwargs = {'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(self.kwargs.get('detail_slug'),'ididi')
        parent_cat = Category.objects.filter(slug = self.kwargs.get('parent_detail_slug'))[0]
        context['model'] = self.kwargs.get('model_slug')
        model = Modell.objects.filter(slug = self.kwargs.get('model_slug'))[0]
        context['marka'] = self.kwargs.get('marka_slug')
        context['parent_detail'] = self.kwargs.get('parent_detail_slug')
        context['subparent_detail'] = self.kwargs.get('subparent_detail_slug')
        context['child_detail'] = self.kwargs.get('child_detail_slug')
        category = Category.objects.filter(slug = self.kwargs.get('child_detail_slug'))[0]
        products = Product.objects.filter(modell_id = model, category_id = category)
        reklamlar = Advertisements.objects.filter(pages ='Filtered Product')
        context['reklamlar'] = reklamlar
        # context["subparts"] = Category.objects.filter(parent_category = parent_cat.id).all()
        

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



class SaleProductPageView(ListView):
    model = Product
    template_name = 'sale-products.html'
    context_object_name = 'sale-products'
    paginate_by = 16

    def get_sale_products(self):
        sale_products = Product.objects.filter(is_discount = True)
        return sale_products


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.get_sale_products()
        

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

        
            context['sale'] = results
        context['sale'] = self.get_sale_products()
        reklamlar = Advertisements.objects.filter(pages ='Sale Product')
        context['reklamlar'] = reklamlar
        return context


