from rest_framework import serializers
from ..models import Category, Socks


class CategorySerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'slug'
        ]


class BaseProductSerializer:

    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects)
    title = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    image = serializers.ImageField(required=True)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=9, decimal_places=2, required=True)



class SocksSerializer(BaseProductSerializer, serializers.ModelSerializer):

    size = serializers.CharField(required=True)
    material = serializers.CharField(required=True)
    color_scheme = serializers.CharField(required=True)
    gender = serializers.CharField(required=True)

    class Meta:
        model = Socks
        fields = '__all__'
