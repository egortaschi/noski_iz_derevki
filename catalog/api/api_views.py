from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from .serializers import CategorySerializer, SocksSerializer
from ..models import Category, Socks


class CategoryListAPIView(ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SocksListAPIView(ListAPIView):

    serializer_class = SocksSerializer
    queryset = Socks.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']
