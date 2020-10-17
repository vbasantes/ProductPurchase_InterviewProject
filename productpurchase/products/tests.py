from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from .models import Product
from .serializers import ProductSerializer
from .views import ProductsViewSet
from django.contrib.auth.models import User


class BaseApiTest(APITestCase):
    client = APIClient()
    factory = APIRequestFactory()

    def setUp(self):
        self.superuser = User.objects.create_superuser('admin', 'admin@admin.com', 'password')
        self.client.login(username='username', password='password') 


class CreateProductTest(BaseApiTest):

    def setUp(self):
        super().setUp()

    def test_create_product(self):        
        """
        This test ensures that a new product can be created
        """       
        view = ProductsViewSet.as_view({'post': 'create'})
        request = self.factory.post('/products/', {'name': 'NewCar'}, format='json')       
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)       


class GetAllProductsTest(BaseApiTest):

    def setUp(self):
        super().setUp()

        # add test product data
        Product.objects.create(name='Car')
        Product.objects.create(name='Monitor')

    def test_get_all_products(self):
        """
        This test ensures that all products added in the setUp method
        exist when we make a GET request to the products/ endpoint
        """
        # hit the API endpoint
        view = ProductsViewSet.as_view({'get': 'list'})
        request = self.factory.get('/products/')        
        response = view(request)

        # fetch the data from db
        expected = Product.objects.all()
        serialized = ProductSerializer(expected, many=True)

        # compare data from db to response data        
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)