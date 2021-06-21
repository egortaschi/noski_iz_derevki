from decimal import Decimal
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from .models import Category, Socks, CartProduct, Cart, Customer
from django.core.files.uploadedfile import SimpleUploadedFile
from .views import recalc_cart, AddToCartView, BaseView
from unittest import mock


User = get_user_model()

class ShopTestCases(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.category = Category.objects.create(name='Носки', slug='socks')
        image = SimpleUploadedFile("socks_image.jpg", content=b'', content_type="image/jpg")
        self.socks = Socks.objects.create(
            category=self.category,
            title="Test Socks",
            slug="test-slug",
            image=image,
            price=Decimal('500.00'),
            size="42-45",
            material="100% wool",

        )
        self.customer = Customer.objects.create(user=self.user, phone="111111", address="Adres")
        self.cart = Cart.objects.create(owner=self.customer)
        self.cart_product = CartProduct.objects.create(
            user=self.customer,
            cart=self.cart,
            content_object=self.socks
        )

    def test_add_to_cart(self):
        self.cart.products.add(self.cart_product)
        recalc_cart(self.cart)
        self.assertIn(self.cart_product, self.cart.products.all())
        self.assertEqual(self.cart.products.count(), 1)
        self.assertEqual(self.cart.final_price, Decimal("500.00"))

    def test_response_from_add_to_cart_view(self):
        factory = RequestFactory()
        request = factory.get('')
        request.user = self.user
        response = AddToCartView.as_view()(request, ct_model="socks", slug="test-slug")
        # response = client.get('add-to-cart/socks/test-slug')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/cart/')

    def test_mock_homepage(self):
        mock_data = mock.Mock(status_code=444)
        with mock.patch('catalog.views.BaseView.get', return_value=mock_data) as mock_data:
            factory = RequestFactory()
            request = factory.get('')
            request.user = self.user
            response = BaseView.as_view()(request)
            self.assertEqual(response.status_code, 444)



