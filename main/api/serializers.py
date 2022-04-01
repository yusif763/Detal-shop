from django.db import models
from django.db.models import fields
from django.db.models.aggregates import Avg
from rest_framework import permissions
from main.models import Contact, Marka, Modell, WishList
from product.models import Product
from account.models import Rating, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = (
            'id',
            'name',
            'phone_number',
        )


class WishListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WishList
        fields = (
            'id',
            'user',
            'product',
        )
        

class MainPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marka
        fields = (
            'id',
            'slug',
            'title',
        )


class MainPageModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Modell
        fields = (
            'id',
            'slug',
            'title',
            'is_parent',
        )


class FilteredProductSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()

    class Meta:
        model = Product

        fields = (
            'id',
            'user_id',
            'title',
            'price',
            'description',
            'vin_code',
            'main_image',
            'discount',
        )
            
class ProductSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Product
        permisson_classes = [permissions.IsAuthenticated]

        fields = (
            'id',
            'user',
            'title',
            'price',
            'description',
            'vin_code',
            'main_image',
            'discount',   
            'is_active',
        )
    
    def get_user(self, obj):
        return obj.user_id.first_name

class UserRatingSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'avg_rating',
        )
    
    def get_avg_rating(self, obj):
        return Rating.objects.filter(rated_user=obj).aggregate(Avg('rating'))['rating__avg']
    