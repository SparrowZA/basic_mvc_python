import unittest
from model import ModelBasic
import basic_backend
from mvc_exceptions import ItemNotStored

class TestModelBasic(unittest.TestCase):

    def test_create_item(self):
        model = ModelBasic([])
        model.create_item('apple', 0.5, 10)
        self.assertEqual(basic_backend.read_item('apple'), {'name': 'apple', 'price': 0.5, 'quantity': 10})

    def test_read_item(self):
        model = ModelBasic([])
        model.create_item('apple', 0.5, 10)
        item = model.read_item('apple')
        self.assertEqual(item, {'name': 'apple', 'price': 0.5, 'quantity': 10})

    def test_update_item(self):
        model = ModelBasic([])
        model.create_item('apple', 0.5, 10)
        model.update_item('apple', 0.6, 11)
        self.assertEqual(basic_backend.read_item('apple'), {'name': 'apple', 'price': 0.6, 'quantity': 11})

    def test_delete_item(self):
        model = ModelBasic([])
        model.create_item('apple', 0.5, 10)
        model.delete_item('apple')
        with self.assertRaises(ItemNotStored) as e:
            basic_backend.read_item('apple')