import unittest
from django.test import TestCase
from .models import Category, Product

class CategoryModelTest(TestCase):

    def test_category_string_representation(self):
        category = Category(name='Books')
        self.assertEqual(str(category), 'Books')
    
    def test_category_get_absolute_url(self):
        category = Category(name='Books', slug='books')
        self.assertEqual(category.get_absolute_url(), '/list_category/books/')

class ProductModelTest(TestCase):

    def test_product_string_representation(self):
        product = Product(title='The Great Gatsby')
        self.assertEqual(str(product), 'The Great Gatsby')
    
    def test_product_get_absolute_url(self):
        product = Product(slug='the-great-gatsby')
        self.assertEqual(product.get_absolute_url(), '/product-info/the-great-gatsby/')

if __name__ == '__main__':
    unittest.main()
import unittest
from django.test import TestCase
from .models import Category, Product

class CategoryModelTest(TestCase):

    def test_category_string_representation(self):
        category = Category(name='Books')
        self.assertEqual(str(category), 'Books')
    
    def test_category_get_absolute_url(self):
        category = Category(name='Books', slug='books')
        self.assertEqual(category.get_absolute_url(), '/list_category/books/')

class ProductModelTest(TestCase):

    def test_product_string_representation(self):
        product = Product(title='The Great Gatsby')
        self.assertEqual(str(product), 'The Great Gatsby')
    
    def test_product_get_absolute_url(self):
        product = Product(slug='the-great-gatsby')
        self.assertEqual(product.get_absolute_url(), '/product-info/the-great-gatsby/')

