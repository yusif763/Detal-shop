from django.db import models
from django.db.models import fields
from main.models import Contact, Marka, Modell, WishList
from product.models import Category, City, Image, Product
from rest_framework import serializers
from main.models import Marka,Modell
from django.contrib.auth import  get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class MarkaSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Marka

        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = City

        fields = '__all__'

class ModellSerializer(serializers.ModelSerializer):
    marka_id = MarkaSerializer()
    models = serializers.SerializerMethodField()
    
    class Meta:
        model = Modell

        fields = (
            'id',
            'title',
            'image',
            'marka_id',
            'models'
        )

    def get_models(self,obj):
        models = obj.sub_models.all()
        return ModellSerializer(models, many = True)


class ImageSeriazlier(serializers.ModelSerializer):

    class Meta:
        model = Image

        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer()
    # marka_id = MarkaSerializer()
    # modell_id = ModellSerializer()
    image = ImageSeriazlier(many=True, read_only=True)
    class Meta:
        model = Product

        fields = (
            'id',
            'user_id',
            'marka_id',
            'modell_id',
            'title',
            'vin_code',
            'price',
            'image',
            'created_at',
            'updated_at',
            "main_image",
            'year',
            'category_id',
            'is_new',
            'city',
        )

    # def get_image(self,obj):
    #     image = obj.product_image.all()
    #     # reply = Comment.objects.get_or_create(=obj)
    #     return ImageSeriazlier(image, many =True).data

    # def create(self, validated_data):
    #     print(validated_data,'imagessssssss')
    #     images_data = validated_data.pop('image')
    #     product = Product.objects.create(**validated_data)
    #     for image_data in images_data:
    #         Image.objects.create(product=product, **image_data)
    #     return product



class CategorySerializer(serializers.ModelSerializer):
    sub_categories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'sub_categories'
        ]

    def get_sub_categories(self,obj):
        subs = obj.sub_categories.all()
        return CategorySerializer(subs,many=True).data


