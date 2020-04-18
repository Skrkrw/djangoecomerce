from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTest(TestCase):
    """Defining the test that will run againts Product Models"""
    
    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')
        