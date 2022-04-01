from django.db.models.base import Model
from main.api.serializers import ContactSerializer, MainPageSerializer, ProductSerializer, UserRatingSerializer , WishListSerializer,MainPageModelSerializer, FilteredProductSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from main.models import Contact, Modell, WishList, Marka
from product.models import Product
from rest_framework.response import Response
from rest_framework import serializers, status
from django.http import Http404
from django.db.models import Q
from account.models import Rating, User


class ContactAPIView(CreateAPIView):
    serializer_class = ContactSerializer
    model = Contact

    def post(self, request, *args, **kwargs):
        print('0---')
        obj = self.create(request, *args, **kwargs)
        print(obj)

        return obj


class WishlistAPIView(APIView):

    def get(self, request, format=None):
        snippets = WishList.objects.all()
        serializer = WishListSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WishListSerializer(data=request.data)
        if serializer.is_valid():
            print('in post')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        product_id = request.data.get('product')
        print('1----', self)
        obj = WishList.objects.filter(product=product_id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MainPageMarkaAPIView(APIView):

    def get(self, request, format=None):
        markas = Marka.objects.all()
        print(markas)
        serializer = MainPageSerializer(markas, many=True)

        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MainPageModelAPIView(APIView):

    def post(self, request, *args, **kwargs):

        marka_slug = request.data['marka_id']
        print(marka_slug)
        models = Modell.objects.filter(marka_id__slug=marka_slug)

        serializer = MainPageModelSerializer(models, many=True)

        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)




class FilteredProductAPIView(APIView):

    def post(self, request, *args, **kwargs):
        marka_id = request.data['marka_id']
        model_id = request.data['modell_id']
        year = request.data['year']
        searchValue = request.data['search_value']
        banCode = request.data['ban_code']
        # print(marka_id, model_id, year, searchValue, banCode)
        if banCode:
            products = Product.objects.filter(vin_code=banCode)
            
        elif marka_id and model_id and searchValue:
            products = Product.objects.filter(Q(
                marka_id=marka_id) | Q(modell_id=model_id) | Q(title__icontains=searchValue))
            print(products)
        elif searchValue:
            products = Product.objects.filter(title__icontains=searchValue)
            print('searchdan gelen')


        elif marka_id and model_id:
            products = Product.objects.filter(Q(
                marka_id=marka_id) | Q(modell_id=model_id))

        else:
            products = Product.objects.filter(marka_id=marka_id)

        serializer = FilteredProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


        
class ActivateProductAPIView(APIView):
    def get(self,request,*args, **kwargs):
        products = Product.objects.filter(user_id = request.user, is_active = False)
        serializer = ProductSerializer(products , many = True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def post(self,request,*args, **kwargs):
        product_id = request.data['product_id']
        product = Product.objects.get(id = product_id)
        if product.user_id == request.user:
            product.is_active = True
            product.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UserRatingAPIView(APIView):
    def get(self,request,*args, **kwargs):
        slug = self.kwargs['slug']
        user = User.objects.get(slug = slug)
        serializer = UserRatingSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def post(self,request,*args, **kwargs):
        serializer = UserRatingSerializer(data = request.data)
        user_id = request.user.id
        rated_user_id = self.kwargs['slug']
        rating = request.data.get('rating')
        if serializer.is_valid():
            if Rating.objects.filter(user = User.objects.get(id=user_id), rated_user = User.objects.get(slug=rated_user_id)).exists():
                rating_obj = Rating.objects.get(user = User.objects.get(id=user_id), rated_user = User.objects.get(slug=rated_user_id))
                rating_obj.rating = rating
                rating_obj.save()
                return Response(status=status.HTTP_200_OK)
            Rating.objects.create(user = User.objects.get(id=user_id), rated_user = User.objects.get(slug=rated_user_id), rating = rating)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)