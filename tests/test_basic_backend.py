from unittest import TestCase
from basic_backend import create_item, read_item, update_item, delete_item
from mvc_exceptions import ItemAlreadyStored, ItemNotStored

class TestBasicBackend(TestCase):
    def test_create_item_when_item_already_stored(self):
        create_item('apple', 0.5, 10)
        with self.assertRaises(ItemAlreadyStored) as e:
            create_item('apple', 0.5, 10)
        self.assertEqual(str(e.exception), '"apple" already stored')

    def test_create_item_when_item_not_stored(self):
        create_item('banana', 0.7, 5)
        self.assertEqual(read_item('banana'), {'name': 'banana', 'price': 0.7, 'quantity': 5})

    def test_read_item_when_item_exists(self):
        create_item('pineapple', 1.2, 3)
        self.assertEqual(read_item('pineapple'), {'name': 'pineapple', 'price': 1.2, 'quantity': 3})

    def test_read_item_when_item_does_not_exist(self):
        with self.assertRaises(ItemNotStored) as e:
            read_item('orange')
        self.assertEqual(str(e.exception), 'Can\'t read "orange" because it was not stored')

    def test_update_item_when_item_exists(self):
        create_item('grape', 0.9, 11)
        update_item('grape', 1.1, 13)
        self.assertEqual(read_item('grape'), {'name': 'grape', 'price': 1.1, 'quantity': 13})

    def test_update_item_when_item_does_not_exist(self):
        with self.assertRaises(ItemNotStored) as e:
            update_item('orange', 0.6, 7)
        self.assertEqual(str(e.exception), 'Can\'t update "orange" because it was not stored')

    def test_delete_item_when_item_exists(self):
        create_item('lemon', 0.5, 13)
        self.assertEqual(read_item('lemon'), {'name': 'lemon', 'price': 0.5, 'quantity': 13})
        delete_item('lemon')
        with self.assertRaises(ItemNotStored) as e:
            read_item('lemon')
        self.assertEqual(str(e.exception), 'Can\'t read "lemon" because it was not stored')

    def test_delete_item_when_item_does_not_exist(self):
        create_item('pineapple', 1.2, 3)
        with self.assertRaises(ItemNotStored) as e:
            delete_item('orange')
        self.assertEqual(str(e.exception), 'Can\'t delete "orange" because it was not stored')

    def test_delete_item_when_item_exists_but_at_a_different_index(self):
        create_item('orange', 0.6, 7)
        create_item('pineapple', 1.2, 3)
        self.assertEqual(read_item('pineapple'), {'name': 'pineapple', 'price': 1.2, 'quantity': 3})
        self.assertEqual(read_item('orange'), {'name': 'orange', 'price': 0.6, 'quantity': 7})
        delete_item('orange')
        self.assertEqual(read_item('pineapple'), {'name': 'pineapple', 'price': 1.2, 'quantity': 3})
        with self.assertRaises(ItemNotStored) as e:
            read_item('orange')
        self.assertEqual(str(e.exception), 'Can\'t read "orange" because it was not stored')
