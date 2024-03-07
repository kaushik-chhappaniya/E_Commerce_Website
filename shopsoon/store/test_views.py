import unittest
from django.test import TestCase, Client
from django.urls import reverse
from .models import Category, Product
from .views import store, categories, product_info, list_category

class StoreViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_store_view(self):
        response = self.client.get(reverse('store'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/store.html')

class CategoriesViewTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        
    def test_categories_view(self):
        response = self.client.get(reverse('categories'))
        self.assertEqual(response.status_code, 200)
        
class ProductInfoViewTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Books', slug='books')
        self.product = Product.objects.create(category=self.category, title='The Great Gatsby', slug='the-great-gatsby')
        self.client = Client()

    def test_product_info_view(self):
        response = self.client.get(reverse('product_info', args=[self.product.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/product-info.html')
        
class ListCategoryViewTest(TestCase):
    
    def setUp(self):
        self.category = Category.objects.create(name='Books', slug='books')
        self.product = Product.objects.create(category=self.category, title='The Great Gatsby', slug='the-great-gatsby')
        self.client = Client()

    def test_list_category_view(self):
        response = self.client.get(reverse('list_category', args=[self.category.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/list-category.html')
