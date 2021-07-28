from django.urls import path
from .api_views import CategoryListAPIView, SocksListAPIView


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('socks/', SocksListAPIView.as_view(), name='socks'),
]