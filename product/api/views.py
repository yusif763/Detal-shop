import re
from product.models import *
from main.models import *
from account.models import *
from django.db.models.base import Model
from product.api.serializers import CategorySerializer, CitySerializer, ProductCreateSerializer,ImageSeriazlier,ModellSerializer,MarkaSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from django.http import Http404
from django.db.models import Q
from product.models import Image
from rest_framework.permissions import IsAuthenticated
from main.api.serializers import MainPageModelSerializer,MainPageSerializer






class CityAPIView(APIView):

    def get(self, request, format=None):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class CreatePoruct(APIView):

    def post(self,request,*args,**kwargs):
        # permission_classes = [IsAuthenticated]
        # permission_classes = [is]
        product_data = request.data 
        product_data['user_id'] = request.user.id
        serializer = ProductCreateSerializer(data = product_data, context = {'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data,'yoooooooooo')
        images_data = product_data.pop('image')
        product = Product.objects.filter(id = serializer.data['id'])[0]
        if product.title_az:
            product.title_en = product.title_az
            product.title_ru = product.title_az
        elif product.title_ru:
            product.title_en = product.title_ru
            product.title_az = product.title_ru
        else:
            product.title_az = product.title_en
            product.title_ru = product.title_en
        product.save()
        
        for image_data in images_data:
            image = Image.objects.create(product=product, image = image_data)
            image.save()
        # for i in product_data['image']:
        #     image = Image.objects.create(product = product,image=i)

        # imageserializer = ImageSeriazlier(product_data['image'],many=True)
        # imageserializer.is_valid(raise_exception=True)
        # imageserializer.save(product = product)
        message = {'success': True,
                       'message': 'Elanınız əlave edildi baxış keçirildikdən sonra şərh ediləcəkdir'}
        return Response(message, status=status.HTTP_201_CREATED)




class ProductDetail(APIView):
    def put(self, request, slug):
        product = Product.objects.get(slug=slug)
        product_data = request.data 
        product_data._mutable = True
        product_data['user_id'] = request.user.id
        product_data['main_image'] = product.main_image
        product_data._mutable = False
        # print(product_data,"qqqqqqqlqkqkwkfjswjknfkwkjfwwekjnfewfjknef")
        serializer = ProductCreateSerializer(instance=product, data=product_data , context={'request': request})
        if serializer.is_valid():
            serializer.save()

            product_data._mutable = True
            for  i in product_data:
                if i == 'image':
                    # print(product_data,'gorek nolurdaaa')
                    images_data = product_data.pop('image')
                    print(images_data,'salaaaaam')
                    for image_data in images_data:
                        image = Image.objects.create(product=product, image = image_data)
                        image.save()
                    break
            product_data._mutable = False
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # for image_data in images_data:
        #     image = Image.objects.create(product=product, image = image_data)
        #     image.save()

    #  def delete(self, request, pk):
    #     product = Product.objects.get(pk=pk)
    #     product.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)



class CategoryApiView(APIView):
    def get(self,request,*args,**kwargs):
        categories = Category.objects.filter(is_parent = True)
        serializer = CategorySerializer(categories,many=True, context = {"request":request})
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        category_data = request.data
        category = Category.objects.filter(id =category_data['category_id'])[0]
        serializer = CategorySerializer(category,context={"request":request})
        print(serializer.data)
        return Response(serializer.data,status=status.HTTP_200_OK)



class AddProductMarkaAPIView(APIView):

     def get(self, request, format=None):
        markas = Marka.objects.all()
        print(markas)
        serializer = MainPageSerializer(markas, many=True)

        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddProductModelAPIView(APIView):

    def post(self, request, *args, **kwargs):

        marka_id = request.data['marka_id']
        models = Modell.objects.filter(marka_id=marka_id,is_parent=False)

        serializer = MainPageModelSerializer(models, many=True)

        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
